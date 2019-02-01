
# coding: utf-8

# ### Transforming dataset distibutions

# In[32]:


# Two way to scale of data: normalization & standarization
# use sckit learn preprocessing:scale data, center data, normalize data, bin data, impute data
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

from pylab import rcParams
import seaborn as sb

import scipy

import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import scale


# In[4]:


get_ipython().magic('matplotlib inline')
rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')


# #### Normalizing and transforming features with MinMaxScalar() and fit_transform()

# In[6]:


address = 'F:\Learn R\Dataset\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']


# In[18]:


mpg = cars.mpg
plt.plot(mpg)


# In[23]:


cars[['mpg']].describe()


# In[33]:


mpg_matrix = mpg.values.reshape(-1,1)

scaled = preprocessing.MinMaxScaler(feature_range=(0,10))

scaled_mpg = scaled.fit_transform(mpg_matrix)

plt.plot(scaled_mpg)


# In[38]:


standardized_mpg=scale(mpg,axis=0,with_mean=False,with_std=False)
plt.plot(standardized_mpg)


# In[40]:


standardized_mpg = scale(mpg)
plt.plot(standardized_mpg)


# #### using scale() to scale  your features
