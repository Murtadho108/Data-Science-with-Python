
# coding: utf-8

# ### Creating labels and annotations

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

from pylab import rcParams
import seaborn as sb


# In[2]:


get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# ### Labeling plot features

# #### The functional method

# In[3]:


x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]

plt.bar(x,y)

plt.xlabel('your x-axis label')
plt.ylabel('your y-axis label')


# In[19]:


z = [1,2,3,4,5]

veh_type = ['bicycle', 'motorbike', 'car', 'van', 'stroller']

plt.pie(z, labels = veh_type)
plt.show()


# #### The object-oriented method

# In[50]:


address = 'F:\Learn R\Dataset\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

mpg = cars.mpg

fig = plt.figure()

# add_axes untuk membuat batasan pada gambar
# left, bottom, width, height bernilai 0-1
ax = fig.add_axes([.1,.1,1,1])

mpg.plot()

ax.set_xticks(range(32))
# ax.set_xticklabels untuk label x-axis
ax.set_xticklabels(cars.car_names, rotation = 60, fontsize ='medium')

ax.set_title('Miles per gallon of cars in mtcars')

ax.set_xlabel('car names')
ax.set_ylabel('miles')



# ### Adding a legend to your plot

# #### The functional method

# In[53]:


# loc = best,upper right,upper left,lower left,lower right
# right,center left,center right,lower center,upper center,center
plt.pie(z)
plt.legend(veh_type,loc = 'best')
plt.show()


# #### The object-oriented method

# In[58]:


fig = plt.figure()

ax = fig.add_axes([.1,.1,1,1])
mpg.plot()

ax.set_xticks(range(32))
# ax.set_xticklabels untuk label x-axis
ax.set_xticklabels(cars.car_names, rotation = 60, fontsize ='medium')

ax.set_title('Miles per gallon of cars in mtcars')

ax.set_xlabel('car names')
ax.set_ylabel('miles')

ax.legend(loc='best')





# ### Annotating your plot

# In[59]:


mpg.max()


# In[ ]:


fig = plt.figure()

ax = fig.add_axes([.1,.1,1,1])
mpg.plot()

ax.set_title('Miles per Gallon of cars in mtcars')

ax.set_ylabel('miles/gal')
ax.set_ylim([0,45])
# xy : posisi koordinat
ax.annotate('Toyota Corolla', xy = (19,33.9),xytext=(21,35),arrowprops=dict(facecolor='black', shrink = 0.01))

