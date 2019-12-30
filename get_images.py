#!/usr/bin/env python
# coding: utf-8

# In[22]:


# importing packages
import pandas as pd
import numpy as np
import os

# create dict
import itertools

# requests to download and resize images
import requests
from PIL import Image 


# In[23]:


# importing csv from get_league_data
champs_df = pd.read_csv('https://raw.githubusercontent.com/peanutshawny/league-of-legends/master/data/champions.csv')


# In[24]:


# path variables
image_path = 'D:/Python/league_of_legends/images/'
splash_path = 'D:/Python/league_of_legends/splash/'
icon_path = 'D:/Python/league_of_legends/icons/'

# os.listdir to check if directories have images already
image_list = os.listdir(image_path)
splash_list = os.listdir(splash_path)
icon_list = os.listdir(icon_path)


# In[25]:


# splitting up image urls for download
image_urls = list(champs_df['image'])
splash_urls = list(champs_df['splash'])
champ_names = list(champs_df['name'])

# creating dict with names as the key to set as name
images_dict = dict(zip(champ_names, image_urls))
splashes_dict = dict(zip(champ_names, splash_urls))


# In[26]:


# downloading images and splash art if directories are empty
if not image_list:
    for key, value in images_dict.items():
        with open(image_path + key + '.png', 'wb') as f:
            f.write(requests.get(value).content)

if not splash_list:    
    for key, value in splashes_dict.items():
        with open(splash_path + key + '.png', 'wb') as f:
            f.write(requests.get(value).content)


# In[18]:


# creating smaller icon for each image in image folder
if not icon_list:
    for item in image_list:
        im = Image.open(path + item)
        icon = im.resize((25, 25))
        icon.save(icon_path + f'{item}', 'PNG')

