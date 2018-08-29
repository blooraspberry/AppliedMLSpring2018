
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


#link to plot: http://www.tylervigen.com/spurious-correlations

data = pd.read_csv('task31.csv')
year = data['Year']
deaths = data['Railway Train Collisions (deaths)']
barrels = data['US Crude Oil from Norway (Barrels)']


# In[4]:


get_ipython().magic(u'matplotlib inline')


# In[90]:


fig = plt.figure()

#line1 Barrels

ax1 = plt.gca()
line1, = ax1.plot(year, barrels, 'rD', linestyle='-')
plt.xticks(np.arange(min(year), max(year)+1, 1.0), color = 'black')

#line2 Deaths

ax2 = ax1.twinx()
line2, = ax2.plot(year, deaths,'ko', linestyle='-')
plt.xticks(np.arange(min(year), max(year)+1, 1.0), color = 'red')

#multi-line titles with different colors using text

fig.text(0.5, 1.1, 'US crude oil imports from Norway',ha="center", fontsize=14, color = 'red')
fig.text(0.5, 1.05, 'correlates with', ha="center", fontsize=12, color = 'grey' )
fig.text(0.5, 0.99, 'Drivers Killed in collision with railway train', ha="center", fontsize = 16, color='black')
fig.text(0.5, 0.92, 'Correlation: 95.45% (r=.954509)', ha="center", fontsize = 11, color='black')

#legend
plt.legend((line2, line1), ('Railway train collisions', 'US crude oil imports from Norway'))

#Labels and Ticks
ax1.set_ylabel('US crude oil imports from Norway \n (Million Barrels)', color = 'red')
ax2.set_ylabel('Railway train collisions \n (Deaths)', color ='black')
ax1.xaxis.set_ticks_position('both')

#ax1.set_xticks(np.arange(min(year), max(year)+1, 1.0))
#ax2.set_xticks(np.arange(min(year), max(year)+1, 1.0))
ax1.set_yticks(np.arange(0, 150+1, 50))
ax2.set_yticks(np.arange(40, 100+1, 20))


# In[95]:


#store png  task31.png
fig.savefig('task31.png', bbox_inches="tight")

