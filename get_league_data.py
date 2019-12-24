#!/usr/bin/env python
# coding: utf-8

# In[178]:


# importing packages
import pandas as pd
import numpy as np

# using the cassiopeia python wrapper for the riot api
import cassiopeia as cass


# In[179]:


# setting the key and region
key = 'RGAPI-9a714f74-318a-4690-b974-5d8181c0b66b'
cass.set_riot_api_key(key)
cass.set_default_region("NA")


# In[180]:


# getting data on all champions with get_champion method
champs = cass.get_champions()
champs = list(champs)


# In[181]:


# appending all useful champion data, including names, ids, info, stats, and images
champ_keys = []
champ_names = []
champ_ids = []
champ_info = []
champ_stats = []
champ_tags = []
champ_images = []

for champ in champs:
    champ_keys.append(champ.key)
    champ_names.append(champ.name)
    champ_ids.append(champ.id)
    champ_info.append(champ.info.to_dict())
    champ_stats.append(champ.stats.to_dict())
    champ_tags.append(champ.tags)
    champ_images.append(champ.image.url)


# In[182]:


# transform all lists into one dataframe
champ_dict = {'key': champ_keys, 'name': champ_names, 'id': champ_ids, 'info': champ_info,
             'stats': champ_stats, 'tags': champ_tags, 'image': champ_images}
champ_df = pd.DataFrame(champ_dict)


# In[184]:


# splitting dictionaries within columns into separate columns
champ_df = champ_df.join(champ_df['info'].apply(pd.Series))
champ_df = champ_df.join(champ_df['stats'].apply(pd.Series))


# In[187]:


# removing unecessary columns
champ_df.drop(['info', 'stats'], axis = 1, inplace = True)


# In[190]:


# writing to csv
champ_df.to_csv('D:/Python/league_of_legends/data/champions.csv', index = False)

