#!/usr/bin/env python
# coding: utf-8

# In[2]:


def mode(numbers):
    
    if not numbers:
        return None
    
    freq = {}        
    max_item = None
    max_freq = 0

    for x in numbers:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

        if freq[x] > max_freq:
            max_freq = freq[x]
            max_item = x

    return max_item


# In[ ]:




