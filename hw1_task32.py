
# coding: utf-8

# In[197]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from sklearn.datasets import load_iris
get_ipython().magic(u'matplotlib inline')


# In[159]:


iris_dataset = load_iris()

#dict of iris dataset:  dict_keys(['target_names', 'feature_names', 'DESCR', 'data', 'target'])
#set variables 
X, y, feature, target = iris_dataset['data'], iris_dataset['target'], iris_dataset['feature_names'], iris_dataset['target_names']

feature_count = len(X[0])
sample_count = len(X)
class_name = target.tolist()

#for the output of y: 
#0 means setosa, 1 means versicolor, and 2 means virginica, which refers to class_name


# In[201]:


#In pair plot, we're trying to look at all possible pairs of features.
# when the pair of the features are the same, a histogram would show. Otherwise, a scatter plot would show

fig, ax = plt.subplots(feature_count, feature_count, figsize=(15, 15))
cc = np.array(['blue', 'red', 'green'])
legend_type = []

#add plots

for i in range(feature_count):
    for j in range(feature_count):
        
        # if i==j, then we'd do a histogram of count
        if i == j:
            ax[i, j].hist(X[:, i], bins = 20, edgecolor='black', linewidth=0.5, color = 'blue')
            
        # scatter plot between the two different features
        else: 
            ax[i, j].scatter(X[:, j], X[:, i], color= cc[y],edgecolor='black', linewidth=0.5)
            
        # add x/y labels
        if j == 0:
            ax[i, j].set_ylabel(feature[i])
        if i == 3:
            ax[i, j].set_xlabel(feature[j])
            
#legend for feature colors

for leg_col in cc:
    legend_type.append(Circle((1, 1), 1, color = leg_col))

fig.legend(legend_type, class_name, loc = 'center right', prop={'size': 11})
fig.text(0.5, .9, 'Iris Pair-Plot Dataset', ha="center", fontsize=20)


# In[202]:


#store png  task32.png
fig.savefig('task32.png', bbox_inches="tight")

