#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[32]:





# In[73]:





# In[74]:





# In[75]:





# In[2]:





# In[24]:





# In[17]:



    


# In[ ]:



    
    
    
    


# In[3]:





# In[20]:





# In[1]:





# In[1]:





# In[3]:


class Solution(object):   
    def merge_sort(self,nums):
        if len(nums)<=1:
            return nums
        if len(nums) > 1:
                x = nums[:len(nums)//2] #x為nums的前一半
                y = nums[len(nums)//2:] #y為nums的後一半
                
                Solution().merge_sort(x)  #對已分割的x，y再重複進行對半的分割
                Solution().merge_sort(y)
                
                return Solution().merge(Solution().merge_sort(x),Solution().merge_sort(y)) #把x,y回傳到merge
                
    def merge(self,x,y):          
            z=[]
            while len(x)>0 and len(y)>0:#最上面有解釋
                if x[0]<=y[0]:
                    z.append(x[0])
                    x.pop(0)
                elif x[0]>y[0]:
                    z.append(y[0])
                    y.pop(0)

            z.extend(x[:])
            z.extend(y[:])
            return z
        
nums = [85,65,95,6,35,2,65,86]
output = Solution().merge_sort(nums)
output


# In[6]:





# In[ ]:




