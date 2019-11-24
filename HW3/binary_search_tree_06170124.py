#!/usr/bin/env python
# coding: utf-8

# In[68]:


class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
       
        
class Solution(object):
    def insert(self,root,val):
        if root!=None:
            if val >root.val:
                if root.right==None:
                    root.right=TreeNode(val)
                    return root.right
                else:
                    root.right=Solution.insert(self,root.right,val)
                
            else:
                if root.left==None:
                    root.left=TreeNode(val)
                    return root.left
                else:
                    root.left=Solution.insert(self,root.left,val)
        else:
            root=TreeNode(val)
            return root
                
    def search(self,root,target):
        if root!=None:
            if root.val==target:
                return root
            elif root.val<target:
                return Solution.search(self,root.right,target)
            else:
                return Solution.search(self,root.left,target)
        else:
            return None
    def Max(self,root):
        while root.right:
            return Solution.Max(self,root.left)
        while root.left:
            return root
        
    def delete(self,root,target):
        if root!=None:
            if root.val==target:
                if root.left==None and root.right==None:
                    root=None
                elif root.left!=None and root.right==None:
                    root=root.left
                elif root.left==None and root.right!=None:
                    root=root.right
                else:
                    root=Solution.Max(self,root)
                    
                    
                
            elif root.val<target:
                Solution.delete(self,root.right,target)
            else:
                Solution.delete(self,root.left,target)
        else:
            return None
        
    def modify(self,root,target,new_val):
        root = Solution.delete(self,root,target)
        Solution.insert(self,root,new_val)
        return root


# In[ ]:





# In[ ]:





# In[65]:





# In[66]:





# In[67]:





# In[ ]:




