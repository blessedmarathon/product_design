#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import os

#os.getcwd()

listings = pd.read_csv("listings.csv")

listings.head(2)
#listings.tail(2)




# In[3]:


listings.to_json("listing.json")


# In[4]:


listings.columns
#listings.index


# In[5]:


listings.index


# In[6]:


listings.sort_index(axis=1, ascending=True)


# In[7]:


listings.sort_values(by='id')


# In[8]:


minlisting = listings[0:100]
minlisting


# In[9]:


listings["room_type"].unique()


# In[11]:


listings.room_type


# In[12]:


listings.isnull().sum()


# In[13]:


listings.loc[3]


# In[14]:


listings.isna().sum()


# In[16]:


listings = listings.fillna(0)
listings.mean()


# In[17]:


neighbourhoods = pd.read_csv("neighbourhoods.csv")


# In[18]:


neighbourhoods


# In[19]:


merged_listings = listings.merge(neighbourhoods, on='neighbourhood', suffixes=('_old','_new'))


# In[20]:


merged_listings.head(100)


# In[21]:


room_types = merged_listings["room_type"].unique()


# In[22]:


import plotly.express as px

fig = px.histogram(merged_listings, x="room_type", color="room_type", title="airbnb")
fig.show()


# In[23]:


import plotly.express as px

### let's do a pie chart!
fig = px.pie(merged_listings, names='room_type')
fig.show()

## todo
## new field "priceByCondition"
## follow-up and do a pie chart on it!


# In[24]:


import plotly.express as px

fig = px.histogram(merged_listings, x="neighbourhood_group_new", color="neighbourhood")
fig.show()
# what happens to the color of the bar chart?


# In[76]:


import plotly.express as px
import numpy as np

def priceCategory(price):
 if price > 3000 :
    return "over 3000"
 elif price > 2000 :
    return "between 2001 and 3000"
 elif price > 1000 :
    return "between 1001 and 2000"
 elif price > 700 :
    return "between 701 and 1000"
 elif price > 500 :
    return "between 501 and 700"
 else :
    return "less than 500"

merged_listings["price_by_condition"] = merged_listings["price"].apply(priceCategory)
merged_listings["total"] = 1

## - another method:
## values=listings["id"].value_counts().values

#merged_listings

### let's do a pie chart!
fig = px.pie(merged_listings, names='price_by_condition', values='total', hole=0.2)
fig.show()

## todo
## new field "priceByCondition"
## follow-up and do a pie chart on it!

