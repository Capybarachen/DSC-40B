#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def learn_theta(data, colors):
    max_blue = None
    for i in range(len(data)):
        if colors[i] == 'blue':
            if max_blue is None or data[i] > max_blue:
                max_blue = data[i]
    return max_blue


def compute_ell(data, colors, theta):
    loss = 0
    for i in range(len(data)):
        x = data[i]
        c = colors[i]
        if c == 'red':
            if x <= theta:
                loss = loss + 1
        else:
            if x > theta:
                loss = loss + 1
    return float(loss)


def minimize_ell(data, colors):
    best_theta = data[0]
    best_loss = compute_ell(data, colors, best_theta)
    for i in range(len(data)):
        theta = data[i]
        loss = compute_ell(data, colors, theta)
        if loss < best_loss:
            best_loss = loss
            best_theta = theta
    return float(best_theta)


def minimize_ell_sorted(data, colors):
    n = len(data)

    total_blue = 0
    for i in range(n):
        if colors[i] == 'blue':
            total_blue = total_blue + 1

    red_leq_theta = 0
    blue_gt_theta = total_blue

    best_loss = red_leq_theta + blue_gt_theta
    best_theta = data[0] - 1.0

    for alpha in range(1, n + 1):
        if colors[alpha - 1] == 'red':
            red_leq_theta = red_leq_theta + 1
        else:
            blue_gt_theta = blue_gt_theta - 1

        theta = data[alpha - 1]
        loss = red_leq_theta + blue_gt_theta

        if loss < best_loss:
            best_loss = loss
            best_theta = theta

    return float(best_theta)
