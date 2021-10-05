#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Library
from bs4 import BeautifulSoup
import pandas as pd
import requests


# ### Halaman 1

# In[2]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/?s={}".format(keyword)


# In[3]:


#Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML menjadi BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])
    #print(link)


# In[92]:


"""
"Untuk Looping Cuman Masih Gagal"
data = []

for page in range(1, 56):
    req = requests.get("https://turnbackhoax.id/?s=covid-19"+ str(page))
    soup = BeautifulSoup(req.text, "html.parser")
    
    content = [1, 56]
    for teks in content:
        column = soup.findAll("div", "mh-loop-content mh-clearfix"+ str(teks))
    
    for i in column:
        text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
        link = i.find("a", {"rel": "bookmark"})["href"]
data.append([text, link])
"""


# In[4]:


# Memasukkan hasil scrapping ke dalam DataFrame
df1 = pd.DataFrame(data)
df1.head()


# In[5]:


# Mengganti nama kolom pada DataFrame "df1"
df1.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df1.head()


# In[6]:


df1.info()


# ### Halaman 2

# In[7]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/2/?s={}".format(keyword)


# In[8]:


# Scrapping data per halaman secara otomatis
#for page in range (1, 10):

# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML menjadi BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])
    #print(link)


# In[9]:


# Memasukkan hasil scrapping ke dalam DataFrame
df2 = pd.DataFrame(data)
df2.head()


# In[10]:


# Mengganti nama kolom pada DataFrame "df2"
df2.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df2.head()


# In[11]:


df2.info()


# ### Halaman 3

# In[12]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/3/?s={}".format(keyword)


# In[13]:


# Scrapping data per halaman secara otomatis
#for page in range (1, 10):

# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML menjadi BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])
    #print(link)


# In[14]:


# Memasukkan hasil scrapping ke dalam DataFrame
df3 = pd.DataFrame(data)
df3.head()


# In[15]:


# Mengganti nama kolom pada DataFrame "df3"
df3.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df3.head()


# In[16]:


df3.info()


# ### Halaman 4

# In[17]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/4/?s={}".format(keyword)


# In[18]:


# Scrapping data per halaman secara otomatis
#for page in range (1, 10):

# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML menjadi BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])
    #print(link)


# In[19]:


# Memasukkan hasil scrapping ke dalam DataFrame
df4 = pd.DataFrame(data)
df4.head()


# In[20]:


# Mengganti nama kolom pada DataFrame "df4"
df4.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df4.head()


# In[21]:


df4.info()


# ### Halaman 5

# In[22]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/5/?s={}".format(keyword)


# In[23]:


# Scrapping data per halaman secara otomatis
#for page in range (1, 10):

# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML menjadi BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])
    #print(link)


# In[24]:


# Memasukkan hasil scrapping ke dalam DataFrame
df5 = pd.DataFrame(data)
df5.head()


# In[25]:


# Mengganti nama kolom pada DataFrame "df5"
df5.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df5.head()


# ### Halaman 6

# In[26]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/6/?s={}".format(keyword)


# In[27]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML menjadi BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])
    #print(link)


# In[28]:


# Memasukkan hasil scrapping ke dalam DataFrame
df6 = pd.DataFrame(data)
df6.head()


# In[29]:


# Mengganti nama kolom pada DataFrame "df6"
df6.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df6.head()


# ### Halaman 7 

# In[30]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/7/?s={}".format(keyword)


# In[31]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML menjadi BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])
    #print(link)


# In[32]:


# Memasukkan hasil scrapping ke dalam DataFrame
df7 = pd.DataFrame(data)
df7.head()


# In[33]:


# Mengganti nama kolom pada DataFrame "df7"
df7.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df7.head()


# In[34]:


df7.info()


# ### Halaman 8 

# In[35]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/8/?s={}".format(keyword)


# In[36]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML menjadi BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[37]:


# Memasukkan hasil scrapping ke dalam DataFrame
df8 = pd.DataFrame(data)
df8.head()


# In[38]:


# Mengganti nama kolom pada DataFrame "df8"
df8.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df8.head()


# In[39]:


df8.tail()


# ### Halaman 9 

# In[40]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/9/?s={}".format(keyword)


# In[41]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML menjadi BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[42]:


# Memasukkan hasil scrapping ke dalam DataFrame
df9 = pd.DataFrame(data)
df9.head()


# In[43]:


# Mengganti nama kolom pada DataFrame "df9"
df9.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df9.head()


# ### Halaman 10 

# In[44]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/10/?s={}".format(keyword)


# In[45]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[46]:


# Memasukkan hasil scrapping ke dalam DataFrame
df10 = pd.DataFrame(data)
df10.head()


# In[47]:


# Mengganti nama kolom pada DataFrame "df10"
df10.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df10.tail()


# ### Halaman 11 

# In[48]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/11/?s={}".format(keyword)


# In[49]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[50]:


# Memasukkan hasil scrapping ke dalam DataFrame
df11 = pd.DataFrame(data)
df11.tail()


# In[51]:


# Mengganti nama kolom pada DataFrame "df11"
df11.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df11.head()


# ### Halaman 12

# In[52]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/12/?s={}".format(keyword)


# In[53]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[149]:


"""
"Untuk Looping Cuman Masih Gagal"
data = []
#count_page = 0

for page in range(1, 56):
    #count_page += 1
    #print("Halaman Scrapping: ", count_page)
    
    req = requests.get(url + str(page))
    soup = BeautifulSoup(req.text, "html.parser")
    column = soup.findAll("div", "mh-loop-content mh-clearfix"+ str(teks))
    
    for i in column:
        text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
        link = i.find("a", {"rel": "bookmark"})["href"]
        data.append([text, link])
"""


# In[54]:


# Memasukkan hasil scrapping ke dalam DataFrame
df12 = pd.DataFrame(data)
df12.tail()


# In[55]:


# Mengganti nama kolom pada DataFrame "df12"
df12.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df12.head()


# ### Halaman 13

# In[56]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/13/?s={}".format(keyword)


# In[57]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[58]:


# Memasukkan hasil scrapping ke dalam DataFrame
df13 = pd.DataFrame(data)
df13.tail()


# In[59]:


# Mengganti nama kolom pada DataFrame "df13"
df13.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df13.head()


# ### Halaman 14

# In[60]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/14/?s={}".format(keyword)


# In[61]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[62]:


# Memasukkan hasil scrapping ke dalam DataFrame
df14 = pd.DataFrame(data)
df14.tail()


# In[63]:


# Mengganti nama kolom pada DataFrame "df14"
df14.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df14.head()


# ### Halaman 15

# In[64]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/15/?s={}".format(keyword)


# In[65]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[66]:


# Memasukkan hasil scrapping ke dalam DataFrame
df15 = pd.DataFrame(data)
df15.tail()


# In[67]:


# Mengganti nama kolom pada DataFrame "df15"
df15.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df15.head()


# ### Halaman 16

# In[68]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/16/?s={}".format(keyword)


# In[69]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[70]:


# Memasukkan hasil scrapping ke dalam DataFrame
df16 = pd.DataFrame(data)
df16.tail()


# In[71]:


# Mengganti nama kolom pada DataFrame "df16"
df16.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df16.head()


# ### Halaman 17

# In[72]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/17/?s={}".format(keyword)


# In[73]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[74]:


# Memasukkan hasil scrapping ke dalam DataFrame
df17 = pd.DataFrame(data)
df17.tail()


# In[75]:


# Mengganti nama kolom pada DataFrame "df17"
df17.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df17.head()


# ### Halaman 18

# In[76]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/18/?s={}".format(keyword)


# In[77]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[78]:


# Memasukkan hasil scrapping ke dalam DataFrame
df18 = pd.DataFrame(data)
df18.tail()


# In[79]:


# Mengganti nama kolom pada DataFrame "df18"
df18.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df18.head()


# ### Halaman 19

# In[80]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/19/?s={}".format(keyword)


# In[81]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[82]:


# Memasukkan hasil scrapping ke dalam DataFrame
df19 = pd.DataFrame(data)
df19.tail()


# In[83]:


# Mengganti nama kolom pada DataFrame "df19"
df19.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df19.head()


# ### Halaman 20 

# In[84]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/20/?s={}".format(keyword)


# In[85]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[86]:


# Memasukkan hasil scrapping ke dalam DataFrame
df20 = pd.DataFrame(data)
df20.tail()


# In[87]:


# Mengganti nama kolom pada DataFrame "df20"
df20.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df20.head()


# ### Halaman 21

# In[88]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/21/?s={}".format(keyword)


# In[89]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[90]:


# Memasukkan hasil scrapping ke dalam DataFrame
df21 = pd.DataFrame(data)
df21.tail()


# In[91]:


# Mengganti nama kolom pada DataFrame "df21"
df21.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df21.head()


# ### Halaman 22

# In[92]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/22/?s={}".format(keyword)


# In[93]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[94]:


# Memasukkan hasil scrapping ke dalam DataFrame
df22 = pd.DataFrame(data)
df22.tail()


# In[95]:


# Mengganti nama kolom pada DataFrame "df22"
df22.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df22.head()


# ### Halaman 23

# In[96]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/23/?s={}".format(keyword)


# In[97]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[98]:


# Memasukkan hasil scrapping ke dalam DataFrame
df23 = pd.DataFrame(data)
df23.tail()


# In[99]:


# Mengganti nama kolom pada DataFrame "df23"
df23.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df23.head()


# ### Halaman 24

# In[100]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/24/?s={}".format(keyword)


# In[101]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[102]:


# Memasukkan hasil scrapping ke dalam DataFrame
df24 = pd.DataFrame(data)
df24.tail()


# In[103]:


# Mengganti nama kolom pada DataFrame "df24"
df24.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df24.head()


# ### Halaman 25

# In[104]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/25/?s={}".format(keyword)


# In[105]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[106]:


# Memasukkan hasil scrapping ke dalam DataFrame
df25 = pd.DataFrame(data)
df25.tail()


# In[107]:


# Mengganti nama kolom pada DataFrame "df25"
df25.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df25.head()


# ### Halaman 26

# In[108]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/26/?s={}".format(keyword)


# In[109]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[110]:


# Memasukkan hasil scrapping ke dalam DataFrame
df26 = pd.DataFrame(data)
df26.head()


# In[111]:


# Mengganti nama kolom pada DataFrame "df26"
df26.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df26.tail()


# ### Halaman 27 

# In[112]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/27/?s={}".format(keyword)


# In[113]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[114]:


# Memasukkan hasil scrapping ke dalam DataFrame
df27 = pd.DataFrame(data)
df27.head()


# In[115]:


# Mengganti nama kolom pada DataFrame "df27"
df27.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df27.tail()


# ### Halaman 28

# In[116]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/28/?s={}".format(keyword)


# In[117]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[118]:


# Memasukkan hasil scrapping ke dalam DataFrame
df28 = pd.DataFrame(data)
df28.head()


# In[119]:


# Mengganti nama kolom pada DataFrame "df28"
df28.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df28.tail()


# ### Halaman 29

# In[120]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/29/?s={}".format(keyword)


# In[121]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[122]:


# Memasukkan hasil scrapping ke dalam DataFrame
df29 = pd.DataFrame(data)
df29.head()


# In[123]:


# Mengganti nama kolom pada DataFrame "df29"
df29.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df29.tail()


# ### Halaman 30 

# In[124]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/30/?s={}".format(keyword)


# In[125]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[126]:


# Memasukkan hasil scrapping ke dalam DataFrame
df30 = pd.DataFrame(data)
df30.head()


# In[127]:


# Mengganti nama kolom pada DataFrame "df30"
df30.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df30.tail()


# ### Halaman 31

# In[130]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/31/?s={}".format(keyword)


# In[131]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[132]:


# Memasukkan hasil scrapping ke dalam DataFrame
df31 = pd.DataFrame(data)
df31.head()


# In[133]:


# Mengganti nama kolom pada DataFrame "df31"
df31.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df31.tail()


# ### Halaman 32

# In[134]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/32/?s={}".format(keyword)


# In[135]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[136]:


# Memasukkan hasil scrapping ke dalam DataFrame
df32 = pd.DataFrame(data)
df32.head()


# In[137]:


# Mengganti nama kolom pada DataFrame "df32"
df32.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df32.tail()


# ### Halaman 33

# In[138]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/33/?s={}".format(keyword)


# In[139]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[140]:


# Memasukkan hasil scrapping ke dalam DataFrame
df33 = pd.DataFrame(data)
df33.head()


# In[141]:


# Mengganti nama kolom pada DataFrame "df33"
df33.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df33.tail()


# ### Halaman 34

# In[142]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/34/?s={}".format(keyword)


# In[143]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[144]:


# Memasukkan hasil scrapping ke dalam DataFrame
df34 = pd.DataFrame(data)
df34.head()


# In[145]:


# Mengganti nama kolom pada DataFrame "df34"
df34.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df34.tail()


# ### Halaman 35

# In[146]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/35/?s={}".format(keyword)


# In[147]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[148]:


# Memasukkan hasil scrapping ke dalam DataFrame
df35 = pd.DataFrame(data)
df35.head()


# In[149]:


# Mengganti nama kolom pada DataFrame "df35"
df35.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df35.tail()


# ### Halaman 36

# In[150]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/36/?s={}".format(keyword)


# In[151]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[152]:


# Memasukkan hasil scrapping ke dalam DataFrame
df36 = pd.DataFrame(data)
df36.head()


# In[153]:


# Mengganti nama kolom pada DataFrame "df36"
df36.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df36.tail()


# ### Halaman 37

# In[154]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/37/?s={}".format(keyword)


# In[155]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[156]:


# Memasukkan hasil scrapping ke dalam DataFrame
df37 = pd.DataFrame(data)
df37.head()


# In[157]:


# Mengganti nama kolom pada DataFrame "df37"
df37.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df37.tail()


# ### Halaman 38

# In[158]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/38/?s={}".format(keyword)


# In[159]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[160]:


# Memasukkan hasil scrapping ke dalam DataFrame
df38 = pd.DataFrame(data)
df38.head()


# In[161]:


# Mengganti nama kolom pada DataFrame "df38"
df38.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df38.tail()


# ### Halaman 39

# In[162]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/39/?s={}".format(keyword)


# In[163]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[164]:


# Memasukkan hasil scrapping ke dalam DataFrame
df39 = pd.DataFrame(data)
df39.head()


# In[165]:


# Mengganti nama kolom pada DataFrame "df39"
df39.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df39.tail()


# ### Halaman 40

# In[166]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/40/?s={}".format(keyword)


# In[167]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[168]:


# Memasukkan hasil scrapping ke dalam DataFrame
df40 = pd.DataFrame(data)
df40.head()


# In[169]:


# Mengganti nama kolom pada DataFrame "df40"
df40.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df40.tail()


# ### Halaman 41

# In[170]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/41/?s={}".format(keyword)


# In[171]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[172]:


# Memasukkan hasil scrapping ke dalam DataFrame
df41 = pd.DataFrame(data)
df41.head()


# In[173]:


# Mengganti nama kolom pada DataFrame "df41"
df41.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df41.tail()


# ### Halaman 42

# In[174]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/42/?s={}".format(keyword)


# In[175]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[176]:


# Memasukkan hasil scrapping ke dalam DataFrame
df42 = pd.DataFrame(data)
df42.head()


# In[177]:


# Mengganti nama kolom pada DataFrame "df42"
df42.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df42.tail()


# ### Halaman 43

# In[178]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/43/?s={}".format(keyword)


# In[179]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[180]:


# Memasukkan hasil scrapping ke dalam DataFrame
df43 = pd.DataFrame(data)
df43.head()


# In[181]:


# Mengganti nama kolom pada DataFrame "df43"
df43.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df43.tail()


# ### Halaman 44

# In[182]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/44/?s={}".format(keyword)


# In[183]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[184]:


# Memasukkan hasil scrapping ke dalam DataFrame
df44 = pd.DataFrame(data)
df44.head()


# In[185]:


# Mengganti nama kolom pada DataFrame "df44"
df44.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df44.tail()


# ### Halaman 45

# In[188]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/45/?s={}".format(keyword)


# In[189]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[190]:


# Memasukkan hasil scrapping ke dalam DataFrame
df45 = pd.DataFrame(data)
df45.head()


# In[191]:


# Mengganti nama kolom pada DataFrame "df45"
df45.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df45.tail()


# ### Halaman 46

# In[192]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/46/?s={}".format(keyword)


# In[193]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[194]:


# Memasukkan hasil scrapping ke dalam DataFrame
df46 = pd.DataFrame(data)
df46.head()


# In[195]:


# Mengganti nama kolom pada DataFrame "df46"
df46.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df46.tail()


# ### Halaman 47

# In[196]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/47/?s={}".format(keyword)


# In[197]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[198]:


# Memasukkan hasil scrapping ke dalam DataFrame
df47 = pd.DataFrame(data)
df47.tail()


# In[199]:


# Mengganti nama kolom pada DataFrame "df47"
df47.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df47.head()


# ### Halaman 48

# In[200]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/48/?s={}".format(keyword)


# In[201]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[202]:


# Memasukkan hasil scrapping ke dalam DataFrame
df48 = pd.DataFrame(data)
df48.tail()


# In[203]:


# Mengganti nama kolom pada DataFrame "df48"
df48.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df48.head()


# ### Halaman 49

# In[204]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/49/?s={}".format(keyword)


# In[205]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[206]:


# Memasukkan hasil scrapping ke dalam DataFrame
df49 = pd.DataFrame(data)
df49.tail()


# In[207]:


# Mengganti nama kolom pada DataFrame "df49"
df49.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df49.head()


# ### Halaman 50

# In[210]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/50/?s={}".format(keyword)


# In[211]:


# Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML dengan BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

# Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = [] # Untuk menampung hasil dari scrapping data

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append([text, link])


# In[212]:


# Memasukkan hasil scrapping ke dalam DataFrame
df50 = pd.DataFrame(data)
df50.tail()


# In[213]:


# Mengganti nama kolom pada DataFrame "df50"
df50.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df50.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:


# Scrapping data per halaman secara otomatis
#for page in range (1, 10):

#Request URL
req = requests.get(url)

# Merubah format dari yang semula HTML menjadi BeautifulSoup 
soup = BeautifulSoup(req.text, "html.parser")

#Memanggil seluruh artikel yang berada di halaman luar
column = soup.findAll("div", "mh-loop-content mh-clearfix")

data = []

for i in column:
    text = i.find("h3", "entry-title mh-loop-title").text.strip().split("\n")
    link = i.find("a", {"rel": "bookmark"})["href"]
    data.append(text)
    #print(link)


# In[1]:


import requests
from bs4 import BeautifulSoup

URL = "https://turnbackhoax.id/?s=PPKM"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

