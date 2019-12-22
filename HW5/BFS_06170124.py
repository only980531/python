#!/usr/bin/env python
# coding: utf-8

# In[7]:


from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self,s):
        queue=[s]
        data=[]
       
        while len(queue)>0:
            if queue[0]  not in data:
                queue.extend(self.graph[queue[0]])
                data.append(queue[0])
                queue.pop(0)
            else:
                queue.pop(0)
        return(data)  
    def DFS(self,s):
        queue=[s]
        data=[]
       
        while len(queue)>0:
            if queue[-1]  not in data:
                data.append(queue[-1])
                queue.pop(-1)
                queue.extend(self.graph[data[-1]])
               
            else:
                queue.pop(-1)
        return(data)  
    
    


# 同學教我我觀念以及
# https://www.youtube.com/watch?v=pcKY4hjDrxk&t=31s

# In[ ]:




