
# coding: utf-8

# ### Generating summary statistics using pandas and scipy

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats


# In[6]:


address = 'F:\Learn R\Dataset\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

cars.head()


# #### Looking at summary statistics thet describe a variable's numeric values

# In[7]:


cars.sum()


# In[10]:


cars.sum(axis=1)


# In[11]:


cars.median()


# In[12]:


cars.mean()


# In[13]:


cars.max()


# In[16]:


mpg = cars.mpg
mpg.idxmax()


# #### Looking at summary statistics that describe variable distribution

# In[19]:


cars.std()


# In[20]:


cars.var()


# In[21]:


#unique
gear = cars.gear
gear.value_counts()


# In[22]:


cars.describe()

