#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([1,2,3,4,5,6,7,8,9])
a
#output od arrays are always tupple and we all know tupples are immutable in nature 


# In[3]:


a.ndim


# In[4]:


a.shape


# In[17]:


#2d and 3d array
b = np.array([[0,1,2], [3,4,5,], [6,7,8]])
b


# In[20]:


b.ndim


# In[21]:


b.shape


# In[24]:


c = np.array([[[0,1,2], [3,4,5,]], [[6,7,8], [9,10,11]]])
c


# In[25]:


c.ndim


# In[26]:


c.shape


# In[28]:


#arrange function 
e= np.arange(20)
e


# In[30]:


f= np.arange(0,41,5)
f


# In[32]:


#common array
a= np.ones((3,3))
a


# In[33]:


a= np.zeros((3,3))
a


# In[34]:


a= np.eye(5)
a


# In[35]:


a= np.eye(5,3)# 5 is no. of column and 3 is no. of row 
a


# In[40]:


#digonal matrix
a =np.diag([1,2,3,4,5,6,7,8,9])
a


# In[42]:


a =np.random.rand(10)
a


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




