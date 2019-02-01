
# coding: utf-8

# ### Creating visualization from time series data

# In[2]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

from pylab import rcParams
import seaborn as sb

from numpy.random import randn


# In[3]:


get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# #### The simple time series plot

# In[24]:


address = 'F:\Learn R\Dataset\Superstore-Sales.csv'
#index_col : untuk menentukan kolom mana yang dijadikan kolom pertama
# parse_dates : membaca kolom sebagai tanggal, bukan sbagai string atau float
df = pd.read_csv(address, index_col = 'Order Date', parse_dates = True)

df.head


# In[25]:


df['Order Quantity'].plot()


# In[40]:


#random_state = pilih acak data
df2 = df.sample(n=100, random_state=2,axis=0)
plt.xlabel('Order Data')
plt.ylabel('Order Quantity')

plt.title('Superstore Sales')

df2['Order Quantity'].plot()

