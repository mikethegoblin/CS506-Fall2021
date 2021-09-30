def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    # if x is empty, then return 0 immediately
    if x == [] or y == []:
        return 0
    n = len(x)
    intersection = 0
    for i in range(n):
        if x[i] == y[i]:
            intersection += 1
    return 1 - intersection / n

def cosine_sim(x, y):
    if x == [] or y == []:
        return 0
    x_norm, y_norm = 0, 0
    dot_product = 0
    for i in range(len(x)):
        x_norm += x[i]**2
        y_norm += y[i]**2
        dot_product += x[i] * y[i]
    x_norm, y_norm = x_norm**0.5, y_norm**0.5
    # add this case to avoid zero division error
    if x_norm == 0 or y_norm == 0:
        return 0
    return dot_product / (x_norm * y_norm)

# Feel free to add more
