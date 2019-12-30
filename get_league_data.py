#!/usr/bin/env python
# coding: utf-8

# In[36]:


# importing packages
import pandas as pd
import numpy as np

# using the cassiopeia python wrapper for the riot api
import cassiopeia as cass

from matplotlib.pyplot import imread, imshow
from matplotlib import pyplot as plt


# In[37]:


# setting the key and region
key = 'RGAPI-1f4663d7-0db2-4037-9089-0198be7ca0c3'
cass.set_riot_api_key(key)
cass.set_default_region("NA")


# In[38]:


# getting data on all champions with get_champion method
champs = cass.get_champions()
champs = list(champs)


# In[39]:


# appending all useful champion data, including names, ids, info, stats, and images
champ_keys = []
champ_names = []
champ_ids = []
champ_info = []
champ_stats = []
champ_tags = []
champ_images = []
champ_splashes = []

for champ in champs:
    champ_keys.append(champ.key)
    champ_names.append(champ.name)
    champ_ids.append(champ.id)
    champ_info.append(champ.info.to_dict())
    champ_stats.append(champ.stats.to_dict())
    champ_tags.append(champ.tags)
    champ_images.append(champ.image.url)
    champ_splashes.append(champ.skins.find('default').loading_image_url)


# In[40]:


# transform all lists into one dataframe
champ_dict = {'key': champ_keys, 'name': champ_names, 'id': champ_ids, 'info': champ_info,
             'stats': champ_stats, 'tags': champ_tags, 'image': champ_images, 'splash': champ_splashes}
champ_df = pd.DataFrame(champ_dict)


# In[41]:


# splitting dictionaries within columns into separate columns
champ_df = champ_df.join(champ_df['info'].apply(pd.Series))
champ_df = champ_df.join(champ_df['stats'].apply(pd.Series))


# In[42]:


# removing unecessary columns
champ_df.drop(['info', 'stats'], axis = 1, inplace = True)


# In[43]:


# writing to csv
champ_df.to_csv('D:/Python/league_of_legends/data/champions.csv', index = False)

