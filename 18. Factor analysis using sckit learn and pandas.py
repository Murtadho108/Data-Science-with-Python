
# coding: utf-8

# ### Explanatory factor analysis

# In[ ]:


# Factor analysis : A method used to explore datasets to find root
# causes that explain why data is actng a certain way


# In[1]:


import pandas as pd
import numpy as np

import sklearn
from sklearn.decomposition import FactorAnalysis

from sklearn import datasets


# #### Factor analysis on iris dataset

# In[3]:


iris  = datasets.load_iris()
x = iris.data
variable_name = iris.feature_names

x[0:10,]


# In[4]:


factor = FactorAnalysis().fit(x)

pd.DataFrame(factor.components_, columns = variable_name)


# In[11]:


x


# In[15]:


pd.DataFrame(x)

