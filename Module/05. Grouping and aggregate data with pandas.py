
# coding: utf-8

# ## Grouping and data aggregation

# In[4]:


import numpy as np
import pandas as pd

from pandas import Series, DataFrame


# ### Grouping data by column index

# In[26]:


address = 'F:\Learn R\Dataset\mtcars.csv'
cars = pd.read_csv(address)

cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

cars


# In[31]:


# group berdasarkan banyak silinder
# berdasarkan mean, std, dsb
cars_groups = cars.groupby(cars['cyl'])
cars_groups.mean()

