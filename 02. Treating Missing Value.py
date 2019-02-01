
# coding: utf-8

# ## Treating missing values

# In[9]:


import numpy as np
import pandas as pd

from pandas import Series, DataFrame


# ## Figuring out what data is missing

# In[10]:


missing = np.nan
series_obj = Series(['row 1', 'row 2',missing,'row 4', 'row 5', missing, 'row 6'])
series_obj


# In[11]:


series_obj.isnull()


# ## Filling in for missing values

# In[26]:


np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6,6))
DF_obj


# In[28]:


DF_obj.loc[3:5,0]=missing
DF_obj.loc[1:4,5]=missing
DF_obj


# In[30]:


filled_DF=DF_obj.fillna(0)
filled_DF


# In[34]:


fill_DF = DF_obj.fillna(method='ffill')
fill_DF


# ## Counting missing values

# In[36]:


np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6,6))

DF_obj.loc[3:5,0]=missing
DF_obj.loc[1:4,5]=missing

DF_obj


# ## Filtering out missing values

# In[48]:


#angka axis=1 menunjukkan pilih kolom yg tdk NaN
#angka axis=0 menunjukkan pilih baris yg tdk NaN
DF_no_NaN = DF_obj.dropna(axis=1) 

DF_no_NaN


# In[49]:


#menunjukkan kembali kondisi awal
DF_obj.dropna(how = 'all')

