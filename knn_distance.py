#!/usr/bin/env python
# coding: utf-8

# In[12]:


import random

def knn_distance(arr, q, k):
    pairs = [(abs(x - q), x) for x in arr]
    target = k - 1

    def partition(start, end, p):
        pivot_dist = pairs[p][0]
        pairs[p], pairs[end] = pairs[end], pairs[p]
        store = start
        for i in range(start, end):
            if pairs[i][0] < pivot_dist:
                pairs[store], pairs[i] = pairs[i], pairs[store]
                store += 1
        pairs[store], pairs[end] = pairs[end], pairs[store]
        return store

    def quickselect(start, end, idx):
        while start < end:
            p = random.randint(start, end)
            p = partition(start, end, p)
            if idx == p:
                return
            if idx < p:
                end = p - 1
            else:
                start = p + 1

    quickselect(0, len(pairs) - 1, target)
    return pairs[target]

