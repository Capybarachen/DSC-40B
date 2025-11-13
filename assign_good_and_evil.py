#!/usr/bin/env python
# coding: utf-8

# In[5]:


def assign_good_and_evil(graph):
    labels = {}

    for start in graph.nodes:
        if start in labels:
            continue

        labels[start] = 'good'
        queue = [start]

        while len(queue) > 0:
            current = queue[0]
            del queue[0]

            for neighbor in graph.neighbors(current):
                if neighbor not in labels:
                    if labels[current] == 'good':
                        labels[neighbor] = 'evil'
                    else:
                        labels[neighbor] = 'good'
                    queue.append(neighbor)
                else:
                    if labels[neighbor] == labels[current]:
                        return None

    return labels


# In[ ]:




