#!/usr/bin/env python
# coding: utf-8
# In[ ]:
import numpy as np
# In[3]:
from scipy import sparse
# In[4]:
eye = np.eye(4)
# In[8]:
print("%s" % eye)
# In[10]:
x = np.arange(20)
# In[11]:
y = np.sin(x)
# In[ ]:
# In[13]:
import matplotlib.pyplot as plt
# In[14]:
plt.plot(x, y, marker="x")
# In[15]:
import pandas as pd
# In[16]:
data = {'name':["tiru","padma","manya","manav"], 'location' :["NY","LA","CHICAGO","Delhi"], 'Age':["45","40","16","10"]}
# In[17]:
data_pandas = pd.DataFrame(data)
# In[18]:
data_pandas
# In[19]:
print("%s\n" % pd.__version__)
# In[22]:
import matplotlib
print("%s\n" % matplotlib.__version__)
# In[21]:
import matplotlib
# In[23]:
print("%s\n" % np.__version__)
# In[28]:
import IPython
print("%s\n" % IPython.__version__)
# In[27]:
import IPython
from sklearn.datasets import load_iris
# In[31]:
iris = load_iris()
# In[32]:
iris.keys()
# In[33]:
print(iris['DESCR'][:193]+ "\n...")
# In[34]:
print("1")
iris['target_names']
iris['feature_names']
print("2")
# In[37]:
type(iris['data'])
iris['data'].shape
print("3")
# In[43]:
iris['data'][:5]
# In[44]:
from sklearn.model_selection import train_test_split
print("4")
# In[45]:
X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=0)
print("5")
# In[46]:
X_train.shape
# In[47]:
X_test.shape
# In[48]:
y_train.shape
# In[49]:
y_test.shape
# In[63]:
fig, ax = plt.subplots(3, 3, figsize=(15, 15))
# In[58]:
plt.suptitle("iris_pairplot")
print("6")
# In[64]:
for i in range(3):
    for j in range(3):
        ax[i,j].scatter(X_train[:,j],X_train[:,i+1],c=y_train,s=60)
        ax[i,j].set_xticks(())
        ax[i,j].set_yticks(())
        if i == 2:
            ax[i,j].set_xlabel(iris['feature_names'][j])
        if j == 0:
            ax[i,j].set_xlabel(iris['feature_names'][i+1])
        if j > i :
            ax[i,j].set_visible(False)
            
print("7")


plt.show()
