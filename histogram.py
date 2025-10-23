#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def histogram(points, bins):
    n = len(points)
    k = len(bins)

    counts = [0] * k
    i = 0  
    j = 0 

    while i < n and j < k:
        a = bins[j][0]
        b = bins[j][1]
        x = points[i]

        if x < a:
            i += 1                 
        elif x >= b:
            j += 1                 
        else:
            counts[j] += 1         
            i += 1

    densities = []
    idx = 0
    while idx < k:
        a = bins[idx][0]
        b = bins[idx][1]
        width = b - a
        densities.append(counts[idx] / (n * width))
        idx += 1

    return densities

