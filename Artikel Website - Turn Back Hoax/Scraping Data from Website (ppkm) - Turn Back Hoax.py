#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import library
import pandas as pd
import requests
from bs4 import BeautifulSoup


# ### Halaman 1

# In[2]:


keyword = "ppkm"
url = "https://turnbackhoax.id/?s={}".format(keyword)


# In[3]:


# Request URL
req = requests.get(url)


soup = BeautifulSoup(req.text, "html.parser")

# Memanggil judul artikel paling terluar
content = soup.findAll("div", "mh-loop-content mh-clearfix")

# Menampung hasil dari scraping data
data = []

for scraping in content:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link])


# In[4]:


df1 = pd.DataFrame(data)
df1.head()


# In[5]:


# Mengganti nama kolom
df1.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df1.tail()


# ### Halaman 2

# In[6]:


keyword = "ppkm"
url = "https://turnbackhoax.id/page/2/?s={}".format(keyword)


# In[7]:


# Request URL
req = requests.get(url)


soup = BeautifulSoup(req.text, "html.parser")

# Memanggil judul artikel paling terluar
content = soup.findAll("div", "mh-loop-content mh-clearfix")

# Membuat list kosong untuk menampung hasil dari scraping data
data = []

for scraping in content:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    # Memasukkan hasil scraping ke dalam list kosong
    data.append([text, link])


# In[8]:


df2 = pd.DataFrame(data)
df2.head()


# In[9]:


# Mengganti nama kolom
df2.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df2.info()


# ### Halaman 3

# In[10]:


keyword = "ppkm"
url = "https://turnbackhoax.id/page/3/?s={}".format(keyword)


# In[11]:


# Request URL
req = requests.get(url)


soup = BeautifulSoup(req.text, "html.parser")

# Memanggil judul artikel paling terluar
content = soup.findAll("div", "mh-loop-content mh-clearfix")

# Membuat list kosong untuk menampung hasil dari scraping data
data = []

for scraping in content:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    # Memasukkan hasil scraping ke dalam list kosong
    data.append([text, link])


# In[12]:


df3 = pd.DataFrame(data)
df3.head()


# In[13]:


# Mengganti nama kolom
df3.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df3.head()


# ### Menggabungkan Ketiga DataFrame Menjadi 1

# In[14]:


# Membuat DataFrame baru untuk menampung ketiga DataFrame hasil scraping
data_scrap = [df1, df2, df3]

# Menggabungkan DataFrame
data_scraping = pd.concat(data_scrap)

data_scraping.head()


# In[15]:


data_scraping.info()


# In[16]:


# Mengubah susunan DataFrame menjadi .csv
data_scraping.to_csv("data scraping (turn back hoax) - PPKM.csv", index=False)

