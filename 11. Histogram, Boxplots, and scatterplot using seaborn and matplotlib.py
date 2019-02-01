
# coding: utf-8

# ### Constructing histogram, box plots, and scatter plots

# In[36]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

from pandas.tools.plotting import scatter_matrix

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb


# In[3]:


get_ipython().magic('matplotlib inline')
rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')


# #### Eyeballing dataset distributions with histograms

# In[22]:


address = 'F:\Learn R\Dataset\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

cars.index = cars.car_names

mpg = cars['mpg']

mpg.plot(kind='hist')


# In[5]:


plt.hist(mpg)

plt.plot()


# In[6]:


sb.distplot(mpg)


# #### Seeing scatterplots in action

# In[9]:


cars.plot(kind='scatter', x = 'hp', y='mpg', c=['darkgray'], s=150)


# In[10]:


sb.regplot(x='hp', y='mpg', data = cars, scatter = True)


# #### Generating a scatter plot matrix

# In[11]:


sb.pairplot(cars)


# In[49]:


#(cars.ix[:,(1,3,4,6)].values) : memilih kolom 1,3,4,6 dari tabel cars
cars_df = pd.DataFrame((cars.ix[:,(1,3,4,6)].values), columns = ['mpg','disp','hp','wt'])

cars_target = cars.ix[:,9].values
target_names = [0,1]
#menambah kolom bernama 'goup' dari cars_df
cars_df['group']=pd.Series(cars_target, dtype = "category")
# list of palette: hls, husl, dark, pastel, muted, bright, deep, colorblind
sb.pairplot(cars_df, hue='group', palette='hls')


# #### Building boxplot

# In[50]:


cars.boxplot(column='mpg', by ='am')
cars.boxplot(column='wt', by ='am')


# In[51]:


sb.boxplot(x='am',y='mpg', data=cars, palette='hls')

