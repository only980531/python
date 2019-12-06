#!/usr/bin/env python
# coding: utf-8

# In[24]:


from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None     
        

        
class MyHashSet:
    
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity

    def add(self, key):
        h=MD5.new()
        h.update(key.encode('utf-8'))
        a=int(h.hexdigest(),16)
        x=a%self.capacity
        Node=self.data[x]
        if Node==None:
            Node=ListNode(a)
            self.data[x]=Node
        else:

            while Node.next!=None:
                Node=Node.next
            Node.next=ListNode(a)
            
                    
            
    def remove(self, key):
        h=MD5.new()
        h.update(key.encode('utf-8'))
        a=int(h.hexdigest(),16)
        x=a%self.capacity
        Node=self.data[x]
        if MyHashSet.contains(self,key)!=True:
            return False
        else:
            if Node==a:
                if Node.next==None:
                    self.data[x]=Node
                    self.data[x]=None
                else:
                    Node=Node.next
            
                
            
                
                
                
           
    def contains(self, key):
        h=MD5.new()
        h.update(key.encode('utf-8'))
        a=int(h.hexdigest(),16)
        x=a%self.capacity
        Node=self.data[x]
        if Node==None:
            return False
        else:
            while Node.val!=a:
                if Node.next==None:
                    return False
                else:
                    Node=Node.next
                
            
            return True


# In[ ]:


#自己的binary search tree https://github.com/only980531/python/blob/master/HW3/binary_search_tree_06170124.py
#https://www.youtube.com/watch?v=KyUTuwz_b7Q
#https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/
#https://ithelp.ithome.com.tw/articles/10208884

