import time 
from plyer import notification
print("Plyer is imported")
from topnews import topStories 

#initiate the list of newsitems
newsItems = topStories()

for newsitem in newsItems:
    notification.notify(
            title = newsitem["title"],
            message=newsitem["description"] ,
           
            # displaying time
            timeout=2)

if __name__=="__main__":
    for newsitem in newsItems:
        notification.notify(
                title = newsitem["title"],
                message=newsitem["description"] ,
                app_icon = '',
                # displaying time
                timeout=2)
        
            # waiting time
        time.sleep(7)