#!/usr/bin/env python
# coding: utf-8

# In[13]:


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
        
    def delete(self,root,target):
        if root!=None:
            if root.val==target:
                if root.left==None and root.right==None:
                    root=None
                elif root.left!=None and root.right==None:
                    root=root.left
                elif root.left==None and root.right!=None:
                    root=root.right
                
            elif root.val<target:
                Solution.delete(self,root.left,target)
            else:
                Solution.delete(self,root.right,target)
        else:
            return None


# In[14]:


root = TreeNode(5)
root.left = TreeNode(3)  
root.left.left = TreeNode(3) 
root.left.left.left = TreeNode(-5) 
root.right = TreeNode(8)
root.right.left = TreeNode(7) 
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(10)


# In[15]:


print(Solution().insert(root,4)==root.left.right)


# In[16]:


print(Solution().search(root,10)==root.right.right)


# In[ ]:




