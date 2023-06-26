#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# class(userdefine datatype) > obj > atrribute(characterstics like colour,size etc > fuctions or method )


# In[13]:


class phone:# thisss is class 
    def calling(self): #function
        print("call laga diya re")
    def game(self):
        print("cod khelega tera bhai pubg nahi re")


# In[14]:


p1=phone()#object jo function upar banaye unko call karne ke liye aak obj ki jarurat padegi iss liye 


# In[27]:


p1.game()
p1.calling()


# In[19]:


class iphone14pro:
    def set_color(self,colour):#ye user dwara input dala jayega 
        self.colour=colour
    def set_cost(self,cost):
        self.cost=cost
    def show_colour(self):#ye jo upar user dwara input dala hai usko show karega call krne pe
        return self.colour
    def show_cost(self):
        return self.cost
    def calling(self): #function
        print("call laga diya re")
    def game(self):
        print("cod khelega tera bhai pubg nahi re")


# In[21]:


p2=iphone14pro()


# In[22]:


p2.set_color("DEEP PURPLE")# set wale functiuon ko call krr ke hum user input dalte hai 
p2.set_cost("1,30,0000 rupees only")


# In[23]:


p2.show_colour()# by this user input ko show karega 


# In[24]:


p2.show_cost()


# In[30]:


p2.calling()


# In[31]:


p2.game()


# In[ ]:


#SAME PROG BY USING CONSTRUCTOR 


# In[49]:


class Employee:
    
    def __init__(self,name,age,salary,gender):# def ke baad space than init likhe 
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
        
    def employee_details(self):
        print("name of the employee is",self.name)
        print("age of the employee is",self.age)
        print("salary of the employee is",self.salary)
        print("Gender of the employee is",self.gender)
    


# In[51]:


E1=Employee("shrey soni",23,1000000000000000000000000000,"Alpha male") # aaksath sara employee details input gaya ander


# In[52]:


E1.employee_details()


# In[ ]:


#inheritance in python 


# In[ ]:





# In[ ]:





# In[ ]:




