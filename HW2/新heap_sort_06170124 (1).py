#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[16]:


data=[1,2,3,4,5,6,7,8,9,10]
z=[]
class Solution(object):
    def heap_sort(data):
        i=len(data)//2-1
        while i>=0:
            if 2*i+2 > len(data)-1:
                while data[i]<=data[2*i+1]:
                    data[i],data[2*i+1]=data[2*i+1],data[i]
                i-=1
            else:
                while data[i]<=data[2*i+1]:
                    data[i],data[2*i+1]=data[2*i+1],data[i]
                while data[i]<=data[2*i+2]:
                    data[i],data[2*i+2]=data[2*i+2],data[i]
                i-=1 
        data[0],data[-1]=data[-1],data[0]
        z.append(data[-1])
        data.pop(-1)
    while len(data)>0:
        heap_sort(data)
output = z
output


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




