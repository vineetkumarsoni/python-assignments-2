#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#MAINLY USED IN GROUP OR LARGE PROJECT
# USING AS REFERENCE AND IMPORT FUNCTION  


# In[1]:


import math# math aak module hai jise call kiya gaya hai usme kisi ne 'pi'ki value save ki hai wahi print ho rahi hai 
print(math.pi)


# In[3]:


import datetime 
datetime.datetime.now()


# In[5]:


import math as m
print(m.pi)


# In[6]:


#to get the all madules of math
dir(math)


# In[12]:


import math as m  #prod module usecase
seq=(2,2,2,9)
print(m.prod(seq))


# In[ ]:


#FILE HANDLING 
#OPEN ,READ, WRITE,CLOSE OF FILE SIKHNA HAI 
#STRUCTURE= f= open("file" , "(r)")
#r=read
#w=write (but purana hatane ya truncate krne ke baad )
#a=appending(purana jodega but pichna remain rakhega )
#t=text mode
#b=binary mode
#+=open file for updating


# In[ ]:


#to get the location of current working directary 


# In[1]:


import os
os.getcwd()


# In[2]:


f=open('file','w')#file bann gai hai back jaake home page me check kare


# In[4]:


f=open('file','w')
f.close()#isse file ram se permanent memory me store ho jati hai 
#not a good practice 


# In[5]:


try:
    f=open('file','w')
finally:
    f.close()
    #good practice 


# In[6]:


# write in the file 
f=open('file','w')
f.write("hello everybuddy mera naaam \n")
f.write("vineet kumar soni hai \n")
f.close()


# In[7]:


#jo likha usse pdhna hai to
f=open('file','r')
f.read()


# In[8]:


#read by character
f=open('file','r')
f.read(12)#12 word hi show karenge read ke liye 


# In[9]:


print(f.read())


# In[11]:


f.seek(0)
for line in f:
    print(line)


# In[12]:


# aak aak krr ke file read krne ke liye 
f=open('file','r')
f.readline()# read first line 


# In[13]:


f.readline()#read second line 


# In[14]:


f.readline ()# third line hai hi nahi yo kuch read nahi kareaga 


# In[15]:


os.listdir(os.getcwd())# sabhi directary ke naam jo home page me hai 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




