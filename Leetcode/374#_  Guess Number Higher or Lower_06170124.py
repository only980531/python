#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        h = n
        while l<= h:
            m = l +(h - l)//2
            g = guess(m)
            if g == 0:
                return m
            if g == -1:
                h = m- 1
            else:
                l = m +1
        return -1

