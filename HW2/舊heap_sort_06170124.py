#!/usr/bin/env python
# coding: utf-8

# In[13]:


data=[1,2,3,4,5,6,7,8,9,10]
z=[]
def heapsort(data):
    i=len(data)//2-1#配合電腦沒電那張圖片使用，我先假設有腳的位置叫i，右腳在計算過後便是2i+2，左腳是2i-1
    while i>=0:#我把最後一個有腳的點的位置設為初始的，然後往前-1到變成第0位，因為第0位是最後一個有角的位置#這一步我卡超久，因為有時候沒有右腳會out of index
        if 2*i+2 > len(data)-1:#這一步我卡超久，我原本沒有設這個if，因為沒考慮到(圖片)，結果，所以我有時候沒有右腳會list is out of index，
            while data[i]<=data[2*i+1]:#所以我多加了如果只有左腳的狀況，試了幾個限制條件結果不行，剛剛看著圖用假設的方式試這個方法，結果成功了，怎麼假設可以當面回答#
                data[i],data[2*i+1]=data[2*i+1],data[i]
            i-=1
        else:
            while data[i]<=data[2*i+1]:    #如果左腳或右腳大於上面就交換位置
                data[i],data[2*i+1]=data[2*i+1],data[i]
            while data[i]<=data[2*i+2]:
                data[i],data[2*i+2]=data[2*i+2],data[i]
            i-=1 
    data[0],data[-1]=data[-1],data[0] #換到最後最大的數會在第1個，我把它跟最後一位交換，再把它放入z，原本想先移出第1位，但感覺把最後一位放到第1位在移掉更麻煩。          #
    z.append(data[-1])          
    data.pop(-1)
while len(data)>0: #然後重複移出最大的數，此時data持續變小，Z持續變大   #終於完成了!!! ，然後
    heapsort(data)
print(data)
z   #終於完成了!!! ，然後改成作業統一的格式，下面那格


# In[10]:


class Solution(object):
    def heapsort(data):
        z=[]
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
        heapsort(data)
        
data=[1,2,3,4,5,6,7,8,9,10]
output = z
output


# In[ ]:





# In[26]:


def heapsort(data):
    i=len(data)//2-1
    while i>=0:
        
   
      
            while data[i]<=data[2*i+1]:
                data[i],data[2*i+1]=data[2*i+1],data[i]
            
            if 2*i+2!=range(len(data)):
                i-=1
                continue
            while data[i]<=data[2*i+2]:
                data[i],data[2*i+2]=data[2*i+2],data[i]
                i-=1
                
            
heapsort(data)
print(data)


# In[7]:


def heapsort(data):
    i=len(data)//2-1
    while i>=0:
        if 2*i+2==range(len(data)-1):
            while data[i]<=data[2*i+1]:
                data[i],data[2*i+1]=data[2*i+1],data[i]
            while data[i]<=data[2*i+2]:
                data[i],data[2*i+2]=data[2*i+2],data[i]
            i-=1 
          
        else:
              while data[i]<=data[2*i+1]:
                data[i],data[2*i+1]=data[2*i+1],data[i]
                i-=1
            
           
heapsort(data)
print(data)


# In[5]:


12==len(data)-1


# In[ ]:


def heapsort(data):
    i=len(data)//2-1
    while i>=0:
        if 2*i+2!=range(len(data)):
            while data[i]<=data[2*i+1]:
                data[i],data[2*i+1]=data[2*i+1],data[i]
                i-=1
        else:
            while data[i]<=data[2*i+1]:
                data[i],data[2*i+1]=data[2*i+1],data[i]
            while data[i]<=data[2*i+2]:
                data[i],data[2*i+2]=data[2*i+2],data[i]
            i-=1
heapsort(data)
print(data)

