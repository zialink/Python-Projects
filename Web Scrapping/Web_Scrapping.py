#!/usr/bin/env python
# coding: utf-8

# In[27]:


from bs4 import BeautifulSoup
import requests, pandas

df= pandas.DataFrame(columns=['Cities','Description'])

headers= {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"
}
r=requests.get("https://pythonhow.com/example.html", stream= True, headers= headers)
content= r.content

soup=BeautifulSoup(content,"html.parser")
all= soup.find_all("div",{"class":"cities"})

for items in all:
    df=df.append({"Cities":items.find_all("h2")[0].text, "Description":items.find_all("p")[0].text}, ignore_index=True)
df.to_csv("Cities.csv")


# In[30]:





# In[ ]:




