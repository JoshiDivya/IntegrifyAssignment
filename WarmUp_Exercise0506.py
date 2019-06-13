#!/usr/bin/env python
# coding: utf-8

# ## Program 3

# In[9]:


import numpy as np


# In[10]:


A=[-5,-3,-1,0,3,6]
A


# In[11]:


B=np.abs(A)
B


# In[12]:


set(B)


# In[13]:


len(set(B))


# ## program 1

# In[19]:



def put_no():
    return int(input("enter no between 0 to 1"))
def isvalid_no(n):
    if n > 7:
        print("Course Passed.")

    elif n < 5:
        print('The current value of n is: {}\n'.format(n))
        n += 1
        return isvalid_no(n)

    else:
        print('The current value of n is: {}\n'.format(n))
        n += 1
        return isvalid_no(n)
        
n=put_no()
isvalid_no(n)    


# ## Program Factorial

# In[21]:


def fact(n):
    if n in range(2):
        return n
    return n * fact(n - 1)

fact(int(input("Enter the no ")))


# In[22]:


a=[2,3,1,5]
a[-1]*(a[-1] + a[0]) / 2 - sum(a)


# ## Right Shift array

# In[24]:


a=[3,8,9,7,6]
np.roll(a,1)


# In[25]:


np.arange(6)


# In[33]:


A=[10,2,5,1,8,20]
A.sort()
A


# In[38]:


def demo():
    for x in range(len(A)):
        n=A[x]+A[x+1]
        if n> A[x+2]:
            return x
n=demo()
print(demo())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




