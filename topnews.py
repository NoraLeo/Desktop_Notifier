import requests 
import xml.etree.ElementTree as ET 

RSS_FEED_URL= "https://techcrunch.com/feed/"

def loadRSS():
    response = requests.get(RSS_FEED_URL)

    return response.content

def parseXML(rss):
    root = ET.fromstring(rss)

    newsItems = []
    
    for item in root.findall("./channel/item"):
        news = {}
        for child in item: 
  
            # special checking for namespace object content:media 
            if child.tag == '{http://search.yahoo.com/mrss/}content': 
                news['media'] = child.attrib['url'] 
            else: 
                news[child.tag] = child.text.encode('utf8') 
        newsItems.append(news) 
    return newsItems 
def topStories(): 
    ''' 
    main function to generate and return news items 
    '''
    # load rss feed 
    rss = loadRSS() 
  
    # parse XML 
    newsitems = parseXML(rss) 
    return newsitems 
