import time 
from notifypy import Notify
print("notify-py is imported")
from topnews import topStories 

#initiate the list of newsitems
newsItems = topStories()

for newsitem in newsItems:
    notification = Notify()
    notification.title = newsitem["title"]
    notification.message=newsitem["description"]
    # displaying time
    notification.timeout=2

    #send the notification
    notification.send()

if __name__=="__main__":
    for newsitem in newsItems:
        notification = Notify()
        notification.title = newsitem["title"]
        notification.message=newsitem["description"]
        notification.icon = ''
        # displaying time
        notification.timeout=2

        #send the notification
        notification.send()
        
            # waiting time
        time.sleep(7)