# Below are the import statements 

from ibapi.wrapper import *
from ibapi.client import *
from ibapi.contract import *
from ibapi.order import *
from threading import Thread
import queue
import datetime
import time
from bs4 import BeautifulSoup
import requests
from random import randint

# Below are the global variables

tickers = [
"amazon",
"shopify",
"the",
"square",
"mercadolibre",
"paypal",
"twilio",
"mongodb",
"arista",
"netflix",
"apple",
"facebook",
"paycom",
"etsy",
"mastercard",
"teladoc",
"okta",
"veeva",
"appian",
"docusign",
"hubspot",
"alteryx",
"tesla",
"walt",
"roku",
"salesforce.com",
"alphabet",
"redfin",
"nvidia",
"datadog",
"zscaler",
"pinterest",
"crowdstrike",
"starbucks",
"zoom",
"axon",
"activision",
"atlassian",
"adobe",
"american",
"intuitive",
"tencent",
"take-two",
"cloudflare,",
"wix.com",
"stitch",
"fastly",
"ulta",
"align",
"cognex",
"workday",
"jd.com",
"illumina",
"fiverr",
"monster",
"blackline,",
"autodesk",
"markel",
"chipotle",
"peloton",
"servicenow,",
"zendesk",
"irobot",
"accenture",
"skyworks",
"match",
"proto",
"upstart",
"sea",
"twitter",
"editas",
"iqiyi",
"ipg",
"berkshire",
"upwork",
"idexx",
"zillow",
"costco",
"guardant",
"electronic",
"splunk",
"novocure",
"mccormick",
"equinix",
"nutanix",
"masimo",
"tractor",
"ubiquiti",
"airbnb,",
"zynga",
"healthequity",
"invitae",
"abiomed",
"unity",
"varonis",
"fortinet",
"lululemon",
"live",
"interactive",
"aerovironment",
"ii-vi",
"lam",
"axos",
"nike",
"nextera",
"moderna",
"new",
"bumble",
"jack",
"dexcom",
"asml",
"baozun",
"ss&c",
"planet",
"booking",
"palo",
"ionis",
"gilead",
"wingstop",
"trex",
"lemonade,",
"coupang,",
"baidu",
"intuit",
"bluebird",
"dassault",
"xilinx",
"beyond",
"kinder",
"rollins",
"hca",
"intercontinental",
"texas",
"five",
"fedex",
"hasbro",
"vail",
"middleby",
"bilibili",
"logitech",
"synopsys",
"fubotv,",
"gartner",
"cintas",
"westinghouse",
"williams-sonoma",
"skechers",
"balchem",
"freshpet",
"boston",
"wayfair",
"coupa",
"hyatt",
"nintendo",
"uber",
"roblox",
"ollie's",
"goodrx",
"copart",
"godaddy",
"liveperson",
"hello",
"netease",
"rh",
"sirius",
"sleep",
"factset",
"alaska",
"zebra",
"ebay",
"alkermes",
"alnylam",
"amgen",
"broadcom",
"blackbaud",
"first",
"chart",
"lkq",
"mastec",
"nice",
"nuvasive",
"novo",
"resmed",
"seagen",
"shockwave",
"vertex",
"biogen",
"exelixis",
"blackberry",
"svb",
"western",
"waste",
"biomarin",
"caseys",
"2u",
"anheuser-busch",
"unitedhealth",
"core",
"t-mobile",
"criteo",
"under",
"cboe",
"cme",
"littelfuse",
"old",
"grupo",
"rpm",
"3m",
"camping",
"cummins",
"emergent",
"watsco",
"oceaneering",
"cvs",
"marriott",
"sherwin-williams",
"the",
"staar",
"nxp",
"transdigm",
"textron",
]

# Global variables for the scraper 

textContent = []    # Holds the headlines in an array 
cycleCount = 0      # Stores the frequency of requests made to the server 
tempHeadlineHolder = [] # Array to hold the most recent headline before it has been analyzed

# Below are the custom classes and methods 

def economistSearch():
    page_link = 'https://www.economist.com/'    # Page Url to point request where to crawl 
    page_response = requests.get(page_link, timeout=20) # Get request to ask for page content
    page_content = BeautifulSoup(page_response.content, "html.parser")  # Ask Beautiful soup to parse for content

    for link in page_content.find_all("span", class_="flytitle-and-title__title", limit = 30):   # Finds all the spans with the class flytitle-and-title__title
        if link.text not in textContent:
            # print(link.text)  # Prints the title so we can verify correct operation 
            textContent.append(link.text)   # Appends the headline to our main array 
            tempHeadlineHolder.append(link.text) 

    print("Economist Done")
    time.sleep(5) # Creates a crawl delay of 5 seconds (which the Economist requires in their robots.txt file)

def CNNSearch():
    page_link = 'https://www.cnn.com/specials/last-50-stories'  # Page Url to point request where to crawl 
    page_response = requests.get(page_link, timeout=20) # Get request to ask for page content
    page_content = BeautifulSoup(page_response.content, "html.parser")  # Ask Beautiful soup to parse for content

    for link in page_content.find_all("span", class_="cd__headline-text", limit = 30):   # Finds all the spans with the class cd__headline-text
        if link.text not in textContent:
            # print(link.text)  # Prints the title so we can verify correct operation 
            textContent.append(link.text)   # Appends the headline to our main array 
            tempHeadlineHolder.append(link.text) 
    print("CNN Done")

def ReutersSearch():
    page_link = 'https://www.reuters.com/'  # Page Url to point request where to crawl 
    page_response = requests.get(page_link, timeout=20) # Get request to ask for page content
    page_content = BeautifulSoup(page_response.content, "html.parser")  # Ask Beautiful soup to parse for content

    for link in page_content.find_all("h3", class_="article-heading", limit = 30):   # Finds h3's with the class article-heading
        if link.text not in textContent:
            # print(link.text)  # Prints the title so we can verify correct operation 
            textContent.append(link.text)   # Appends the headline to our main array 
            tempHeadlineHolder.append(link.text) 
    print("Reuters Done")

def AlphaSearch():
    page_link = 'https://seekingalpha.com/market-news/all'  # Page Url to point request where to crawl 
    page_response = requests.get(page_link, timeout=20)     # Get request to ask for page content
    page_content = BeautifulSoup(page_response.content, "html.parser")  # Ask Beautiful soup to parse for content

    for link in page_content.find_all("div", class_="media-body", limit = 30):   # Finds divs with the class media-body
        if link.div.a.text not in textContent:  # Navigates down into the div to get the content in the link and checks if we have seen it before
            textContent.append(link.div.a.text) # Appends the title to our master so we can track if we have seen it before 
            tempHeadlineHolder.append(link.div.a.text)  # Appends the title to our temporary holder which has been cleared after the last unique title
    print("Seeking Alpha Done")

	
# Below is the logic processing area

def headlineAnalysis(headline):

    # Splits the headline so we can look for individual word matches
    words = headline.split()

    # A simple count to track if the headline contains our keywords
    matchScore = 0

    # Iterates over the words in the headline and looks for word matches 
    for individualWord in words: 
        if individualWord.lower() in tickers:
             print(individualWord.lower())


#################


economistSearch()   # Calls our main scraping method 
CNNSearch()
ReutersSearch()
AlphaSearch()   
print("Search Done at: " + str(datetime.datetime.now()))  # An optional printout to keep track of how many times the program has run 

# You can append text here to test the algorithm's response to certain cases 
#if cycleCount == 12: 
	#tempHeadlineHolder.append("Apple exceeds expectations in the latest quarter")

# A loop that cycles through our temporary headline holder
for headline in tempHeadlineHolder:
	print(headline)
	headlineAnalysis(headline)

tempHeadlineHolder = [] # Reset the headline holder after we have searched the content to avoid repeats 

# (Optional wait time that may be necessary for websites with a crawl delay or bot monitors) 
time.sleep(randint(0,5))  


















