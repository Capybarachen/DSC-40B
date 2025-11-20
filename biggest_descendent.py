#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def biggest_descendent(graph, root, value):

    best = {}

    def dfs(u):
        m = value[u]

        for v in graph.neighbors(u):
            child_best = dfs(v)
            if child_best > m:
                m = child_best

        best[u] = m 
        return m

    dfs(root)
    return best

