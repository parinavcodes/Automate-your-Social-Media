import facebook
import fb
import json
import instapy_cli
from datetime import datetime, timedelta, date
from threading import Timer
#import pynew2

def hello_world():
    graph=facebook.GraphAPI(access_token="")
    msg=graph.put_object(parent_object='me',connection_name='feed',message='test message')
    print(msg)
    
def kl():
    print("hi")

if __name__=="__main__":
    x=datetime.today()
    y = x.replace(day=x.day, hour=3, minute=45, second=45, microsecond=0)
    # + timedelta(days=1)
    delta_t=y-x

    secs=delta_t.total_seconds()
    print(date.today())
    #hello_world()

    t = Timer(secs, kl)
    t.start()