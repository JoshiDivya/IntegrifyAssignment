#!/usr/bin/env python
# coding: utf-8

# ## list 

# In[25]:


list1= [1,2,3,4,5,6,7,8,9]
list1[4]


# In[26]:


list1[-4]


# In[27]:


list1[1::2]


# In[28]:


list1[3:6]


# ## Dictionary

# In[29]:


dict1={'foo': {'name': 'Foo', 'lastname': 'Fooer'}, 'bar': {'name': 'Bar', 'lastname': 'Baer'}, 'Baz': None}


# In[30]:


for x in dict1:
    print(x)


# In[31]:


print("Firstname is {} and lastname is {}".format(dict1['bar']['name'],dict1['bar']['lastname']))


# In[38]:


for x,y in dict1.items():
    if dict1[x]!=None:
        print("Firstname is {} and lastname is {}".format(y['name'],y['lastname']))


# ## Function

# In[56]:


def summer(a,*bs):
    c=0
    for b in bs:
        if b<0:
            True
        c=c+b
    if True:
        return -(a+c)
print(summer(34,5,4,-5,3))


# ## list2

# In[65]:


list2=['python', 'and', 'data', 'science', 'is', 'awesome']
newList=[a for a in list2 if len(a)>5]
newList


# In[66]:


dict2={k: v for k, v in enumerate(list2)}
dict2


# In[77]:


dict2[len(dict2)]='!'
dict2


# ## decending order

# In[88]:


list3=['x', -0.1, 'foo', True, 'bar', 10, 1.1, '8', 5, None, 12]
list3 = [x for x in list3 if type(x) == int]
list3.sort(reverse=True)
list3


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





# In[ ]:





# In[ ]:




