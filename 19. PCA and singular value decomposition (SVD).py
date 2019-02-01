
# coding: utf-8

# ### Principal component analysis

# In[5]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import pylab as plt
import seaborn as sb
from IPython.display import Image
from IPython.core.display import HTML
from pylab import rcParams

import sklearn
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn import datasets


# In[6]:


get_ipython().magic('matplotlib inline')
rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')


# #### PCA on the iris dataset

# In[13]:


iris = datasets.load_iris()
x = iris.data
variable_names = iris.feature_names

x[0:10,]


# In[8]:


pca = decomposition.PCA()
iris_pca = pca.fit_transform(x)
pca.explained_variance_ratio_


# In[9]:


# cumulative variance
pca.explained_variance_ratio_.sum()


# In[15]:


comps = pd.DataFrame(pca.components_,columns=variable_names)
comps


# In[16]:


sb.heatmap(comps)

