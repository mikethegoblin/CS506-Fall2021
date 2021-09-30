from sim import euclidean_dist
from queue import Queue

class DBC():

    def __init__(self, dataset, min_pts, epsilon):
        self.dataset = dataset
        self.min_pts = min_pts
        self.epsilon = epsilon
        self.noise = 0


    def find_neighbors(self, idx):
        neighborhood = []
        for i in range(len(self.dataset)):
            if i == idx:
                continue
            if euclidean_dist(self.dataset[i], self.dataset[idx]) <= self.epsilon:
                neighborhood.append(i)
        return neighborhood

    def dbscan(self):
        """
            returns a list of assignments. The index of the
            assignment should match the index of the data point
            in the dataset.
        """
        assignments = [-1 for i in range(len(self.dataset))]
        # initial cluster number
        cluster = 0

        for i, point in enumerate(self.dataset):
            if assignments[i] != -1:
                continue

            found_neighbors = self.find_neighbors(i)
            # if number of neighbors is less than min_points, then mark this point as noise
            if len(found_neighbors) < self.min_pts:
                assignments[i] = self.noise
                continue

            # increment the label
            cluster += 1
            # assign current point to current cluster
            assignments[i] = cluster

            # create a queue to hold the neighbors of current point
            q = Queue()
            
            for neighbor in found_neighbors:
                q.put(neighbor)

            while not q.empty():
                cur_point_idx = q.get()

                # if this point was previously assigned as a noise point, assign it to the current cluster
                if assignments[cur_point_idx] == 0:
                    assignments[cur_point_idx] = cluster
                # if the current point already has an assignment, continue
                if assignments[cur_point_idx] != -1:
                    continue

                assignments[cur_point_idx] = cluster

                cur_neighbors = self.find_neighbors(i)
                if len(cur_neighbors) >= self.min_pts:
                    for idx in cur_neighbors:
                        if idx not in found_neighbors:
                            q.put(idx)
                            found_neighbors.append(idx)

        return assignments
