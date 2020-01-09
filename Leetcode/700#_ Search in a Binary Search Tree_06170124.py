#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root!=None:
            if root.val==val:
                return root
            elif root.val<val:
                return Solution.searchBST(self,root.right,val)
            else:
                return Solution.searchBST(self,root.left,val)
        else:
            return NULL
        

