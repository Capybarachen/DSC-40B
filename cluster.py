#!/usr/bin/env python
# coding: utf-8

# In[1]:


def cluster(graph, weights, level):
    visited_nodes = set()
    all_clusters = []

    for start_node in graph.nodes:
        if start_node in visited_nodes:
            continue

        nodes_to_visit = [start_node]
        visited_nodes.add(start_node)
        current_cluster_nodes = set()

        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            current_cluster_nodes.add(current_node)

            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited_nodes and weights(current_node, neighbor) >= level:
                    visited_nodes.add(neighbor)
                    nodes_to_visit.append(neighbor)

        all_clusters.append(frozenset(current_cluster_nodes))

    return frozenset(all_clusters)

