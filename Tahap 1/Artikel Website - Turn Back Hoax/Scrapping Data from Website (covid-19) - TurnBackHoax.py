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


# In[4]:


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


# In[5]:


# Memasukkan hasil scrapping ke dalam DataFrame
df1 = pd.DataFrame(data)
df1.head()


# In[6]:


# Mengganti nama kolom pada DataFrame "df1"
df1.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df1.head()


# In[7]:


df1.info()


# ### Halaman 2

# In[8]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/2/?s={}".format(keyword)


# In[9]:


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


# In[10]:


# Memasukkan hasil scrapping ke dalam DataFrame
df2 = pd.DataFrame(data)
df2.head()


# In[11]:


# Mengganti nama kolom pada DataFrame "df2"
df2.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df2.head()


# In[12]:


df2.info()


# ### Halaman 3

# In[13]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/3/?s={}".format(keyword)


# In[14]:


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


# In[15]:


# Memasukkan hasil scrapping ke dalam DataFrame
df3 = pd.DataFrame(data)
df3.head()


# In[16]:


# Mengganti nama kolom pada DataFrame "df3"
df3.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df3.head()


# In[17]:


df3.info()


# ### Halaman 4

# In[18]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/4/?s={}".format(keyword)


# In[19]:


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


# In[20]:


# Memasukkan hasil scrapping ke dalam DataFrame
df4 = pd.DataFrame(data)
df4.head()


# In[21]:


# Mengganti nama kolom pada DataFrame "df4"
df4.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df4.head()


# In[22]:


df4.info()


# ### Halaman 5

# In[23]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/5/?s={}".format(keyword)


# In[24]:


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


# In[25]:


# Memasukkan hasil scrapping ke dalam DataFrame
df5 = pd.DataFrame(data)
df5.head()


# In[26]:


# Mengganti nama kolom pada DataFrame "df5"
df5.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df5.head()


# ### Halaman 6

# In[27]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/6/?s={}".format(keyword)


# In[28]:


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


# In[29]:


# Memasukkan hasil scrapping ke dalam DataFrame
df6 = pd.DataFrame(data)
df6.head()


# In[30]:


# Mengganti nama kolom pada DataFrame "df6"
df6.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df6.head()


# ### Halaman 7 

# In[31]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/7/?s={}".format(keyword)


# In[32]:


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


# In[33]:


# Memasukkan hasil scrapping ke dalam DataFrame
df7 = pd.DataFrame(data)
df7.head()


# In[34]:


# Mengganti nama kolom pada DataFrame "df7"
df7.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df7.head()


# In[35]:


df7.info()


# ### Halaman 8 

# In[36]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/8/?s={}".format(keyword)


# In[37]:


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


# In[38]:


# Memasukkan hasil scrapping ke dalam DataFrame
df8 = pd.DataFrame(data)
df8.head()


# In[39]:


# Mengganti nama kolom pada DataFrame "df8"
df8.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df8.head()


# In[40]:


df8.tail()


# ### Halaman 9 

# In[41]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/9/?s={}".format(keyword)


# In[42]:


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


# In[43]:


# Memasukkan hasil scrapping ke dalam DataFrame
df9 = pd.DataFrame(data)
df9.head()


# In[44]:


# Mengganti nama kolom pada DataFrame "df9"
df9.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df9.head()


# ### Halaman 10 

# In[45]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/10/?s={}".format(keyword)


# In[46]:


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


# In[47]:


# Memasukkan hasil scrapping ke dalam DataFrame
df10 = pd.DataFrame(data)
df10.head()


# In[48]:


# Mengganti nama kolom pada DataFrame "df10"
df10.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df10.tail()


# ### Halaman 11 

# In[49]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/11/?s={}".format(keyword)


# In[50]:


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


# In[51]:


# Memasukkan hasil scrapping ke dalam DataFrame
df11 = pd.DataFrame(data)
df11.tail()


# In[52]:


# Mengganti nama kolom pada DataFrame "df11"
df11.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df11.head()


# ### Halaman 12

# In[53]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/12/?s={}".format(keyword)


# In[54]:


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


# In[55]:


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


# In[56]:


# Memasukkan hasil scrapping ke dalam DataFrame
df12 = pd.DataFrame(data)
df12.tail()


# In[57]:


# Mengganti nama kolom pada DataFrame "df12"
df12.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df12.head()


# ### Halaman 13

# In[58]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/13/?s={}".format(keyword)


# In[59]:


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


# In[60]:


# Memasukkan hasil scrapping ke dalam DataFrame
df13 = pd.DataFrame(data)
df13.tail()


# In[61]:


# Mengganti nama kolom pada DataFrame "df13"
df13.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df13.head()


# ### Halaman 14

# In[62]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/14/?s={}".format(keyword)


# In[63]:


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


# In[64]:


# Memasukkan hasil scrapping ke dalam DataFrame
df14 = pd.DataFrame(data)
df14.tail()


# In[65]:


# Mengganti nama kolom pada DataFrame "df14"
df14.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df14.head()


# ### Halaman 15

# In[66]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/15/?s={}".format(keyword)


# In[67]:


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


# In[68]:


# Memasukkan hasil scrapping ke dalam DataFrame
df15 = pd.DataFrame(data)
df15.tail()


# In[69]:


# Mengganti nama kolom pada DataFrame "df15"
df15.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df15.head()


# ### Halaman 16

# In[70]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/16/?s={}".format(keyword)


# In[71]:


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


# In[72]:


# Memasukkan hasil scrapping ke dalam DataFrame
df16 = pd.DataFrame(data)
df16.tail()


# In[73]:


# Mengganti nama kolom pada DataFrame "df16"
df16.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df16.head()


# ### Halaman 17

# In[74]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/17/?s={}".format(keyword)


# In[75]:


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


# In[76]:


# Memasukkan hasil scrapping ke dalam DataFrame
df17 = pd.DataFrame(data)
df17.tail()


# In[77]:


# Mengganti nama kolom pada DataFrame "df17"
df17.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df17.head()


# ### Halaman 18

# In[78]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/18/?s={}".format(keyword)


# In[79]:


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


# In[80]:


# Memasukkan hasil scrapping ke dalam DataFrame
df18 = pd.DataFrame(data)
df18.tail()


# In[81]:


# Mengganti nama kolom pada DataFrame "df18"
df18.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df18.head()


# ### Halaman 19

# In[82]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/19/?s={}".format(keyword)


# In[83]:


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


# In[84]:


# Memasukkan hasil scrapping ke dalam DataFrame
df19 = pd.DataFrame(data)
df19.tail()


# In[85]:


# Mengganti nama kolom pada DataFrame "df19"
df19.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df19.head()


# ### Halaman 20 

# In[86]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/20/?s={}".format(keyword)


# In[87]:


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


# In[88]:


# Memasukkan hasil scrapping ke dalam DataFrame
df20 = pd.DataFrame(data)
df20.tail()


# In[89]:


# Mengganti nama kolom pada DataFrame "df20"
df20.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df20.head()


# ### Halaman 21

# In[90]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/21/?s={}".format(keyword)


# In[91]:


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


# In[92]:


# Memasukkan hasil scrapping ke dalam DataFrame
df21 = pd.DataFrame(data)
df21.tail()


# In[93]:


# Mengganti nama kolom pada DataFrame "df21"
df21.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df21.head()


# ### Halaman 22

# In[94]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/22/?s={}".format(keyword)


# In[95]:


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


# In[96]:


# Memasukkan hasil scrapping ke dalam DataFrame
df22 = pd.DataFrame(data)
df22.tail()


# In[97]:


# Mengganti nama kolom pada DataFrame "df22"
df22.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df22.head()


# ### Halaman 23

# In[98]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/23/?s={}".format(keyword)


# In[99]:


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


# In[100]:


# Memasukkan hasil scrapping ke dalam DataFrame
df23 = pd.DataFrame(data)
df23.tail()


# In[101]:


# Mengganti nama kolom pada DataFrame "df23"
df23.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df23.head()


# ### Halaman 24

# In[102]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/24/?s={}".format(keyword)


# In[103]:


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


# In[104]:


# Memasukkan hasil scrapping ke dalam DataFrame
df24 = pd.DataFrame(data)
df24.tail()


# In[105]:


# Mengganti nama kolom pada DataFrame "df24"
df24.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df24.head()


# ### Halaman 25

# In[106]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/25/?s={}".format(keyword)


# In[107]:


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


# In[108]:


# Memasukkan hasil scrapping ke dalam DataFrame
df25 = pd.DataFrame(data)
df25.tail()


# In[109]:


# Mengganti nama kolom pada DataFrame "df25"
df25.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df25.head()


# ### Halaman 26

# In[110]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/26/?s={}".format(keyword)


# In[111]:


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


# In[112]:


# Memasukkan hasil scrapping ke dalam DataFrame
df26 = pd.DataFrame(data)
df26.head()


# In[113]:


# Mengganti nama kolom pada DataFrame "df26"
df26.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df26.tail()


# ### Halaman 27 

# In[114]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/27/?s={}".format(keyword)


# In[115]:


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


# In[116]:


# Memasukkan hasil scrapping ke dalam DataFrame
df27 = pd.DataFrame(data)
df27.head()


# In[117]:


# Mengganti nama kolom pada DataFrame "df27"
df27.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df27.tail()


# ### Halaman 28

# In[118]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/28/?s={}".format(keyword)


# In[119]:


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


# In[120]:


# Memasukkan hasil scrapping ke dalam DataFrame
df28 = pd.DataFrame(data)
df28.head()


# In[121]:


# Mengganti nama kolom pada DataFrame "df28"
df28.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df28.tail()


# ### Halaman 29

# In[122]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/29/?s={}".format(keyword)


# In[123]:


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


# In[124]:


# Memasukkan hasil scrapping ke dalam DataFrame
df29 = pd.DataFrame(data)
df29.head()


# In[125]:


# Mengganti nama kolom pada DataFrame "df29"
df29.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df29.tail()


# ### Halaman 30 

# In[126]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/30/?s={}".format(keyword)


# In[127]:


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


# In[128]:


# Memasukkan hasil scrapping ke dalam DataFrame
df30 = pd.DataFrame(data)
df30.head()


# In[129]:


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

# In[186]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/45/?s={}".format(keyword)


# In[187]:


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


# In[188]:


# Memasukkan hasil scrapping ke dalam DataFrame
df45 = pd.DataFrame(data)
df45.head()


# In[189]:


# Mengganti nama kolom pada DataFrame "df45"
df45.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df45.tail()


# ### Halaman 46

# In[190]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/46/?s={}".format(keyword)


# In[191]:


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


# In[192]:


# Memasukkan hasil scrapping ke dalam DataFrame
df46 = pd.DataFrame(data)
df46.head()


# In[193]:


# Mengganti nama kolom pada DataFrame "df46"
df46.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df46.tail()


# ### Halaman 47

# In[194]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/47/?s={}".format(keyword)


# In[195]:


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


# In[196]:


# Memasukkan hasil scrapping ke dalam DataFrame
df47 = pd.DataFrame(data)
df47.tail()


# In[197]:


# Mengganti nama kolom pada DataFrame "df47"
df47.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df47.head()


# ### Halaman 48

# In[198]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/48/?s={}".format(keyword)


# In[199]:


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


# In[200]:


# Memasukkan hasil scrapping ke dalam DataFrame
df48 = pd.DataFrame(data)
df48.tail()


# In[201]:


# Mengganti nama kolom pada DataFrame "df48"
df48.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df48.head()


# ### Halaman 49

# In[202]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/49/?s={}".format(keyword)


# In[203]:


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


# In[204]:


# Memasukkan hasil scrapping ke dalam DataFrame
df49 = pd.DataFrame(data)
df49.tail()


# In[205]:


# Mengganti nama kolom pada DataFrame "df49"
df49.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df49.head()


# ### Halaman 50

# In[206]:


# Memanggil keyword dan menyalin url
keyword = "covid-19"
url = "https://turnbackhoax.id/page/50/?s={}".format(keyword)


# In[207]:


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


# In[208]:


# Memasukkan hasil scrapping ke dalam DataFrame
df50 = pd.DataFrame(data)
df50.tail()


# In[209]:


# Mengganti nama kolom pada DataFrame "df50"
df50.rename(columns={0:"Text", 1:"URL"}, inplace = True)
df50.head()


# ### Menggabungkan Beberapa DataFrame Menjadi 1

# In[210]:


# Membuat DataFrame untuk menampung hasil dari 50 df
data = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, 
       df21, df22, df23, df24, df25, df26, df27, df28, df29, df30, df31, df32, df33, df34, df35, df36, df37, df38, df39, df40,
       df41, df42, df43, df44, df45, df46, df47, df48, df49, df50]

# Menggabungkan 50 df menjadi 1 dengan fungsi "concat"
data_scrapping = pd.concat(data)

data_scrapping.info()


# In[211]:


data_scrapping.tail()


# In[212]:


# Menjadikan DataFrame ke dalam bentuk .csv
data_scrapping.to_csv("Data Scraping (turn back hoax) - covid-19.csv", index=False)

