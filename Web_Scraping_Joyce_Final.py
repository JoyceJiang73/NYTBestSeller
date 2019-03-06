#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import json
import requests
from pprint import pprint
from scipy.stats import linregress
from scipy import stats


# In[2]:


from bs4 import BeautifulSoup
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'}

# In[3]:


data = pd.read_json('Resources/nyt2_1.json', lines=True, orient='columns')
data.head()


# In[4]:


json_books = data.to_json(path_or_buf='output.json',orient = "records")
json_books


# In[5]:


with open('output.json') as file:
    data = json.load(file)


# In[6]:


url=data[1]['amazon_product_url']
url


# In[7]:


import time


# In[14]:


reviews=[]
rating=[]
price_1=[]
price_2=[]
price_3=[]
price_4=[]
amazon_url=[]

for x in data:
    try:
        url=x['amazon_product_url']
        response = requests.get(url,headers=headers)
        
        soup = BeautifulSoup(response.text, 'lxml')
    
        review=soup.find_all('span',id="acrCustomerReviewText")[0].text
        rate=soup.find('span',class_="a-icon-alt").text
        price1=soup.find_all('span',class_="a-size-small a-color-price")[0].text
#        price2=soup.find_all('span',class_="a-size-small a-color-price")[1].text
#        price3=soup.find_all('span',class_="a-size-small a-color-price")[2].text
#        price4=soup.find_all('span',class_="a-size-small a-color-price")[3].text

        reviews.append(review)
        rating.append(rate)
        price_1.append(price1)
#        price_2.append(price2)
#        price_3.append(price3)
#        price_4.append(price4)
        amazon_url.append(url)
        
        print(review,rate,price1)

    #    t0 = time.time()
    #    response_delay = time.time() - t0
    #    time.sleep(10*response_delay)

    except IndexError:
        print("error")
    


# In[15]:


reviews


# In[16]:


#response = requests.get(url)
#soup = BeautifulSoup(response.text, 'lxml')
#print(soup.prettify())


# In[91]:


#price1=soup.find_all('span',class_="a-size-small a-color-price")[0].text
#price2=soup.find_all('span',class_="a-size-small a-color-price")[1].text
#price3=soup.find_all('span',class_="a-size-small a-color-price")[2].text
#price4=soup.find_all('span',class_="a-size-small a-color-price")[3].text


# In[20]:


table = pd.DataFrame(np.column_stack([amazon_url, reviews, rating, price_1]), 
                               columns=['url','reviews', 'rating', 'price'])
table


# In[21]:


table.to_csv('output4.csv')


# In[ ]:






#%%
