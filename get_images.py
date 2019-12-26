#!/usr/bin/env python
# coding: utf-8

# In[12]:


# importing packages
import pandas as pd
import numpy as np
import os

# create dict
import itertools

# requests to download and resize images
import requests
from PIL import Image 


# In[13]:


# importing csv from get_league_data
champs_df = pd.read_csv('https://raw.githubusercontent.com/peanutshawny/league-of-legends/master/data/champions.csv')


# In[14]:


# splitting up image urls for download
image_urls = list(champs_df['image'])
champ_names = list(champs_df['name'])

# creating dict with names as the key
images_dict = dict(zip(champ_names, image_urls))


# In[15]:


# downloading images
for key, value in images_dict.items():
    f = open(f'D:/Python/league_of_legends/images/{key}.png', 'wb')
    f.write(requests.get(value).content)
    f.close()


# In[16]:


# path for images and icons
image_path = 'D:/Python/league_of_legends/images/'
icon_path = 'D:/Python/league_of_legends/icons/'
dirs = os.listdir(image_path)


# In[18]:


# creating smaller icon for each image in image folder
for item in dirs:
    im = Image.open(path + item)
    icon = im.resize((25, 25))
    icon.save(icon_path + f'{item}', 'PNG')

