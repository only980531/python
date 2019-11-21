#!/usr/bin/env python
# coding: utf-8

# In[33]:


x=[2,8,9,9,16,56,82]
y=[1,7,7,8,10,56,85]
z=[]
for i in x:
    for j in y :
        while x[0]<=y[0]:
            z.append(x[0])
            x.pop(0)
        while x[0]>y[0]:
            z.append(y[0])
            y.pop(0)
        print(x,y,z)
        
#我先從mergesort的最後一步驟下手，我的想法是把兩個排好的隊伍合併成一個長一點的隊伍，實現方法是兩個小隊伍的第一個數字比較，小的放入長的隊伍的第一個，
#然後不斷執行這個動作，但我不會用++的寫法，所以我把每次看過的數給移除
#一開始我不知如何呼叫兩個list裡的元素，上網查後我用兩個for，但是跑出來的結果總會剩兩個數，所以我詢問同學該怎麼解決esort的最後一步 11/01

    


# In[32]:


x=[2,8,9,9,16,56,82]
y=[1,7,7,8,10,56,85]
z=[]
while len(x)>=0 and len(y)>=0:

    if x[0]<=y[0]:
        z.append(x[0])
        x.pop(0)
    else:
        z.append(y[0])
        y.pop(0)
        print(x,y,z)
        #首先他告訴我如果沒使用到i跟j的話可以用while來限制條件就好，然後下面用if跟else來寫，並發現了問題 11/01
        

    


# In[73]:


x


# In[74]:


y


# In[75]:


i


# In[2]:


x=[2,8,9,9,16,56,82]
y=[1,7,7,8,10,56,85]
z=[]
while len(x)!=0 and len(y)!=0:

    if x[0]<=y[0]:
        z.append(x[0])
        x.pop(0)
    else:
        z.append(y[0])
        y.pop(0)
   
    
z.extend(x)
z.extend(y)
x=[]
y=[]
print(z)

        
        
    #思考後我把條件從>=改成不=，這樣其中一邊會變成沒有元素，另一邊會剩1個以上的元素，原本我想:如果x沒了，就把y extennd進z，y沒了就把x extend進z
    #但我突然發現好像不用那麼麻煩，直接把兩個都extend就好了，因為其中一個會變沒有元素，加了也不會影響，這才完成了最後一步 11/01


# In[24]:


z


# In[17]:


data=[2,6,96,86,58,9,64,65,58,98,63,25,85,56,89,67]

def mergesort(data):
    for index in range(0,len(data)-1,2):
        if data[index]>data[index+1]:
            data[index], data[index+1] = data[index+1], data[index]
       
     
        
        

mergesort(data) 
data
            #開始第一步驟我的想法是每個偶數位跟下一個基數位比較，暫時可以跑出來，但有個問題是最後一個數不會被比到，因此下一步驟要再思考一下怎麼修正 11/02


# In[ ]:



while data[i]<len(data):
    x.append(data[:2**i-1])
    z.pop(data[:2**i-1])
    y.append(data[2**i-1:2**(i+1)-1])
    
    
    
    
    


# In[3]:


#後來發現，merge有兩種，一個是遞迴，一個不是，我的是不遞迴，但好像會有很多例外，所以我後面只保留合併的部分。


# In[20]:


)


# In[1]:


def merge_sort(nums):
        if len(nums) > 1:
            x = nums[:len(nums)//2]
            y = nums[len(nums)//2:]
            merge_sort(x)
            merge_sort(y)

        while len(x)>0 and len(y)>0:
            z=[]
            if x[0]<=y[0]:
                z.append(x[0])
                x.pop(0)
            else:
                z.append(y[0])
                y.pop(0)          

            z.extend(x)
            z.extend(y)

    

              
            



   


# In[1]:


nums=[5,65,98,5,36,44,82,67,89,57,46,20,15]


# In[1]:


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




