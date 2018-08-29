
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
get_ipython().magic(u'matplotlib inline')


# In[2]:


boston_data = load_boston()


# In[40]:


#boston_data dict contains: 'DESCR','data', 'feature_names', 'target'

X, y, feature = boston_data['data'], boston_data['target'], boston_data['feature_names']

feature_count = len(feature)
sample_count = len(X)


# In[62]:


#boston_data['DESCR']


# In[87]:


#In the housing plots, we're trying to plot all feature against targeted median. There are 13 features. 

fig, ax = plt.subplots(feature_count, 1, figsize=(15, 100))

for i in range(feature_count):
    ax[i].scatter(X[:, i], y, color= 'blue',edgecolor='black', linewidth=0.4, alpha = 0.5)
    ax[i].set_xlabel(feature[i])
    ax[i].set_ylabel('MEDV')
    ax[i].set_title(feature[i]+' vs. MEDV')

fig.text(0.5, .883, 'Bostin Housing Dataset', ha="center", fontsize=20)


# In[88]:


#store png  task33.png
fig.savefig('task33.png', bbox_inches="tight")

