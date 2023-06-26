#!/usr/bin/env python
# coding: utf-8

# In[2]:


s={1,2,3,4,5,6,7,8,9}
print(s)
type(s)


# In[6]:


s=set()#empty set
print(s)


# In[7]:


s={1,2,3,4,5,6,7,8,9}
print(s[2])# SET NOT SUPPORT THE INDEXING 


# In[10]:


s={1,2,3,4,5}
s.add(6)
print(s) # aak baar me aak element hi add krr sakte hai and its prove it is mutable 


# In[12]:


s={1,2,3,4,5}
s.update({6,7,8,9,10})# for adding multiple element in a set than use update 
print(s)


# In[14]:


# set is a collectiion of unique elem and also list on set 
s={1,2,3,4,5}
s.update({1,2,3,8,9,7},[11,12,13,14])
print(s)# output me sirf unique elem hi ayenge 


# In[19]:


s={1,2,3,4,5}
s.discard(4)
s.remove(3)
print(s)


# In[22]:


s={1,2,3,4,5}
s.remove(6)


# In[24]:


s={1,2,3,4,5}
s.discard(6)# remove unavailable element ke liye error dega but discard koi error nahi dega 


# In[26]:


#using pop func 
s={1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 14}
s.pop()
print(s) # first element ko udaa dega 


# In[27]:


s.pop()
print(s)# abb second elem delete krr dega 


# In[28]:


s={1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 14}
s.clear()
print(s)


# In[32]:


s1={1,2,3,4,5}
s2={5,6,7,8,9}
print(s1|s2)# union 
#or write
print(s1.union(s2))
print(s1&s2)#intersection 
print(s1^s2)#symmetric diff mean common ko hata krr dono ke element AYENGE 


# In[34]:


x={1,2,3,4,5}
y={3,4,5}
print("x is subset of y",x.issubset(y))
print("y is subset of x",y.issubset(x))


# In[2]:


#frozen set is  IMMUTABLE IN NATURE 
f= frozenset([1,2,3,4,5])
print(f)


# In[3]:


f.add(6) # error kyoki frozen set immutable hota hai kuch add remove nahi kr sakte 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




