#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


# ### Halaman 1

# In[2]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/?s={}".format(keyword)


# In[3]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[4]:


# Memasukkan hasil scraping ke dalam DataFrame
df1 = pd.DataFrame(data)
df1.head()


# In[5]:


# Mengganti nama kolom
df1.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df1.tail()


# ### Halaman 2

# In[6]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/2/?s={}".format(keyword)


# In[7]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[8]:


# Memasukkan hasil scraping ke dalam DataFrame
df2 = pd.DataFrame(data)
df2.head()


# In[9]:


# Mengganti nama kolom
df2.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df2.tail()


# ### Halaman 3

# In[10]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/3/?s={}".format(keyword)


# In[11]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[12]:


# Memasukkan hasil scraping ke dalam DataFrame
df3 = pd.DataFrame(data)
df3.head()


# In[13]:


# Mengganti nama kolom
df3.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df3.tail()


# ### Halaman 4

# In[14]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/4/?s={}".format(keyword)


# In[15]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[16]:


# Memasukkan hasil scraping ke dalam DataFrame
df4 = pd.DataFrame(data)
df4.head()


# In[17]:


# Mengganti nama kolom
df4.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df4.tail()


# ### Halaman 5

# In[18]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/5/?s={}".format(keyword)


# In[19]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[20]:


# Memasukkan hasil scraping ke dalam DataFrame
df5 = pd.DataFrame(data)
df5.head()


# In[21]:


# Mengganti nama kolom
df5.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df5.tail()


# ### Halaman 6

# In[22]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/6?s={}".format(keyword)


# In[23]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[24]:


# Memasukkan hasil scraping ke dalam DataFrame
df6 = pd.DataFrame(data)
df6.head()


# In[25]:


# Mengganti nama kolom
df6.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df6.tail()


# ### Halaman 7

# In[26]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/7/?s={}".format(keyword)


# In[27]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[28]:


# Memasukkan hasil scraping ke dalam DataFrame
df7 = pd.DataFrame(data)
df7.head()


# In[29]:


# Mengganti nama kolom
df7.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df7.tail()


# ### Halaman 8

# In[30]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/8/?s={}".format(keyword)


# In[31]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[32]:


# Memasukkan hasil scraping ke dalam DataFrame
df8 = pd.DataFrame(data)
df8.head()


# In[33]:


# Mengganti nama kolom
df8.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df8.tail()


# ### Halaman 9

# In[34]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/9/?s={}".format(keyword)


# In[35]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[36]:


# Memasukkan hasil scraping ke dalam DataFrame
df9 = pd.DataFrame(data)
df9.head()


# In[37]:


# Mengganti nama kolom
df9.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df9.tail()


# ### Halaman 10

# In[38]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/10/?s={}".format(keyword)


# In[39]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[40]:


# Memasukkan hasil scraping ke dalam DataFrame
df10 = pd.DataFrame(data)
df10.head()


# In[41]:


# Mengganti nama kolom
df10.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df10.tail()


# ### Halaman 11

# In[42]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/11/?s={}".format(keyword)


# In[43]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[44]:


# Memasukkan hasil scraping ke dalam DataFrame
df11 = pd.DataFrame(data)
df11.head()


# In[45]:


# Mengganti nama kolom
df11.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df11.tail()


# ### Halaman 12

# In[46]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/12/?s={}".format(keyword)


# In[47]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[48]:


# Memasukkan hasil scraping ke dalam DataFrame
df12 = pd.DataFrame(data)
df12.head()


# In[49]:


# Mengganti nama kolom
df12.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df12.tail()


# ### Halaman 13

# In[50]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/13/?s={}".format(keyword)


# In[51]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[52]:


# Memasukkan hasil scraping ke dalam DataFrame
df13 = pd.DataFrame(data)
df13.head()


# In[53]:


# Mengganti nama kolom
df13.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df13.tail()


# ### Halaman 14

# In[54]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/14/?s={}".format(keyword)


# In[55]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[56]:


# Memasukkan hasil scraping ke dalam DataFrame
df14 = pd.DataFrame(data)
df14.head()


# In[57]:


# Mengganti nama kolom
df14.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df14.tail()


# ### Halaman 15

# In[58]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/15/?s={}".format(keyword)


# In[59]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[60]:


# Memasukkan hasil scraping ke dalam DataFrame
df15 = pd.DataFrame(data)
df15.head()


# In[61]:


# Mengganti nama kolom
df15.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df15.tail()


# ### Halaman 16

# In[62]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/16/?s={}".format(keyword)


# In[63]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[64]:


# Memasukkan hasil scraping ke dalam DataFrame
df16 = pd.DataFrame(data)
df16.head()


# In[65]:


# Mengganti nama kolom
df16.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df16.tail()


# ### Halaman 17

# In[66]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/17/?s={}".format(keyword)


# In[67]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[68]:


# Memasukkan hasil scraping ke dalam DataFrame
df17 = pd.DataFrame(data)
df17.head()


# In[69]:


# Mengganti nama kolom
df17.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df17.tail()


# ### Halaman 18

# In[70]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/18/?s={}".format(keyword)


# In[71]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[72]:


# Memasukkan hasil scraping ke dalam DataFrame
df18 = pd.DataFrame(data)
df18.head()


# In[73]:


# Mengganti nama kolom
df18.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df18.tail()


# ### Halaman 19

# In[74]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/19/?s={}".format(keyword)


# In[75]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[76]:


# Memasukkan hasil scraping ke dalam DataFrame
df19 = pd.DataFrame(data)
df19.head()


# In[77]:


# Mengganti nama kolom
df19.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df19.tail()


# ### Halaman 20

# In[78]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/20/?s={}".format(keyword)


# In[79]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[80]:


# Memasukkan hasil scraping ke dalam DataFrame
df20 = pd.DataFrame(data)
df20.head()


# In[81]:


# Mengganti nama kolom
df20.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df20.tail()


# ### Halaman 21

# In[82]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/21/?s={}".format(keyword)


# In[83]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[84]:


# Memasukkan hasil scraping ke dalam DataFrame
df21 = pd.DataFrame(data)
df21.head()


# In[85]:


# Mengganti nama kolom
df21.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df21.tail()


# ### Halaman 22

# In[86]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/22/?s={}".format(keyword)


# In[87]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[88]:


# Memasukkan hasil scraping ke dalam DataFrame
df22 = pd.DataFrame(data)
df22.head()


# In[89]:


# Mengganti nama kolom
df22.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df22.tail()


# ### Halaman 23

# In[90]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/23/?s={}".format(keyword)


# In[91]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[92]:


# Memasukkan hasil scraping ke dalam DataFrame
df23 = pd.DataFrame(data)
df23.head()


# In[93]:


# Mengganti nama kolom
df23.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df23.tail()


# ### Halaman 24

# In[94]:


keyword = "ekonomi"
url = "https://turnbackhoax.id/page/24/?s={}".format(keyword)


# In[95]:


# Request URL Website
req = requests.get(url)

# Parsing HTML ke dalam BeautifulSoup
soup = bs(req.text, "html.parser")

# Memanggil judul artikel
article = soup.findAll("div", "mh-loop-content mh-clearfix")

# List kosong
data = []

for scraping in article:
    text = scraping.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = scraping.find("a", {"rel":"bookmark"})["href"]
    
    data.append([text, link]) # Memasukkan data scraping ke dalam list data


# In[96]:


# Memasukkan hasil scraping ke dalam DataFrame
df24 = pd.DataFrame(data)
df24.head()


# In[97]:


# Mengganti nama kolom
df24.rename(columns={0: "Text", 1:"URL"}, inplace=True)
df24.tail()


# ### Menggabungkan DataFrame "df" menjadi 1

# In[98]:


# Membuat DataFrame baru untuk menampung ketiga DataFrame hasil scraping
result = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21,
         df22, df23, df24]

# Menggabungkan DataFrame
df_final_result = pd.concat(result)

df_final_result.head()


# In[99]:


df_final_result.info()


# In[100]:


# Mengubah ke format .csv
df_final_result.to_csv("Data Scraping (turn back hoax) - Ekonomi.csv", index=True)

