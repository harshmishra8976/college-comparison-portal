from flask import Flask, render_template, request
from crawler import crawl_college
import os

# =========================================================
# FLASK CONFIGURATION
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

print("APP PATH:", os.path.abspath(__file__))
print("BASE DIR:", BASE_DIR)
print("TEMPLATES EXISTS:", os.path.exists(os.path.join(BASE_DIR, "templates")))
print("INDEX EXISTS:", os.path.exists(os.path.join(BASE_DIR, "templates", "index.html")))


# =========================================================
# COLLEGE DATABASE (50 COLLEGES)
# =========================================================

colleges = {

    # -----------------------------------------------------
    # IITs (9)
    # -----------------------------------------------------

    "iit bombay": {
        "Full Name": "Indian Institute of Technology Bombay",
        "Short Name": "IITB",
        "Location": "Powai, Mumbai, Maharashtra",
        "Established": "1958",
        "Type": "Government",
        "Courses Offered": "B.Tech, Dual Degree, M.Tech, MSc, MBA, PhD",
        "Admission": "JEE Advanced, GATE, JAM, CAT",
        "Fees": "Approx. ₹2.3 Lakh per year",
        "Placement": "Excellent",
        "Average Package": "Approx. ₹36 LPA",
        "Highest Package": "₹3.67 Crore",
        "Top Recruiters": "Google, Microsoft, Amazon, Apple, Qualcomm, Tata",
        "Hostel": "Available",
        "Library": "Central Library",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Medical Centre, Gym",
        "Official Website": "https://www.iitb.ac.in",
        "Review": "One of India's best engineering institutes.",
        "Why Choose": "Excellent academics, research, infrastructure and placements.",
        "image": "iit_bombay.jpg"
    },

    "iit delhi": {
        "Full Name": "Indian Institute of Technology Delhi",
        "Short Name": "IITD",
        "Location": "New Delhi",
        "Established": "1961",
        "Type": "Government",
        "Courses Offered": "B.Tech, M.Tech, MSc, MBA, PhD",
        "Admission": "JEE Advanced, GATE, JAM, CAT",
        "Fees": "Approx. ₹2.4 Lakh per year",
        "Placement": "Excellent",
        "Average Package": "Approx. ₹25 LPA",
        "Highest Package": "₹2.45 Crore",
        "Top Recruiters": "Google, Microsoft, Amazon, Adobe, Goldman Sachs",
        "Hostel": "Available",
        "Library": "Central Library",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Medical Centre, Gym",
        "Official Website": "https://home.iitd.ac.in",
        "Review": "One of India's top engineering institutes.",
        "Why Choose": "Strong academics, research and excellent placement opportunities.",
        "image": "iit_delhi.jpg"
    },

    "iit madras": {
        "Full Name": "Indian Institute of Technology Madras",
        "Short Name": "IITM",
        "Location": "Chennai, Tamil Nadu",
        "Established": "1959",
        "Type": "Government",
        "Courses Offered": "B.Tech, M.Tech, MSc, MBA, MA, PhD",
        "Admission": "JEE Advanced, GATE, JAM, CAT",
        "Fees": "Approx. ₹2.3 Lakh per year",
        "Placement": "Excellent",
        "Average Package": "Approx. ₹22 LPA",
        "Highest Package": "₹4.3 Crore",
        "Top Recruiters": "Google, Microsoft, Amazon, Qualcomm, Deloitte",
        "Hostel": "Available",
        "Library": "Central Library",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Medical Centre, Gym",
        "Official Website": "https://www.iitm.ac.in",
        "Review": "India's top-ranked engineering institute with excellent academics and research.",
        "Why Choose": "World-class academics, research and infrastructure.",
        "image": "iit_madras.jpg"
    },

    "iit kanpur": {
        "Full Name": "Indian Institute of Technology Kanpur",
        "Short Name": "IITK",
        "Location": "Kanpur, Uttar Pradesh",
        "Established": "1959",
        "Type": "Government",
        "Courses Offered": "B.Tech, BS, M.Tech, MBA, MSc, PhD",
        "Admission": "JEE Advanced, GATE, JAM, CAT",
        "Fees": "Approx. ₹2.3 Lakh per year",
        "Placement": "Excellent",
        "Average Package": "Approx. ₹26 LPA",
        "Highest Package": "₹1.9 Crore",
        "Top Recruiters": "Google, Microsoft, Intel, Samsung, Oracle, Adobe",
        "Hostel": "Available",
        "Library": "Central Library",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Medical Centre, Gym, Auditorium",
        "Official Website": "https://www.iitk.ac.in",
        "Review": "Known for world-class research, innovation and excellent placements.",
        "Why Choose": "Strong research culture and excellent academic environment.",
        "image": "iit_kanpur.jpg"
    },

    "iit kharagpur": {
        "Full Name": "Indian Institute of Technology Kharagpur",
        "Short Name": "IITKGP",
        "Location": "Kharagpur, West Bengal",
        "Established": "1951",
        "Type": "Government",
        "Courses Offered": "B.Tech, B.Arch, LLB, M.Tech, MBA, MSc, PhD",
        "Admission": "JEE Advanced, GATE, JAM, CAT",
        "Fees": "Approx. ₹2.3 Lakh per year",
        "Placement": "Excellent",
        "Average Package": "Approx. ₹24 LPA",
        "Highest Package": "₹2.6 Crore",
        "Top Recruiters": "Google, Microsoft, Amazon, Tata Steel, ISRO, Qualcomm",
        "Hostel": "Available",
        "Library": "Central Library",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Medical Centre, Gym, Stadium",
        "Official Website": "https://www.iitkgp.ac.in",
        "Review": "India's first IIT with a large campus and excellent academics.",
        "Why Choose": "Strong academics, research and placement opportunities.",
        "image": "iit_kharagpur.jpg"
    },

    "iit hyderabad": {
        "Full Name": "Indian Institute of Technology Hyderabad",
        "Short Name": "IITH",
        "Location": "Kandi, Sangareddy, Telangana",
        "Established": "2008",
        "Type": "Government",
        "Courses Offered": "B.Tech, M.Tech, MSc, PhD",
        "Admission": "JEE Advanced, GATE, JAM",
        "Fees": "As per institute norms",
        "Placement": "Excellent","Average Package": "₹20.26 LPA",
        "Highest Package": "₹66.13 LPA",
        
        "Top Recruiters": "Microsoft, Amazon, Google, Deloitte",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Labs, Library, Sports Complex",
        "Official Website": "https://www.iith.ac.in",
        "Review": "Premier IIT known for engineering, research and innovation.",
        "Why Choose": "Strong academics, research opportunities and modern campus.",
        "image": "iit_hyderabad.jpg"
    },

    "iit roorkee": {
        "Full Name": "Indian Institute of Technology Roorkee",
        "Short Name": "IITR",
        "Location": "Roorkee, Uttarakhand",
        "Established": "1847",
        "Type": "Government",
        "Courses Offered": "B.Tech, B.Arch, M.Tech, MSc, MBA, PhD",
        "Admission": "JEE Advanced, GATE, JAM, CAT",
        "Fees": "As per institute norms",
        "Placement": "Excellent",
        "Average Package": "₹20.8 LPA",
        "Highest Package": "₹2.05 Crore",
        "Top Recruiters": "Google, Microsoft, Amazon, Adobe, Deloitte",
        "Hostel": "Available",
        "Library": "Central Library",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Labs, Library, Sports Complex",
        "Official Website": "https://www.iitr.ac.in",
        "Review": "One of India's oldest and most prestigious technical institutes.",
        "Why Choose": "Strong academic heritage, research and excellent placements.",
        "image": "iit_roorkee.jpg"
    },

    "iit guwahati": {
        "Full Name": "Indian Institute of Technology Guwahati",
        "Short Name": "IITG",
        "Location": "Guwahati, Assam",
        "Established": "1994",
        "Type": "Government",
        "Courses Offered": "B.Tech, B.Des, M.Tech, MSc, MBA, PhD",
        "Admission": "JEE Advanced, GATE, JAM, CAT",
        "Fees": "As per institute norms",
        "Placement": "Excellent","Average Package": "₹25.75 LPA",
        "Highest Package": "₹2.4 Crore",
        "Top Recruiters": "Google, Microsoft, Amazon, Qualcomm, Samsung",
        "Hostel": "Available",
        "Library": "Central Library",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Labs, Library, Sports Complex",
        "Official Website": "https://www.iitg.ac.in",
        "Review": "Leading IIT with strong academics, research and a scenic campus.",
        "Why Choose": "Excellent infrastructure, research opportunities and placements.",
        "image": "iit_guwahati.jpg"
    },

    "iit bhu": {
        "Full Name": "Indian Institute of Technology (BHU) Varanasi",
        "Short Name": "IIT BHU",
        "Location": "Varanasi, Uttar Pradesh",
        "Established": "1919",
        "Type": "Government",
        "Courses Offered": "B.Tech, M.Tech, MSc, Integrated M.Tech, PhD",
        "Admission": "JEE Advanced, GATE, JAM",
        "Fees": "As per institute norms",
        "Placement": "Excellent",
        "Average Package": "₹29.25 LPA",
        "Highest Package": "₹1.67 Crore",
        "Top Recruiters": "Google, Microsoft, Amazon, Tata, Deloitte",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Labs, Library, Sports Complex",
        "Official Website": "https://iitbhu.ac.in",
        "Review": "Premier technical institute with a strong academic and research environment.",
        "Why Choose": "Strong engineering programs and established alumni network.",
        "image": "iit_bhu.jpg"
    },

    # -----------------------------------------------------
    # IIMs & MANAGEMENT (18)
    # -----------------------------------------------------

    "iim ahmedabad": {
        "Full Name": "Indian Institute of Management Ahmedabad",
        "Short Name": "IIMA",
        "Location": "Ahmedabad, Gujarat",
        "Established": "1961",
        "Type": "Government",
        "Courses Offered": "MBA, MBA-FABM, Executive MBA, PhD",
        "Admission": "CAT",
        "Fees": "Approx. ₹26 Lakh (2 Years)",
        "Placement": "Excellent",
        
"Average Package": "Approx. ₹35 LPA",
"Highest Package": "₹1.46 Crore",
        "Top Recruiters": "McKinsey, BCG, Bain, Amazon, Google, Microsoft",
        "Hostel": "Available",
        "Library": "Vikram Sarabhai Library",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Medical Centre, Gym",
        "Official Website": "https://www.iima.ac.in",
        "Review": "India's top management institute with world-class faculty and placements.",
        "Why Choose": "Excellent academics, global reputation and outstanding placements.",
        "image": "iim_ahmedabad.jpg"
    },

    "iim bangalore": {
        "Full Name": "Indian Institute of Management Bangalore",
        "Short Name": "IIMB",
        "Location": "Bengaluru, Karnataka",
        "Established": "1973",
        "Type": "Government",
        "Courses Offered": "MBA, Executive MBA, PhD",
        "Admission": "CAT",
        "Fees": "Approx. ₹26 Lakh (2 Years)",
        "Placement": "Excellent",
        
"Average Package": "Approx. ₹35 LPA",
"Highest Package": "₹1.15 Crore",
        "Top Recruiters": "Amazon, Microsoft, BCG, Accenture, Goldman Sachs",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Medical Centre, Gym",
        "Official Website": "https://www.iimb.ac.in",
        "Review": "One of India's premier management institutes.",
        "Why Choose": "Strong industry connections, global recognition and outstanding faculty.",
        "image": "iim_bangalore.jpg"
    },

    "iim calcutta": {
        "Full Name": "Indian Institute of Management Calcutta",
        "Short Name": "IIMC",
        "Location": "Kolkata, West Bengal",
        "Established": "1961",
        "Type": "Government",
        "Courses Offered": "MBA, Executive MBA, MBAEx, PhD",
        "Admission": "CAT",
        "Fees": "Approx. ₹27 Lakh (2 Years)",
        "Placement": "Excellent",
        
"Average Package": "Approx. ₹35 LPA",
"Highest Package": "₹1.15 Crore",
        "Top Recruiters": "BCG, Bain, McKinsey, Amazon, Microsoft, Deloitte",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Medical Centre, Gym",
        "Official Website": "https://www.iimcal.ac.in",
        "Review": "One of India's oldest and most prestigious IIMs.",
        "Why Choose": "Outstanding faculty, alumni network and corporate reputation.",
        "image": "iim_calcutta.jpg"
    },

    "iim lucknow": {
        "Full Name": "Indian Institute of Management Lucknow",
        "Short Name": "IIML",
        "Location": "Lucknow, Uttar Pradesh",
        "Established": "1984",
        "Type": "Government",
        "Courses Offered": "MBA, Executive MBA, IPMX, PhD",
        "Admission": "CAT",
        "Fees": "Approx. ₹21 Lakh (2 Years)",
        "Placement": "Excellent",
        
"Average Package": "Approx. ₹32.3 LPA",
"Highest Package": "₹75 LPA",
        "Top Recruiters": "BCG, Deloitte, EY, Amazon, Accenture, Infosys",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Medical Centre, Gym",
        "Official Website": "https://www.iiml.ac.in",
        "Review": "One of India's leading management institutes.",
        "Why Choose": "Strong alumni network, faculty and placement record.",
        "image": "iim_lucknow.jpg"
    },

    "iim mumbai": {
        "Full Name": "Indian Institute of Management Mumbai",
        "Short Name": "IIMM",
        "Location": "Mumbai, Maharashtra",
        "Established": "1963 as NITIE; IIM Status 2023",
        "Type": "Government",
        "Courses Offered": "MBA, MBA Operations & Supply Chain, Executive MBA, PhD",
        "Admission": "CAT",
        "Fees": "Approx. ₹21 Lakh (2 Years)",
        "Placement": "Excellent",
        
"Average Package": "Approx. ₹31 LPA",
"Highest Package": "₹54 LPA",
        "Top Recruiters": "Amazon, Deloitte, PwC, Accenture, Tata, Reliance",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Medical Centre, Gym",
        "Official Website": "https://iimmumbai.ac.in",
        "Review": "Leading management institute especially known for operations and supply chain.",
        "Why Choose": "Industry-focused curriculum and strong corporate connections.",
        "image": "iim_mumbai.jpg"
    },

    "iim kozhikode": {
        "Full Name": "Indian Institute of Management Kozhikode",
        "Short Name": "IIMK",
        "Location": "Kozhikode, Kerala",
        "Established": "1996",
        "Type": "Government",
        "Courses Offered": "MBA, Executive MBA, PhD",
        "Admission": "CAT",
        "Fees": "Approx. ₹22 Lakh (2 Years)",
        "Placement": "Excellent",
    
"Average Package": "Approx. ₹28 LPA",
"Highest Package": "₹72.02 LPA",
        "Top Recruiters": "Amazon, Deloitte, EY, Accenture, Infosys",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Medical Centre, Gym",
        "Official Website": "https://www.iimk.ac.in",
        "Review": "One of India's fastest-growing IIMs.",
        "Why Choose": "Strong academics, international exposure and excellent placements.",
        "image": "iim_kozhikode.jpg"
    },

    "iim indore": {
        "Full Name": "Indian Institute of Management Indore",
        "Short Name": "IIMI",
        "Location": "Indore, Madhya Pradesh",
        "Established": "1996",
        "Type": "Government",
        "Courses Offered": "MBA, IPM, Executive MBA, PhD",
        "Admission": "CAT, IPMAT",
        "Fees": "Approx. ₹21 Lakh (2 Years)",
        "Placement": "Excellent",
        
"Average Package": "Approx. ₹30 LPA",
"Highest Package": "₹1 Crore",
        "Top Recruiters": "BCG, Amazon, Deloitte, PwC, Infosys",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Medical Centre, Gym",
        "Official Website": "https://www.iimidr.ac.in",
        "Review": "One of India's leading management institutes.",
        "Why Choose": "Strong alumni network, faculty and placement record.",
        "image": "iim_indore.jpg"
    },

    "iim rohtak": {
        "Full Name": "Indian Institute of Management Rohtak",
        "Short Name": "IIM Rohtak",
        "Location": "Rohtak, Haryana",
        "Established": "2010",
        "Type": "Government",
        "Courses Offered": "MBA, IPM, Executive MBA, PhD",
        "Admission": "CAT, IPMAT",
        "Fees": "Course dependent",
        "Placement": "Very Good",
        
"Average Package": "₹19.27 LPA",
"Highest Package": "₹48.25 LPA",
        "Top Recruiters": "Deloitte, EY, KPMG, Accenture, Amazon",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Library, Labs, Wi-Fi, Gym",
        "Official Website": "https://www.iimrohtak.ac.in",
        "Review": "A prominent new-generation IIM.",
        "Why Choose": "Management education, industry exposure and modern facilities.",
        "image": "iim_rohtak.jpg"
    },

    "iim udaipur": {
        "Full Name": "Indian Institute of Management Udaipur",
        "Short Name": "IIM Udaipur",
        "Location": "Udaipur, Rajasthan",
        "Established": "2011",
        "Type": "Government",
        "Courses Offered": "MBA, MBA Global Supply Chain Management, PhD",
        "Admission": "CAT",
        "Fees": "Approx. ₹18 Lakh (2 Years)",
        "Placement": "Excellent",
        
"Average Package": "₹18.77 LPA",
"Highest Package": "₹47.66 LPA",
        "Top Recruiters": "Amazon, Deloitte, Accenture, EY, KPMG",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Library, Sports Facilities",
        "Official Website": "https://www.iimu.ac.in",
        "Review": "One of India's leading new-generation IIMs.",
        "Why Choose": "Strong academics, industry exposure and corporate connections.",
        "image": "iim_udaipur.jpg"
    },

    "iim trichy": {
        "Full Name": "Indian Institute of Management Tiruchirappalli",
        "Short Name": "IIM Trichy",
        "Location": "Tiruchirappalli, Tamil Nadu",
        "Established": "2011",
        "Type": "Government",
        "Courses Offered": "MBA, Executive MBA, PhD",
        "Admission": "CAT",
        "Fees": "Approx. ₹19 Lakh (2 Years)",
        "Placement": "Excellent",
        
"Average Package": "₹19.27 LPA",
"Highest Package": "₹43.94 LPA",
        "Top Recruiters": "Amazon, Deloitte, EY, Accenture, ICICI Bank",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Library, Sports Complex",
        "Official Website": "https://www.iimtrichy.ac.in",
        "Review": "A reputed new-generation IIM.",
        "Why Choose": "Modern campus, good academics and placement opportunities.",
        "image": "iim_trichy.jpg"
    },

    "iim ranchi": {
        "Full Name": "Indian Institute of Management Ranchi",
        "Short Name": "IIM Ranchi",
        "Location": "Ranchi, Jharkhand",
        "Established": "2010",
        "Type": "Government",
        "Courses Offered": "MBA, MBA-HRM, Executive MBA, PhD",
        "Admission": "CAT",
        "Fees": "Approx. ₹17 Lakh (2 Years)",
        "Placement": "Excellent",
        
"Average Package": "₹19.29 LPA",
"Highest Package": "₹50.39 LPA",
        "Top Recruiters": "Amazon, Deloitte, EY, Accenture, KPMG",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Library, Sports Facilities",
        "Official Website": "https://iimranchi.ac.in",
        "Review": "A growing IIM offering quality management education.",
        "Why Choose": "Strong faculty, industry exposure and career opportunities.",
        "image": "iim_ranchi.jpg"
    },

    "iim raipur": {
        "Full Name": "Indian Institute of Management Raipur",
        "Short Name": "IIM Raipur",
        "Location": "Raipur, Chhattisgarh",
        "Established": "2010",
        "Type": "Government",
        "Courses Offered": "MBA, Executive MBA, PhD",
        "Admission": "CAT",
        "Fees": "Approx. ₹18 Lakh (2 Years)",
        "Placement": "Excellent",
        
"Average Package": "₹21.04 LPA",
"Highest Package": "₹67.60 LPA",
        "Top Recruiters": "Amazon, Deloitte, Accenture, EY, KPMG",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Library, Sports Complex",
        "Official Website": "https://iimraipur.ac.in",
        "Review": "One of the prominent new-generation IIMs.",
        "Why Choose": "Good placements, modern infrastructure and industry-oriented education.",
        "image": "iim_raipur.jpg"
    },

    "iim kashipur": {
        "Full Name": "Indian Institute of Management Kashipur",
        "Short Name": "IIM Kashipur",
        "Location": "Kashipur, Uttarakhand",
        "Established": "2011",
        "Type": "Government",
        "Courses Offered": "MBA, MBA Analytics, Executive MBA, PhD",
        "Admission": "CAT",
        "Fees": "Approx. ₹17 Lakh (2 Years)",
        "Placement": "Excellent",
        
"Average Package": "₹14.95 LPA",
"Highest Package": "₹33.12 LPA",
        "Top Recruiters": "Amazon, Deloitte, Accenture, EY, Infosys",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Library, Sports Complex",
        "Official Website": "https://www.iimkashipur.ac.in",
        "Review": "A reputed new-generation IIM.",
        "Why Choose": "Strong management programs and industry exposure.",
        "image": "iim_kashipur.jpg"
    },

    "fms delhi": {
        "Full Name": "Faculty of Management Studies, University of Delhi",
        "Short Name": "FMS Delhi",
        "Location": "New Delhi",
        "Established": "1954",
        "Type": "Government",
        "Courses Offered": "MBA, Executive MBA, PhD",
        "Admission": "CAT",
        "Fees": "Approx. ₹2 Lakh (2 Years)",
        "Placement": "Excellent",
        "Average Package": "₹34.10 LPA",
        "Highest Package": "₹1.23 Crore",
        "Top Recruiters": "McKinsey, BCG, Amazon, Microsoft, Aditya Birla Group",
        "Hostel": "Limited",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Library, Wi-Fi, Labs, Seminar Hall",
        "Official Website": "https://fms.edu",
        "Review": "One of India's best MBA colleges with excellent ROI.",
        "Why Choose": "Low fees, outstanding placements and strong alumni network.",
        "image": "fms_delhi.jpg"
    },

    "xlri jamshedpur": {
        "Full Name": "XLRI - Xavier School of Management",
        "Short Name": "XLRI",
        "Location": "Jamshedpur, Jharkhand",
        "Established": "1949",
        "Type": "Private",
        "Courses Offered": "PGDM BM, PGDM HRM, Executive PGDM, FPM",
        "Admission": "XAT, GMAT",
        "Fees": "Approx. ₹30 Lakh (2 Years)",
        "Placement": "Excellent",
        "Average Package": "₹29.89 LPA",
"Highest Package": "₹1.10 Crore",
        "Top Recruiters": "BCG, Bain, Accenture, Deloitte, Amazon, Tata",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Medical Centre, Gym",
        "Official Website": "https://xlri.ac.in",
        "Review": "India's oldest and one of the best private business schools.",
        "Why Choose": "Excellent placements and top HR program.",
        "image": "xlri.jpg"
    },

    "kj somaiya": {
        "Full Name": "K J Somaiya Institute of Management",
        "Short Name": "KJSIM",
        "Location": "Mumbai, Maharashtra",
        "Established": "1981",
        "Type": "Private",
        "Courses Offered": "MBA, MBA Executive, PhD",
        "Admission": "CAT, XAT, CMAT, NMAT",
        "Fees": "Approx. ₹22 Lakh (2 Years)",
        "Placement": "Very Good",
        "Average Package": "₹12.23 LPA",
"Highest Package": "₹27.50 LPA",
        "Top Recruiters": "Deloitte, KPMG, EY, Infosys, ICICI Bank",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Medical Centre, Auditorium",
        "Official Website": "https://kjsim.somaiya.edu",
        "Review": "One of Mumbai's leading private management institutes.",
        "Why Choose": "Strong industry connections and modern campus.",
        "image": "kj_somaiya.jpg"
    },

    "spjimr": {
        "Full Name": "S. P. Jain Institute of Management and Research",
        "Short Name": "SPJIMR",
        "Location": "Mumbai, Maharashtra",
        "Established": "1981",
        "Type": "Private",
        "Courses Offered": "PGDM, PGPM, Executive MBA, FPM",
        "Admission": "CAT, GMAT",
        "Fees": "Approx. ₹24 Lakh (2 Years)",
        "Placement": "Excellent",
        "Average Package": "₹32.06 LPA",
"Highest Package": "₹81 LPA",
        "Top Recruiters": "BCG, Bain, Amazon, Deloitte, Accenture",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Wi-Fi, Labs, Medical Centre, Auditorium",
        "Official Website": "https://www.spjimr.org",
        "Review": "One of India's top private management institutes.",
        "Why Choose": "Industry-oriented curriculum and excellent placements.",
        "image": "spjimr.jpg"
    },

    "jbims": {
        "Full Name": "Jamnalal Bajaj Institute of Management Studies",
        "Short Name": "JBIMS",
        "Location": "Mumbai, Maharashtra",
        "Established": "1965",
        "Type": "Government",
        "Courses Offered": "MBA, MMS, MSc Finance, PhD",
        "Admission": "MAH MBA CET, CAT, CMAT",
        "Fees": "Approx. ₹6 Lakh (2 Years)",
        "Placement": "Excellent",
        "Average Package": "₹28.02 LPA",
"Highest Package": "₹55.60 LPA",
        "Top Recruiters": "Goldman Sachs, JP Morgan, Deloitte, Accenture, HDFC Bank",
        "Hostel": "Limited",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Library, Wi-Fi, Labs, Seminar Hall",
        "Official Website": "https://jbims.edu",
        "Review": "One of India's premier management institutes.",
        "Why Choose": "Low fees, excellent placements and strong alumni network.",
        "image": "jbims.jpg"
    },

    # -----------------------------------------------------
    # TECHNICAL, DEGREE COLLEGES & UNIVERSITIES (23)
    # -----------------------------------------------------

    "nit trichy": {
        "Full Name": "National Institute of Technology Tiruchirappalli",
        "Short Name": "NIT Trichy",
        "Location": "Tiruchirappalli, Tamil Nadu",
        "Established": "1964",
        "Type": "Government",
        "Courses Offered": "B.Tech, M.Tech, MSc, MBA, MCA, PhD",
        "Admission": "JEE Main, GATE, JAM, CAT",
        "Fees": "As per institute norms",
        "Placement": "Excellent",
        "Average Package": "₹14.35 LPA",
"Highest Package": "₹55 LPA",
        "Top Recruiters": "Amazon, Microsoft, Google, Deloitte, Qualcomm",
        "Hostel": "Available",
        "Library": "Central Library",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Labs, Library, Sports Complex",
        "Official Website": "https://www.nitt.edu",
        "Review": "One of India's leading NITs.",
        "Why Choose": "Excellent engineering education and industry exposure.",
        "image": "nit_trichy.jpg"
    },

    "nit warangal": {
        "Full Name": "National Institute of Technology Warangal",
        "Short Name": "NIT Warangal",
        "Location": "Warangal, Telangana",
        "Established": "1959",
        "Type": "Government",
        "Courses Offered": "B.Tech, M.Tech, MSc, MBA, MCA, PhD",
        "Admission": "JEE Main, GATE, JAM, CAT",
        "Fees": "Course dependent",
        "Placement": "Excellent",
        "Average Package": "₹17 LPA",
"Highest Package": "₹88 LPA",
        "Top Recruiters": "Microsoft, Amazon, Google, Deloitte, Oracle",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Labs, Library, Wi-Fi, Sports Facilities",
        "Official Website": "https://www.nitw.ac.in",
        "Review": "Highly reputed technical institute.",
        "Why Choose": "Strong technical programs, research and good placements.",
        "image": "nit_warangal.jpg"
    },

    "bits pilani": {
        "Full Name": "Birla Institute of Technology and Science, Pilani",
        "Short Name": "BITS Pilani",
        "Location": "Pilani, Rajasthan",
        "Established": "1964",
        "Type": "Private",
        "Courses Offered": "BE, MSc, M.E., MBA, PhD",
        "Admission": "BITSAT / Entrance Based",
        "Fees": "Course dependent",
        "Placement": "Excellent",
        "Average Package": "₹17.01 LPA",
"Highest Package": "₹60.75 LPA",
        "Top Recruiters": "Google, Microsoft, Amazon, Adobe, Qualcomm",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Labs, Library, Wi-Fi, Sports Complex",
        "Official Website": "https://www.bits-pilani.ac.in",
        "Review": "One of India's leading private technical institutes.",
        "Why Choose": "Flexible curriculum and strong placement opportunities.",
        "image": "bits_pilani.jpg"
    },

    "bk birla college": {
        "Full Name": "B. K. Birla College of Arts, Science and Commerce",
        "Short Name": "BK Birla College",
        "Location": "Kalyan, Maharashtra",
        "Established": "1972",
        "Type": "Private",
        "Courses Offered": "BA, BCom, BSc, BMS, BAF, BBI, BMM, MSc, MCom, PhD",
        "Admission": "Merit Based",
        "Fees": "As per University Norms",
        "Placement": "Good",
        "Average Package": "₹3 LPA",
"Highest Package": "₹8 LPA",
        "Hostel": "Not Available",
        "Library": "Available",
        "Sports": "Available",
        "Facilities": "Library, Computer Labs, Wi-Fi, Auditorium, Sports Complex",
        "Official Website": "https://bkbirlacollegekalyan.com",
        "Review": "One of the leading colleges affiliated with the University of Mumbai.",
        "Why Choose": "Good academics, experienced faculty and affordable fees.",
        "image": "bk_birla.jpg"
    },

    "rj college": {
        "Full Name": "Hindi Vidya Prachar Samiti's Ramniranjan Jhunjhunwala College of Arts, Science & Commerce",
        "Short Name": "RJ College",
        "Location": "Ghatkopar, Mumbai, Maharashtra",
        "Established": "1963",
        "Type": "Private",
        "Courses Offered": "BA, BCom, BSc, BMS, BAF, BBI, BMM, BSc IT, BSc CS, BSc Biotechnology, MSc, MCom",
        "Admission": "Merit Based",
        "Fees": "As per University Norms",
        "Placement": "Good",
        "Average Package": "₹4.5 LPA",
"Highest Package": "₹12 LPA",
        "Top Recruiters": "TCS, Infosys, Wipro, Capgemini, Accenture",
        "Hostel": "Not Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Library, Computer Labs, Wi-Fi, Auditorium, Gymkhana",
        "Official Website": "https://www.rjcollege.edu.in",
        "Review": "A reputed autonomous college affiliated with the University of Mumbai.",
        "Why Choose": "Quality education, autonomous curriculum and good placement support.",
        "image": "rj_college.jpg"
    },

    "achievers college": {
        "Full Name": "Achievers College of Commerce and Management",
        "Short Name": "Achievers College",
        "Location": "Kalyan, Maharashtra",
        "Established": "2015",
        "Type": "Private",
        "Courses Offered": "BCom, BMS, BAF, BBI, BSc IT, BSc CS",
        "Admission": "Merit Based",
        "Fees": "As per College Norms",
        "Placement": "Good",
        "Average Package": "₹3.5 LPA",
"Highest Package": "₹8 LPA",
        "Top Recruiters": "TCS, Wipro, Infosys, Tech Mahindra",
        "Hostel": "Not Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Library, Computer Labs, Wi-Fi, Seminar Hall",
        "Official Website": "https://achieversccm.ac.in",
        "Review": "A growing college offering commerce and management education.",
        "Why Choose": "Affordable fees, practical learning and student-friendly environment.",
        "image": "achievers.jpg"
    },

    "nm college": {
        "Full Name": "Narsee Monjee College of Commerce and Economics",
        "Short Name": "NM College",
        "Location": "Vile Parle, Mumbai, Maharashtra",
        "Established": "1964",
        "Type": "Private",
        "Courses Offered": "BCom, BMS, BAF, BBI, BFM, BSc IT, BSc CS, MCom",
        "Admission": "Merit Based",
        "Fees": "As per University Norms",
        "Placement": "Good",
        "Average Package": "₹5 LPA",
"Highest Package": "₹12 LPA",
        "Top Recruiters": "Deloitte, TCS, Infosys, EY, KPMG",
        "Hostel": "Not Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Library, Computer Labs, Wi-Fi, Auditorium",
        "Official Website": "https://nmcollege.in",
        "Review": "One of Mumbai's well-known commerce and management colleges.",
        "Why Choose": "Strong academics and good industry exposure.",
        "image": "nm_college.jpg"
    },

    "mithibai college": {
        "Full Name": "Mithibai College of Arts, Science and Commerce",
        "Short Name": "Mithibai College",
        "Location": "Vile Parle, Mumbai, Maharashtra",
        "Established": "1961",
        "Type": "Private",
        "Courses Offered": "BA, BCom, BSc, BMS, BSc IT, BSc CS, MSc, MCom",
        "Admission": "Merit Based",
        "Fees": "As per University Norms",
        "Placement": "Good",
        "Average Package": "₹5 LPA",
"Highest Package": "₹12 LPA",
        "Top Recruiters": "TCS, Deloitte, Infosys, Accenture, EY",
        "Hostel": "Not Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Library, Computer Labs, Wi-Fi, Auditorium",
        "Official Website": "https://mithibai.ac.in",
        "Review": "A reputed autonomous college in Mumbai.",
        "Why Choose": "Good academics, facilities and extracurricular opportunities.",
        "image": "mithibai.jpg"
    },

    "st xaviers college": {
        "Full Name": "St. Xavier's College, Mumbai",
        "Short Name": "St. Xavier's",
        "Location": "Fort, Mumbai, Maharashtra",
        "Established": "1869",
        "Type": "Private",
        "Courses Offered": "BA, BCom, BSc, BMS, MSc, MA",
        "Admission": "Merit Based / Entrance",
        "Fees": "As per College Norms",
        "Placement": "Good",
        "Average Package": "₹5 LPA",
"Highest Package": "₹12 LPA",
        "Top Recruiters": "TCS, Deloitte, EY, KPMG, Accenture",
        "Hostel": "Limited",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Library, Labs, Computer Labs, Auditorium, Sports Facilities",
        "Official Website": "https://xaviers.ac",
        "Review": "One of Mumbai's most reputed colleges.",
        "Why Choose": "Strong academic reputation and vibrant campus life.",
        "image": "st_xaviers.jpg"
    },

    "jai hind college": {
        "Full Name": "Jai Hind College",
        "Short Name": "Jai Hind College",
        "Location": "Churchgate, Mumbai, Maharashtra",
        "Established": "1948",
        "Type": "Private",
        "Courses Offered": "BA, BCom, BSc, BMS, BAF, BBI, BSc IT",
        "Admission": "Merit Based",
        "Fees": "As per College Norms",
        "Placement": "Good",
        "Average Package": "₹5 LPA",
"Highest Package": "₹12 LPA",
        "Top Recruiters": "Deloitte, TCS, EY, KPMG, Infosys",
        "Hostel": "Not Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Library, Computer Labs, Wi-Fi, Auditorium, Seminar Hall",
        "Official Website": "https://jaihindcollege.com",
        "Review": "A well-known Mumbai college.",
        "Why Choose": "Good academics, industry exposure and extracurricular activities.",
        "image": "jai_hind.jpg"
    },

    "hr college": {
        "Full Name": "H. R. College of Commerce and Economics",
        "Short Name": "HR College",
        "Location": "Churchgate, Mumbai, Maharashtra",
        "Established": "1960",
        "Type": "Private",
        "Courses Offered": "BCom, BMS, BAF, BBI, BFM, MCom",
        "Admission": "Merit Based",
        "Fees": "As per University Norms",
        "Placement": "Good",
        "Average Package": "₹5 LPA",
"Highest Package": "₹12 LPA",
        "Top Recruiters": "Deloitte, EY, KPMG, TCS, Accenture",
        "Hostel": "Not Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Library, Computer Labs, Wi-Fi, Auditorium",
        "Official Website": "https://www.hrcollege.edu",
        "Review": "A reputed commerce and management college in South Mumbai.",
        "Why Choose": "Strong commerce education and industry exposure.",
        "image": "hr_college.jpg"
    },

    "km agrawal college": {
        "Full Name": "K. M. Agrawal College of Arts, Commerce & Science",
        "Short Name": "K. M. Agrawal College",
        "Location": "Kalyan West, Maharashtra",
        "Established": "1994",
        "Type": "Private",
        "Courses Offered": "BA, BCom, BSc, BSc CS, BSc IT, BMS, BAF, BBI, MSc, MCom",
        "Admission": "Merit Based",
        "Fees": "As per University Norms",
        "Placement": "Good",
        "Average Package": "₹3 LPA",
"Highest Package": "₹8 LPA",
        "Hostel": "Not Available",
        "Library": "Available",
        "Sports": "Available",
        "Facilities": "Library, Computer Labs, Wi-Fi, Auditorium, Sports Facilities",
        "Official Website": "https://www.kmagrawalcollege.org",
        "Review": "A reputed college in Kalyan.",
        "Why Choose": "Affordable education and diverse courses.",
        "image": "km_agrawal.jpg"
    },

    "thane college": {
        "Full Name": "Thane College",
        "Short Name": "Thane College",
        "Location": "Thane, Maharashtra",
        "Established": "1960",
        "Type": "Private",
        "Courses Offered": "BA, BCom, BSc, BMS",
        "Admission": "Merit Based",
        "Fees": "As per University Norms",
        "Placement": "Good",
        "Average Package": "₹3 LPA",
"Highest Package": "Not Disclosed",
        "Hostel": "Not Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Library, Computer Labs, Wi-Fi, Auditorium",
        "Official Website": "https://www.thanecollege.org",
        "Review": "A local degree college serving students in the Thane region.",
        "Why Choose": "Convenient location and affordable education.",
        "image": "thane_college.jpg"
    },

    "ruia college": {
        "Full Name": "Ramnarain Ruia Autonomous College",
        "Short Name": "Ruia College",
        "Location": "Matunga, Mumbai, Maharashtra",
        "Established": "1937",
        "Type": "Private",
        "Courses Offered": "BA, BSc, BCom, BVoc, MSc and other programs",
        "Admission": "Merit Based",
        "Fees": "As per College Norms",
        "Placement": "Good",
        "Average Package": "Not Disclosed",
"Highest Package": "Not Disclosed",
        "Hostel": "Not Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Library, Labs, Wi-Fi, Research Centres, Sports Facilities",
        "Official Website": "https://ruiacollege.edu",
        "Review": "One of Mumbai's well-known autonomous colleges.",
        "Why Choose": "Strong academics and autonomous curriculum.",
        "image": "ruia_college.jpg"
    },

    "shree ram college bhandup": {
        "Full Name": "Shree Ram College",
        "Short Name": "Shree Ram College",
        "Location": "Bhandup, Mumbai, Maharashtra",
        "Established": "2010",
        "Type": "Private",
        "Courses Offered": "BCom, BMS, BAF, BBI, BSc IT, BSc CS",
        "Admission": "Merit Based",
        "Fees": "As per College Norms",
        "Placement": "Good",
        "Average Package": "₹3 LPA",
"Highest Package": "Not Disclosed",
        "Hostel": "Not Available",
        "Library": "Available",
        "Sports": "Available",
        "Facilities": "Library, Computer Labs, Wi-Fi, Seminar Hall",
        "Official Website": "College Website",
        "Review": "A local college offering undergraduate programs.",
        "Why Choose": "Convenient location and career-oriented courses.",
        "image": "shree_ram_college.jpg"
    },

    "thakur college of engineering": {
        "Full Name": "Thakur College of Engineering and Technology",
        "Short Name": "TCET",
        "Location": "Kandivali East, Mumbai, Maharashtra",
        "Established": "2001",
        "Type": "Private",
        "Courses Offered": "BE/BTech, MTech, PhD, Vocational Programs",
        "Admission": "MHT-CET, JEE Main",
        "Fees": "As per College / Government Norms",
        "Placement": "Good",
        "Average Package": "₹6 LPA",
"Highest Package": "₹24 LPA",
        "Top Recruiters": "TCS, Infosys, Accenture, Capgemini",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Labs, Library, Wi-Fi, Computer Centre, Sports Facilities",
        "Official Website": "https://www.tcetmumbai.in",
        "Review": "A well-known autonomous engineering institute in Kandivali.",
        "Why Choose": "Engineering-focused education and modern facilities.",
        "image": "thakur_engineering.jpg"
    },

    "christ university": {
        "Full Name": "Christ (Deemed to be University)",
        "Short Name": "CHRIST",
        "Location": "Bengaluru, Karnataka",
        "Established": "2008",
        "Type": "Private",
        "Courses Offered": "BBA, BCom, BCA, BSc, MBA, MSc, PhD",
        "Admission": "University Entrance / Merit / CAT",
        "Fees": "Course dependent",
        "Placement": "Very Good",
        "Average Package": "₹7.5 LPA",
"Highest Package": "₹20 LPA",
        "Top Recruiters": "Deloitte, EY, KPMG, Accenture, TCS",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Labs, Library, Hostel, Wi-Fi, Sports Complex",
        "Official Website": "https://christuniversity.in",
        "Review": "Well-known private university with a wide range of programs.",
        "Why Choose": "Strong academics, campus facilities and industry exposure.",
        "image": "christ_university.jpg"
    },

    "nmims": {
        "Full Name": "SVKM's Narsee Monjee Institute of Management Studies",
        "Short Name": "NMIMS",
        "Location": "Mumbai, Maharashtra",
        "Established": "1981",
        "Type": "Private",
        "Courses Offered": "BBA, BCom, BTech, MBA, MSc, PhD",
        "Admission": "NPAT, NMAT, Merit",
        "Fees": "Course dependent",
        "Placement": "Excellent",
        "Average Package": "₹13.06 LPA",
"Highest Package": "₹67.70 LPA",
        "Top Recruiters": "Deloitte, EY, KPMG, Accenture, Amazon",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Library, Labs, Wi-Fi, Hostel, Auditorium",
        "Official Website": "https://www.nmims.edu",
        "Review": "Well-known private university, particularly strong in management.",
        "Why Choose": "Strong industry connections and professional courses.",
        "image": "nmims.jpg"
    },

    "symbiosis pune": {
        "Full Name": "Symbiosis International (Deemed University)",
        "Short Name": "SIU",
        "Location": "Pune, Maharashtra",
        "Established": "2002",
        "Type": "Private",
        "Courses Offered": "BBA, BCA, BSc, MBA, MSc, Law, Engineering",
        "Admission": "SET, SNAP, Merit",
        "Fees": "Course dependent",
        "Placement": "Very Good",
        "Average Package": "₹8.8 LPA",
"Highest Package": "₹28 LPA",
        "Top Recruiters": "Deloitte, Infosys, Accenture, TCS, Wipro",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Hostel, Library, Labs, Wi-Fi, Sports Facilities",
        "Official Website": "https://www.siu.edu.in",
        "Review": "A reputed private university known for management, law and professional education.",
        "Why Choose": "Wide range of programs and strong campus facilities.",
        "image": "symbiosis_pune.jpg"
    },

    "university of mumbai": {
        "Full Name": "University of Mumbai",
        "Short Name": "MU",
        "Location": "Mumbai, Maharashtra",
        "Established": "1857",
        "Type": "Government",
        "Courses Offered": "BA, BCom, BSc, BMS, BSc CS, MA, MCom, MSc, PhD",
        "Admission": "Merit / Entrance Based",
        "Fees": "As per University Norms",
        "Placement": "Good",
        "Average Package": "Not Disclosed",
"Highest Package": "Not Disclosed",
        "Top Recruiters": "TCS, Infosys, Wipro, Accenture, Deloitte",
        "Hostel": "Available at selected campuses",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Library, Computer Labs, Research Facilities, Sports",
        "Official Website": "https://mu.ac.in",
        "Review": "One of India's oldest public universities.",
        "Why Choose": "Large academic network and wide course selection.",
        "image": "university_mumbai.jpg"
    },

    "pune university": {
        "Full Name": "Savitribai Phule Pune University",
        "Short Name": "SPPU",
        "Location": "Pune, Maharashtra",
        "Established": "1949",
        "Type": "Government",
        "Courses Offered": "BA, BCom, BSc, BCA, BBA, MA, MCom, MSc, MBA, PhD",
        "Admission": "Merit / Entrance Based",
        "Fees": "As per University Norms",
        "Placement": "Good",
        "Average Package": "Not Disclosed",
"Highest Package": "Not Disclosed",
        "Top Recruiters": "TCS, Infosys, Wipro, Accenture, Deloitte",
        "Hostel": "Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Library, Research Centres, Labs, Hostel, Sports",
        "Official Website": "https://www.unipune.ac.in",
        "Review": "One of Maharashtra's leading public universities.",
        "Why Choose": "Strong academic reputation and diverse courses.",
        "image": "sppu.jpg"
    },

    "sies college": {
        "Full Name": "SIES College of Arts, Science and Commerce",
        "Short Name": "SIES College",
        "Location": "Sion, Mumbai, Maharashtra",
        "Established": "1960",
        "Type": "Private / Autonomous",
        "Courses Offered": "BA, BCom, BSc, BMS, BSc IT, BSc CS, MSc, MCom",
        "Admission": "Merit Based",
        "Fees": "As per College Norms",
        "Placement": "Good",
        "Average Package": "₹4.5 LPA",
"Highest Package": "₹12 LPA",
        "Top Recruiters": "TCS, Infosys, Deloitte, Accenture, Wipro",
        "Hostel": "Not Available",
        "Library": "Available",
        "Sports": "Indoor & Outdoor Sports",
        "Facilities": "Library, Computer Labs, Wi-Fi, Laboratories, Auditorium, Sports Facilities",
        "Official Website": "https://siesascs.edu.in",
        "Review": "A reputed autonomous college in Mumbai offering undergraduate and postgraduate programs.",
        "Why Choose": "Good academic environment, diverse courses and convenient Mumbai location.",
        "image": "sies_college.jpg"
    },

    "kc college": {
        "Full Name": "K.C. College of Arts, Commerce and Science",
        "Short Name": "K.C. College",
        "Location": "Churchgate, Mumbai, Maharashtra",
        "Established": "1954",
        "Type": "Private / Autonomous",
        "Courses Offered": "BA, BCom, BSc, BMS, BAF, BBI, BSc IT, BSc CS, MSc, MCom",
        "Admission": "Merit Based",
        "Fees": "As per College Norms",
        "Placement": "Good",
        "Average Package": "₹5 LPA",
"Highest Package": "₹12 LPA",
        "Top Recruiters": "TCS, Infosys, Deloitte, EY, Accenture",
        "Hostel": "Not Available",
        "Library": "Available",
        "Sports": "Available",
        "Facilities": "Library, Computer Labs, Wi-Fi, Auditorium, Sports Facilities",
        "Official Website": "https://kccollege.edu.in",
        "Review": "A well-known autonomous college in South Mumbai.",
        "Why Choose": "Good academics, diverse undergraduate programs and convenient Mumbai location.",
        "image": "kc_college.jpg"
    }
}


# =========================================================
# HOME
# =========================================================

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        college_name = request.form.get(
            "college",
            ""
        ).strip().lower()

        if college_name in colleges:
            result = colleges[college_name]

        else:
            result = {
                "Error": "College not found in database."
            }

    return render_template(
        "index.html",
        result=result,
        colleges=colleges
    )


# =========================================================
# TOP COLLEGES
# =========================================================

@app.route("/top-colleges")
def top_colleges():

    return render_template(
        "top_colleges.html",
        colleges=colleges
    )


# =========================================================
# COMPARE COLLEGES
# =========================================================

@app.route("/compare", methods=["GET", "POST"])
def compare():

    college1 = None
    college2 = None

    if request.method == "POST":

        c1 = request.form.get(
            "college1",
            ""
        ).strip().lower()

        c2 = request.form.get(
            "college2",
            ""
        ).strip().lower()

        if c1 in colleges:
            college1 = colleges[c1]

        if c2 in colleges:
            college2 = colleges[c2]

    return render_template(
        "compare.html",
        colleges=colleges,
        college1=college1,
        college2=college2
    )


# =========================================================
# RUN APPLICATION
# =========================================================
@app.route("/crawler", methods=["GET", "POST"])
def crawler_page():

    selected = None
    result = None

    if request.method == "POST":

        selected = request.form.get("college")

        # Only allow colleges already present
        # in the existing 50-college dictionary
        if selected in colleges:

            website = colleges[selected].get("Official Website")

            if website:
                result = crawl_college(website)

            else:
                result = {
                    "success": False,
                    "error": "Official website is not available for this college."
                }

        else:

            result = {
                "success": False,
                "error": "Invalid college selected."
            }

    return render_template(
        "crawler.html",
        colleges=colleges,
        selected=selected,
        result=result
    )

# =========================================================
# COURSE SEARCH
# =========================================================

@app.route("/course-search", methods=["GET", "POST"])
def course_search():

    results = []
    search_course = ""

    # Normal search box
    if request.method == "POST":
        search_course = request.form.get("course", "").strip()

    # Popular Course button
    else:
        search_course = request.args.get("course", "").strip()

    if search_course:

        query = search_course.lower()

        for college_name, college_data in colleges.items():

            courses = college_data.get(
                "Courses Offered",
                ""
            ).lower()

            if query in courses:

                result = college_data.copy()

                result["College Key"] = college_name
                result["Matched Course"] = search_course

                results.append(result)

    return render_template(
        "course_search.html",
        colleges=colleges,
        results=results,
        search_course=search_course
    )
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(
            os.environ.get(
                "PORT",
                5000
            )
        ),
        debug=True
    )
