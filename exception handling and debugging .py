#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# very very very imp 
#practice by coders yo maintain professnalism
#use of 'try clause' 


# In[1]:


v=w


# In[3]:


if a>3


# In[4]:


1/0


# In[11]:


#prog for error handling
import sys
list=["v",0,2,4,7,-8,9,3.1417]# isme sirf ,2' hi valid input hai baki invalid error dega 
for entry in list:
    try:
        print("input hai yeh",entry)
        r=1/int(entry)# reciprocal nikalna hai entry kaa 
    except:
           print('galat ya invalid entry ki hai apne chicha',sys.exc_info()[0]," ye wala error occured hua hai.")
           print('next entry')
           print("###@@@!!!%%%^^^&&&***((()))___+++===~~~```{{{|||\\\///,,,<<<.>>>}}}")
    print("RECIPROCAL OF",entry,"is",r)


# In[13]:


#raise of perticular error
raise MemoryError("abe sale ram kam hai mere laptop me ")


# In[15]:


# finally block is executed no matter what!
try:
    f=open('file','w')
    #apna jo kaam jo kamm jai karo 
finally:
        f.close()# must hai nahi to program ram me rahega aur system restart ke baad udd jayega 


# In[ ]:


#DEBUGGING OR pdb


# In[1]:


import pdb#call for debugg func  
def seq(n):
    for i in range(n):
        pdb.set_trace()#breakpoint
        print(i)
    return
seq(6)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




