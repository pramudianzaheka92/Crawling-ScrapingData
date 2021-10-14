#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Import Library
import pandas as pd
import tweepy


# In[36]:


# Memanggil api key yang ada di twitter developers
api_key = "7POVm0zEIwIXZC5ADFHV1vQJz"
api_secret_key = "vAeKOrshM14Qkl35YBbNg2l2bHbz8hYYrUDM04Hv0TWRYcjgtm"


# In[37]:


# Memanggil kode token yang ada di twitter developers
access_token = "1444155092861521933-nfkhX6WlXjUidEOazIRRK5NFLtKb6l"
access_secret_token = "pe3RNZzvGtzyA0b8Dj4R0fDjbsNqFpETdK9fW9TaxmoCE"


# In[38]:


# Memanggil api dan akses token
authentication = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_secret_token)


# In[39]:


api_authentication = tweepy.API(authentication, wait_on_rate_limit = True)


# In[40]:


keyword = "ekonomi -filter:retweets"


# In[41]:


# Mengambil data tweet dan username
teks = []
username =[]

for tweet in tweepy.Cursor(api_authentication.search, q=keyword, 
                           lang="id", tweet_mode="extended").items(1500):
    
    teks.append(tweet.full_text) # Data Tweet
    username.append(tweet.user.name) # Username
    print ("text : ", tweet.full_text, "username :", tweet.user.name)


# In[42]:


data_twitter = pd.DataFrame({"Username":username, "Isi Tweet":teks})
data_twitter.head()


# In[43]:


#Memanggil link url yang terdapat di kolom Tweet
data_twitter["URL"] = data_twitter["Isi Tweet"].str.split().str[-1]
data_twitter.tail()


# In[44]:


data_twitter.info()


# In[45]:


# Format .csv
data_twitter.to_csv("Data Twitter Tentang Ekonomi.csv", index=False)

