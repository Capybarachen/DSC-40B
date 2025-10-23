#!/usr/bin/env python
# coding: utf-8

# In[1]:


def swap_sum(A, B):
    SA = sum(A)
    SB = sum(B)
    diff = SB - SA - 10

    if diff % 2 != 0:
        return None
    delta = diff // 2 

    i = 0
    j = 0
    nA = len(A)
    nB = len(B)

    while i < nA and j < nB:
        cur = B[j] - A[i]
        if cur == delta:
            return (i, j)
        elif cur < delta:
            j += 1
        else:
            i += 1

    return None


# In[ ]:




