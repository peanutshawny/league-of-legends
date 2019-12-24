#!/usr/bin/env python
# coding: utf-8

# In[32]:


# importing packages
import pandas as pd
import numpy as np

# create dict
import itertools

# requests to download images
import requests


# In[33]:


# importing csv from get_league_data
champs_df = pd.read_csv('https://raw.githubusercontent.com/peanutshawny/league-of-legends/master/data/champions.csv')


# In[34]:


# splitting up image urls for download
image_urls = list(champs_df['image'])
champ_names = list(champs_df['name'])

# creating dict with names as the key
images_dict = dict(zip(champ_names, image_urls))


# In[35]:


# downloading images
for key, value in images_dict.items():
    f = open(f'D:\Python\league_of_legends\images\\{key}.png', 'wb')
    f.write(requests.get(value).content)
    f.close()

