
# coding: utf-8

# # Concatenating and transforming data

# In[6]:


import numpy as np
import pandas as pd

from pandas import Series, DataFrame


# In[8]:


DF_obj = pd.DataFrame(np.arange(36).reshape(6,6))
DF_obj


# In[9]:


DF_obj_2 = pd.DataFrame(np.arange(15).reshape(5,3))
DF_obj_2


# ## Concatenating data

# In[14]:


# axis=1 gabung kolom (nambah k kanan)
# axis=0 gabung baris (nambah k bawah)
pd.concat([DF_obj,DF_obj_2],axis = 1)


# In[15]:


# tidak ditulis, axis=0
pd.concat([DF_obj,DF_obj_2])


# ## Transforming data

# ### Dropping data 

# In[23]:


DF_obj.drop([0,2], axis =0)


# In[20]:


# drop baris ke 1 dan 3
DF_obj.drop([0,2])


# In[24]:


# Drop kolom ke 1 dan 3
DF_obj.drop([0,2], axis =1)


# ### Adding data

# In[25]:


series_obj = Series(np.arange(6))
series_obj.name = 'added_variable'
series_obj


# In[29]:


#menambahkan kolom dengan  nama kolom added_variable
variable_added = DataFrame.join(DF_obj,series_obj)
variable_added


# In[36]:


# fungsi append menggabung tabel berdasarkan baris/nambah baris
# ignore index = False -> index tidak berurutan
added_datatable = variable_added.append(variable_added, ignore_index = False)
added_datatable


# In[37]:


added_datatable = variable_added.append(variable_added, ignore_index = True)
added_datatable


# ### Sorting data

# In[50]:


DF_obj


# In[59]:


# by = [x] diurutkan berdasarkan kolom ke - x
DF_sorted = DF_obj.sort_values(by = [0], ascending = [False])
DF_sorted

