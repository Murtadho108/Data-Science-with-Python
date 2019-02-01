
# coding: utf-8

# ### Using NumPy to perform arithmetic operation on data

# In[2]:


import numpy as np
from numpy.random import randn


# In[5]:


np.set_printoptions(precision=2)


# ### Creating arrays

# #### Creating arrays using a list

# In[6]:


a = np.array([1,2,3,4,5,6])
a


# In[8]:


b = np.array([[10,20,30],[40,50,60]])
b


# #### Creating arrays via assignment

# In[13]:


np.random.seed(25)
c=36*np.random.randn(6)
c


# In[15]:


d = np.arange(1,35)
d


# ### Performing arithmetic on arrays

# In[16]:


a*10


# In[17]:


c+a


# In[18]:


c-a


# In[19]:


c*a


# In[20]:


c/a


# ### Multiplying matrices and basic linear algebra

# In[30]:


aa = np.array([[2.,4.,6.],[1.,3.,5.],[10.,20.,30.]])
aa


# In[29]:


bb = np.array([[0.,1.,2.],[3.,4.,5.],[6.,7.,8.]])
bb


# In[32]:


# perkalian antar elemen matrix
aa * bb


# In[33]:


# perkalian matrix
np.dot(aa,bb)

