# # Basics of Data Munging

# ## Filtering and selecting data

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# ## Selecting and retrieving data



series_obj = Series(np.arange(8), index = ['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6', 'row 7', 'row 8'])
series_obj


series_obj['row 7']


series_obj[[0,7]]



np.random.seed(25)
DF_obj = DataFrame (np.random.rand(36).reshape((6,6)), index = ['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6'],
                   columns = ['column 1', 'column 2', 'column 3', 'column 4', 'column 5', 'column 6'])
DF_obj



DF_obj.loc[['row 2', 'row 4'],['column 1','column 5']]


# ## Data slicing

# # DF_obj['row 2':'row 5']

# ## Comparing with scalars



DF_obj < 0.2


# ## Filtering with scalars 



series_obj[series_obj > 3]


# ## Setting values with scalars




series_obj['row 1','row 5', 'row 7']= 8
series_obj

