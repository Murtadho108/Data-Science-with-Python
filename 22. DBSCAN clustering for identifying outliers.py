
# coding: utf-8

# ### DBSCAN clustering to identify outliers

# In[1]:


import pandas as pd
from pylab import rcParams
import seaborn as sb
import matplotlib.pyplot as plt

import sklearn
from sklearn.cluster import DBSCAN
from collections import Counter


# In[2]:


get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# #### DBSCAN clustering to identify outliers

# ##### Train your model and identify outliers

# In[26]:


df = pd.read_csv(filepath_or_buffer='F:\Learn R\Dataset\iris.csv')
df.columns=['Sepal Length','Sepal Width', 'Petal Length','Petal Width','Species']

data = df.iloc[:,0:4]
target = df.iloc[:,4]

df[:5]


# In[8]:


model = DBSCAN(eps = 0.8, min_samples=19).fit(data)
print (model)


# In[34]:


outliers_df = pd.DataFrame(data)
print (Counter(model.labels_))
print (outliers_df[model.labels_==-1])


# In[39]:


fig = plt.figure()

ax = fig.add_axes([.1,.1,1,1])

colors = model.labels_

ax.scatter(data[:,2],data[:,1],c=colors, s=120)

ax.set_xlabel('Petal Length')
ax.set_ylabel('Sepal Width')
plt.title('DBSCAN')

