from collections import defaultdict
from math import inf
import random
import csv
from .sim import euclidean_dist


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    # a list to hold the mean of each column in the dataset, this will be the returned value
    column_means = []
    n = len(points)
    for col in range(len(points[0])):
        total = 0
        for row in range(len(points)):
            total += points[row][col]
        column_means.append(total / n)
    return column_means


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    clusters = list(set(assignments))
    clusters.sort()
    centers = []

    for c in clusters:
        # a list to hold the points in current cluster
        points_in_cluster = []
        for i in range(len(dataset)):
            if assignments[i] == c:
                points_in_cluster.append(dataset[i])
        centers.append(point_avg(points_in_cluster))
    
    return centers


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    return euclidean_dist(a, b)

def distance_squared(a, b):
    return distance(a, b) ** 2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    indexes = [*range(len(dataset))]
    # randomly shuffles the indexes
    random.shuffle(indexes)
    # get the first k indices
    k_points = indexes[ :k]
    initial_points = []
    for idx in k_points:
        initial_points.append(dataset[idx])
    return initial_points

def cost_function(clustering):
    '''
    returns the kmeans cost function
    input clustering is a defaultdict
    '''
    sum_of_squares = 0
    for cluster in clustering.values():
        mean = point_avg(cluster)
        for point in cluster:
            sum_of_squares += distance_squared(point, mean)
    return sum_of_squares

def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    centers = []
    # randomly select a first centroid
    centers.append(dataset[random.randint(0, len(dataset) - 1)])

    # select the next k-1 centers
    for c in range(k - 1):
        dist = []
        for point in dataset:
            smallest_d = inf
            # find the distance between the current data point and the nearest chosen centroid
            for centroid in centers:
                smallest_d = min(smallest_d, distance(point, centroid))
            dist.append(smallest_d ** 2)
        next_center_idx = get_point_from_rand(dist)
        centers.append(dataset[next_center_idx])
    return centers
        
def get_point_from_rand(dist):
    '''
    choose a random point with probability proportional to the values in dist
    '''
    total = sum(dist)
    rand_num = random.randint(0, total)
    threshold = 0
    result = -1
    for i, val in enumerate(dist):
        threshold += val
        if rand_num <= threshold:
            result = i
            break
    return result
        


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
