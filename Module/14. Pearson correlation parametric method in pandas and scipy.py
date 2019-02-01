
# coding: utf-8

# ### Starting with parametric methods in pandas and scipy

# In[14]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from pylab import rcParams
import seaborn as sb

import scipy
from scipy.stats.stats import pearsonr


# In[3]:


get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# #### The pearson correlation

# In[5]:


address = 'F:\Learn R\Dataset\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']


# In[6]:


sb.pairplot(cars)


# In[7]:


x = cars[['mpg','hp','qsec','wt']]
sb.pairplot(x)


# #### Using scipy to calculate the pearson correlation coefficient

# In[33]:


mpg = cars['mpg']
hp = cars['hp']
qsec = cars['qsec']
wt = cars['wt']

pearsonr_coefficient, p_value = pearsonr(mpg,hp)
print('PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient))


# In[34]:


pearsonr_coefficient, p_value = pearsonr(mpg,qsec)
print('PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient))


# In[35]:


pearsonr_coefficient, p_value = pearsonr(mpg,wt)
print('PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient))


# In[36]:


corr = x.corr()
corr


# #### Using pandas to calculate the pearson correlation coefficient

# In[38]:


sb.heatmap(corr,xticklabels=corr.columns.values, yticklabels=corr.columns.values)


# #### Using seaborn to visualize the pearson correlation coefficient
