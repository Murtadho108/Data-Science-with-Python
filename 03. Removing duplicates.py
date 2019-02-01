
# coding: utf-8

# ## Removing duplicates 

# In[2]:


import numpy as np
import pandas as pd

from pandas import Series, DataFrame


# In[29]:


# index untuk memberi labe pada row
# jika tdk ditulis index akan berlabel 0-6
DF_obj = DataFrame({'column 1':[1,1,2,2,3,3,3],
                   'column 2':['a','a','b','b','c','c','c'],
                   'column 3':['A','A','B','B','C','C','C']},index=['1','2','3','4','5','6','7'])
DF_obj


# In[21]:


DF_obj.duplicated()


# In[30]:


# untuk menghapus duplikat baris
DF_obj.drop_duplicates([])


# In[15]:


DF_obj = DataFrame({'column 1':[1,1,2,2,3,3,3],
                   'column 2':['a','a','b','b','c','c','c'],
                   'column 3':['A','A','B','B','D','C','C']},index=['1','2','3','4','5','6','7'])
DF_obj


# In[16]:


# menghapus duplikat berdasarkn entri yang sama pada kolom tertentu
DF_obj.drop_duplicates(['column 3'])

