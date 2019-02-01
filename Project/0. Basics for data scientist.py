
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
edu = pd.read_csv( 'F:\Learn Python\Data\educ_figdp_1_Data.csv',
                 na_values = ':',
                 usecols = ['TIME','GEO','Value'])


# In[3]:


edu.head()


# In[4]:


edu.tail()


# In[5]:


edu.describe()


# In[6]:


edu['Value']


# In[7]:


edu[10:14]


# In[8]:


edu.ix[90:94,['TIME','GEO']]


# In[9]:


edu[edu['Value'] > 6.5].tail()


# In[10]:


edu[edu['Value'].isnull()].tail()


# In[11]:


edu.max(axis = 0)


# In[12]:


print ("Pandas max function:"), edu['Value'].max()
print ("Python max function:"), max(edu['Value'])


# In[13]:


s = edu['Value']/100
s.head()


# In[14]:


s = edu['Value'].apply(np.sqrt)
s.head()


# In[15]:


s = edu['Value'].apply(lambda a: a**2)
s.head()


# In[16]:


edu['+newcol'] = edu['Value']/edu['Value'].max()
edu.tail()


# In[17]:


edu.drop('+newcol',axis = 1, inplace = True)
edu.head()


# In[18]:


edu = edu.append({'TIME': 2000,'Value': 5.00,'GEO':'+ row bawah'},
                ignore_index = True)
edu.tail()


# In[19]:


edu.drop(max(edu.index),axis = 0, inplace = True)
edu.tail()


# In[20]:


eduDrop = edu.dropna(how = 'any', subset = ['Value'])
eduDrop.head()


# In[21]:


eduFilled = edu.fillna(value = {'Value': 0})
eduFilled.head()


# In[22]:


edu.sort_values(by = 'Value', ascending = False,
              inplace = True)
edu.head()


# In[23]:


edu.sort_index(axis = 0, ascending = True, inplace = True)
edu.head()


# In[24]:


group = edu[['GEO', 'Value']].groupby('GEO').mean()
group.head()


# In[25]:


filtered_data = edu[edu['TIME']>2005]
pivedu = pd.pivot_table(filtered_data, values = 'Value',
                       index = ['GEO'],
                       columns = ['TIME'])
pivedu.head()


# In[26]:


pivedu.ix[['Spain','Portugal'], [2006,2011]]


# In[27]:


pivedu = pivedu.drop([
    'Euro area (13 countries)',
    'Euro area (15 countries)',
    'Euro area (17 countries)',
    'Euro area (18 countries)',
    'European Union (25 countries)',
    'European Union (27 countries)',
    'European Union (28 countries)'
],
    axis=0)
pivedu = pivedu.rename(index = {'Germany (until 1990 former territory of the FRG )':'Germany'})
pivedu = pivedu.dropna()
pivedu.rank(ascending = False, method = 'first').head()


# In[28]:


totalSum = pivedu.sum(axis = 1)
totalSum.rank(ascending = False, method = 'dense').sort_values().head()


# In[29]:


totalSum = pivedu.sum(axis = 1).sort_values(ascending = False)
totalSum.plot(kind = 'bar', style = 'r', alpha = 0.4,
             title = 'Total Values for Country')


# In[31]:


#kind = barh, bar, hist, box,kde,area, scatter, hexbin, pie
my_colors = ['b', 'r', 'g', 'y', 'm', 'c']
ax = pivedu.plot(kind = 'barh', 
                stacked = True,
                color = my_colors)
ax.legend(loc = 'center right', bbox_to_anchor = (1,0.5))
plt.show()

