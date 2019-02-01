
# coding: utf-8

# ### Creating standard plots (line,bar,pie)

# In[1]:


get_ipython().system(' pip install Seaborn')


# In[3]:


import numpy as np
from numpy.random import randn
import pandas as pd

from pandas import Series, DataFrame
import matplotlib.pyplot as plt

from matplotlib import rcParams

import seaborn as sb


# In[7]:


# set_style = whitegrid, dark, white, ticks
get_ipython().magic('matplotlib inline')

rcParams['figure.figsize']= 5,4

sb.set_style('whitegrid')


# ### Creating aline chart from a list object

# #### Plotting a line chart in matplotlib

# In[12]:


x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]

plt.plot(x,y)


# #### Plotting a line chart from a pandas object

# In[15]:


address = 'F:\Learn R\Dataset\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

mpg = cars['mpg']

mpg.plot()


# In[20]:


df = cars[['cyl','wt','mpg']]
df.plot()


# ### Creating bar charts

# #### Creating a bar chart from a list

# In[21]:


plt.bar(x,y)


# #### Creating bar chart from pandas objects

# In[22]:


mpg.plot(kind = 'bar')


# In[25]:


mpg.plot(kind = 'barh')


# #### Creating a pie chart

# In[29]:


x = [1,2,3,4,5]
plt.pie(x)
plt.show()


# In[31]:


plt.savefig('pe_chart.jpeg')
plt.show()


# In[32]:


get_ipython().magic('pwd')

