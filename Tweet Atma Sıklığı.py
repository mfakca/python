import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime,timedelta






consumer_key = 'xxx'
consumer_secret = 'xxx'
access_token = 'xxx-xxx'
access_token_secret = 'xxx'



auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

mfa=api.me()

freq=[]
screen_name=[]
list__=[]



for friend in mfa.friends(count=10):
#name,id,url,verified(Doğrulanmış hesap),screen_name,location,statuses_count,followers_count,friends_count
    tweets = api.user_timeline(id = friend.screen_name,count=10)
    
    
    
    
    
    a=timeline_df(tweets).created_at.apply(lambda x: datetime.today()-x)
    plus_days=0
    for day in a:
        
        plus_days+=day.days
        
    plus_days=plus_days/10     
    list__.append(plus_days)
    if plus_days==0:
        
        if len(timeline_df(tweets).text)==0:
            frequncy=0
        else:frequncy=5
    elif plus_days<4:frequncy=5
    
    elif plus_days<10:frequncy=4
    
    elif plus_days<25:frequncy=3
        
    elif plus_days<45:frequncy=2
    
    elif plus_days<75:frequncy=1
        
    else:frequncy=0

    print(friend.screen_name,frequncy)
    screen_name.append(friend.screen_name)
    freq.append(frequncy)
df=pd.DataFrame({'screen_name':screen_name,
                 'frekans':freq})

plt.plot(df.screen_name[1:6],df.frekans[1:6])

plt.ylabel('Tweet atma sıklığı')
plt.xlabel('Kullanıcı adları')
plt.title('Twitter kullanıcılarının tweet atma sıklığının kategorize edilmiş tablosu')
plt.show()