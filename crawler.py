import requests
from html.parser import HTMLParser
from urllib.parse import urlparse, urljoin
from urllib.robotparser import RobotFileParser

USER_AGENT = "CollegeComparisonPortal/1.0"


class CollegeHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()

        self.title = ""
        self.description = ""

        self.headings = []
        self.links = []
        self.text_parts = []

        self.in_title = False
        self.in_script = False
        self.in_style = False

        self.current_heading = None
        self.current_link = None

    def handle_starttag(self, tag, attrs):

        tag = tag.lower()
        attrs_dict = dict(attrs)

        # -------------------------
        # TITLE
        # -------------------------

        if tag == "title":
            self.in_title = True

        # -------------------------
        # META DESCRIPTION
        # -------------------------

        elif tag == "meta":

            name = attrs_dict.get("name", "").lower()

            if name == "description":

                self.description = attrs_dict.get(
                    "content",
                    ""
                )

        # -------------------------
        # HEADINGS
        # -------------------------

        elif tag in ["h1", "h2", "h3"]:

            self.current_heading = {
                "text": "",
                "url": None
            }

        # -------------------------
        # LINKS
        # -------------------------

        elif tag == "a":

            href = attrs_dict.get("href")

            if href:

                self.current_link = {
                    "url": href,
                    "text": ""
                }

        # -------------------------
        # IGNORE SCRIPT / STYLE
        # -------------------------

        elif tag in [
            "script",
            "style",
            "noscript"
        ]:

            self.in_script = True

    def handle_endtag(self, tag):

        tag = tag.lower()

        # -------------------------
        # TITLE END
        # -------------------------

        if tag == "title":

            self.in_title = False

        # -------------------------
        # HEADING END
        # -------------------------

        elif tag in ["h1", "h2", "h3"]:

            if self.current_heading:

                text = self.current_heading["text"].strip()

                if text:

                    self.headings.append(text)

                    if self.current_heading["url"]:

                        self.links.append({
                            "text": text,
                            "url": self.current_heading["url"]
                        })

            self.current_heading = None

        # -------------------------
        # LINK END
        # -------------------------

        elif tag == "a":

            if self.current_link:

                text = self.current_link["text"].strip()
                url = self.current_link["url"]

                if text and url:

                    self.links.append({
                        "text": text,
                        "url": url
                    })

            self.current_link = None

        # -------------------------
        # SCRIPT / STYLE END
        # -------------------------

        elif tag in [
            "script",
            "style",
            "noscript"
        ]:

            self.in_script = False

    def handle_data(self, data):

        data = data.strip()

        if not data:
            return

        if self.in_script:
            return

        # -------------------------
        # PAGE TITLE
        # -------------------------

        if self.in_title:

            self.title += " " + data

        # -------------------------
        # HEADING TEXT
        # -------------------------

        elif self.current_heading is not None:

            self.current_heading["text"] += " " + data

            if self.current_link:

                self.current_heading["url"] = (
                    self.current_link["url"]
                )

        # -------------------------
        # LINK TEXT
        # -------------------------

        elif self.current_link is not None:

            self.current_link["text"] += " " + data

        else:

            self.text_parts.append(data)


def crawl_college(url):

    try:

        # =====================================================
        # 1. CHECK URL
        # =====================================================

        parsed = urlparse(url)

        if parsed.scheme not in ["http", "https"]:

            return {
                "success": False,
                "error": "Invalid website URL."
            }

        # =====================================================
        # 2. CHECK ROBOTS.TXT
        # =====================================================

        try:

            robots_url = (
                f"{parsed.scheme}://"
                f"{parsed.netloc}/robots.txt"
            )

            rp = RobotFileParser()

            rp.set_url(robots_url)
            rp.read()

            # Website does not allow our crawler
            if not rp.can_fetch(USER_AGENT, url):

                return {
                    "success": False,
                    "error_type": "robots_blocked",
                    "error": (
                        "Automated crawling is not allowed "
                        "by this website's robots.txt."
                    )
                }

        except Exception:

            # If robots.txt cannot be read,
            # continue with the normal HTTP request.
            pass

        # =====================================================
        # 3. REQUEST WEBSITE
        # =====================================================

        response = requests.get(

            url,

            headers={
                "User-Agent": USER_AGENT
            },

            timeout=15
        )

        # =====================================================
        # 4. HANDLE HTTP ERRORS
        # =====================================================

        if response.status_code == 403:

            return {
                "success": False,
                "error_type": "forbidden",
                "error": (
                    "The website refused the crawler request "
                    "(HTTP 403 Forbidden)."
                )
            }

        if response.status_code == 404:

            return {
                "success": False,
                "error_type": "not_found",
                "error": (
                    "The requested webpage was not found "
                    "(HTTP 404)."
                )
            }

        response.raise_for_status()

        # =====================================================
        # 5. PARSE HTML
        # =====================================================

        parser = CollegeHTMLParser()

        parser.feed(response.text)

        # =====================================================
        # 6. TITLE
        # =====================================================

        title = parser.title.strip()

        # =====================================================
        # 7. DESCRIPTION
        # =====================================================

        description = parser.description.strip()

        # =====================================================
        # 8. HEADINGS
        # =====================================================

        headings = parser.headings[:30]

        # =====================================================
        # 9. WEBSITE TEXT
        # =====================================================

        text = " ".join(parser.text_parts)

        text = " ".join(text.split())

        # Keep result manageable
        text = text[:5000]

        # =====================================================
        # 10. CLEAN WEBSITE LINKS
        # =====================================================

        clean_links = []

        seen_urls = set()

        for item in parser.links:

            link_text = item["text"].strip()
            link_url = item["url"].strip()

            # Empty text
            if not link_text:
                continue

            # Empty URL
            if not link_url:
                continue

            # Ignore page anchors
            if link_url.startswith("#"):
                continue

            # Ignore JavaScript
            if link_url.startswith("javascript:"):
                continue

            # Ignore email
            if link_url.startswith("mailto:"):
                continue

            # Ignore phone links
            if link_url.startswith("tel:"):
                continue

            # Convert relative URL to absolute URL
            absolute_url = urljoin(
                url,
                link_url
            )

            parsed_link = urlparse(
                absolute_url
            )

            # Only HTTP / HTTPS
            if parsed_link.scheme not in [
                "http",
                "https"
            ]:
                continue

            # Remove duplicate URLs
            if absolute_url in seen_urls:
                continue

            seen_urls.add(
                absolute_url
            )

            clean_links.append({
                "text": link_text,
                "url": absolute_url
            })

            # Maximum 50 links
            if len(clean_links) >= 50:
                break

        # =====================================================
        # 11. SUCCESS RESULT
        # =====================================================

        return {

            "success": True,

            "url": url,

            "title": title,

            "description": description,

            "headings": headings,

            "links": clean_links,

            "text": text
        }

    # =========================================================
    # REQUEST ERROR
    # =========================================================

    except requests.exceptions.Timeout:

        return {
            "success": False,
            "error_type": "timeout",
            "error": (
                "The website took too long to respond."
            )
        }

    except requests.exceptions.ConnectionError:

        return {
            "success": False,
            "error_type": "connection",
            "error": (
                "Could not connect to the website."
            )
        }

    except requests.exceptions.RequestException as e:

        return {
            "success": False,
            "error_type": "request",
            "error": f"Request error: {e}"
        }

    # =========================================================
    # OTHER ERROR
    # =========================================================

    except Exception as e:

        return {
            "success": False,
            "error_type": "unknown",
            "error": f"Unexpected error: {e}"
        }