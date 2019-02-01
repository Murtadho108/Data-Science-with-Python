
# coding: utf-8

# ### Non-parametric methods using pandas and scipy

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

from pylab import rcParams
import seaborn as sb

import scipy
from scipy.stats import spearmanr


# In[4]:


get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# In[6]:


address = 'F:\Learn R\Dataset\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

cars.head()


# In[7]:


sb.pairplot(cars)


# In[8]:


x = cars[['cyl','am','gear']]
sb.pairplot(x)


# In[12]:


cyl = cars['cyl']
vs = cars['vs']
am = cars['am']
gear = cars['gear']

spearmanr_coefficient, p_value=spearmanr(cyl,vs)
print( 'Separman Rank Correlation Coefficient %0.3f' %(spearmanr_coefficient))


# In[13]:


spearmanr_coefficient, p_value=spearmanr(cyl,am)
print( 'Separman Rank Correlation Coefficient %0.3f' %(spearmanr_coefficient))


# In[14]:


spearmanr_coefficient, p_value=spearmanr(cyl,gear)
print( 'Separman Rank Correlation Coefficient %0.3f' %(spearmanr_coefficient))


# #### Chi-Square test for independence

# In[16]:


table = pd.crosstab(cyl,am)

#p<0.05 reject null hypothesis -> variables are correlated
from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(table.values)
print('Chi-square statistics %0.3f p_value %0.3f' % (chi2,p))


# In[19]:


table = pd.crosstab(cars['cyl'],cars['vs'])

#p<0.05 reject null hypothesis -> variables are correlated
from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(table.values)
print('Chi-square statistics %0.3f p_value %0.3f' % (chi2,p))


# In[20]:


table = pd.crosstab(cars['cyl'],cars['gear'])

#p<0.05 reject null hypothesis -> variables are correlated
from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(table.values)
print('Chi-square statistics %0.3f p_value %0.3f' % (chi2,p))

