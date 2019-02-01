
# coding: utf-8

# ### Extreme value analysis using univariate methods

# In[1]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams


# In[ ]:


get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4


# In[100]:


df = pd.read_csv(filepath_or_buffer='F:\Learn R\Dataset\iris.csv')
df.columns=['Sepal Length','Sepal Width', 'Petal Length','Petal Width','Species']
x = df.iloc[:,0:4].values
y = df.iloc[:,4].values
df.head()


# #### Identifying outliers from tukey boxplots

# In[105]:


df.boxplot(return_type='dict')
plt.show()


# In[115]:


Sepal_Width=x[:,1]

iris_outliers = (Sepal_Width>4)
df[iris_outliers]


# #### Applying Tukey outier labeling

# In[127]:


pd.options.display.float_format = '{:.1f}'.format

x_df = pd.DataFrame(x)

x_df.describe()

