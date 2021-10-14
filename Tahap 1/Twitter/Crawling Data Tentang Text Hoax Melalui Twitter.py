#!/usr/bin/env python
# coding: utf-8

# In[19]:


# import library
import pandas as pd
import tweepy


# In[20]:


# Memanggil api key yang ada di twitter developers
api_key = "KUNFoSzybeAeJx4vfXnHLakR6"
api_secret_key = "QtPIXWmtCFUPXkdqIfRrMW9gTzuezZ4bpSEpuZkWGviFXenDWL"


# In[21]:


# Memanggil kode token yang ada di twitter developers
access_token = "1444155092861521933-u1OcQuhzpRVNMEsYxT5pe0KZqZlyhL"
access_secret_token = "3tBct3p0EYD7ssPROn0hscyRWAOs2GWq9Yugcfku5V28A"


# In[22]:


# Memanggil api dan akses token
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_secret_token)


# In[23]:


api_auth = tweepy.API(auth, wait_on_rate_limit = True)


# In[24]:


search_engine = "vaksin -filter:retweets"


# In[25]:


# Mengambil data tweet dan tipe sumber dari mana tweet itu berasal
teks = []
source =[]

for tweet in tweepy.Cursor(api_auth.search, q=search_engine, lang="id", tweet_mode="extended").items(1000):
    teks.append(tweet.full_text) # Data Tweet
    source.append(tweet.source) # Type Source
    print ("text : ", tweet.full_text, "source :", tweet.source)


# In[26]:


# Memasukkan isi crawling ke dalam DataFrame
data = pd.DataFrame({"Tweet": teks, "Source Type": source})
data.head()


# In[27]:


#Memanggil link url yang terdapat di kolom Tweet
data["Source URL"] = data["Tweet"].str.split().str[-1]
data.head()


# In[28]:


data.tail(10)


# In[29]:


data.info()


# In[30]:


# Mengubah dataframe menjadi file .csv
data.to_csv("data crawling.csv", index=False)

