
# coding: utf-8

# ### Multivariate analysis for outlier detection

# In[2]:


# Tools : scatter plot, boxplot
import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb


# In[4]:


get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# #### Visually inspecting boxplots

# In[5]:


df = pd.read_csv(filepath_or_buffer='F:\Learn R\Dataset\iris.csv')
df.columns=['Sepal Length','Sepal Width', 'Petal Length','Petal Width','Species']

df[:5]


# #### Looking at the scatterplot matrix

# In[12]:


sb.boxplot(x='Species', y='Sepal Length', data=df, palette ='hls')


# In[13]:


sb.pairplot(df,hue='Species',palette = 'hls')

