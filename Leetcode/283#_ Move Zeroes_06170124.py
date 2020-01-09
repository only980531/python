#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        for x in nums:
            if x != 0:
                nums[i] = x
                i += 1
            else:
                j += 1
        for y in range(j):
            nums[i+y] = 0

