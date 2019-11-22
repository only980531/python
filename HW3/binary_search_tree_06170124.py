#!/usr/bin/env python
# coding: utf-8

# In[2]:


class TreeNode(object):
    def _init_(self,x):
        self.val=val
        self.left=None
        self.right=None
        
class Solution(object):
    def insert(self,root,val):
        if val >=self.root.val:
            if self.root.right==None:
                self.root.val=val
            else:
                Solution.insert(self.root.right,val)
        else:
            if self.root.left==None:
                self.root.left=val
            else:
                Solution().insert(self.root.left,val)
                
    def search(self,root,target):
        if self.root!=None:
            if self.root.val==target:
                return root
            elif self.root.val<target:
                Solution().search(self.root.left,target)
            else:
                Solution().search(self.root.right,target)
        else:
            return False
        
    def delete(seif root.target):
        if self.root!=None:
            if self.root.val==target:
                

        else:
            return self.root
            
            


# In[ ]:




