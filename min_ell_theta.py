#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def learn_theta(data, colors):
    max_blue = float('-inf')
    min_red = float('inf')

    for x, c in zip(data, colors):
        if c == 'blue':
            if x > max_blue:
                max_blue = x
        else:  # red
            if x < min_red:
                min_red = x

    return 0.5 * (max_blue + min_red)


def compute_ell(data, colors, theta):
    loss = 0

    for x, c in zip(data, colors):
        if c == 'red' and x <= theta:
            loss += 1
        elif c == 'blue' and x > theta:
            loss += 1

    return float(loss)


def minimize_ell(data, colors):
    best_theta = data[0]
    best_loss = compute_ell(data, colors, best_theta)

    for theta in data:
        loss = compute_ell(data, colors, theta)
        if loss < best_loss:
            best_loss = loss
            best_theta = theta

    return best_theta


def minimize_ell_sorted(data, colors):
    n = len(data)

    total_blue = 0
    for c in colors:
        if c == 'blue':
            total_blue += 1

    red_leq_theta = 0
    blue_gt_theta = total_blue

    best_loss = red_leq_theta + blue_gt_theta
    best_theta = data[0] - 1.0

    for alpha in range(1, n + 1):
        if colors[alpha - 1] == 'red':
            red_leq_theta += 1
        else:
            blue_gt_theta -= 1

        if alpha < n:
            theta = 0.5 * (data[alpha - 1] + data[alpha])
        else:
            theta = data[-1] + 1.0

        loss = red_leq_theta + blue_gt_theta
        if loss < best_loss:
            best_loss = loss
            best_theta = theta

    return best_theta

