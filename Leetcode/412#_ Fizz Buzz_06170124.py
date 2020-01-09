#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        data = []
        x = ""
        for i in range(1, n + 1): 
            x = str(i)
            if i % 3 == 0:
                x = "Fizz"
            if i % 5 == 0:
                x = "Buzz"
            if i % 3 == 0 and i % 5 == 0:
                x = "FizzBuzz"
            data.append(x)
        return data

