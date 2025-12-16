#file name: dbscan_alghoritm
from math import sqrt


class My_DBSCAN:

    def __init__(self, eps=0.5, min_samples=5):
        if eps <= 0:
            raise ValueError("eps must be > 0")
        if min_samples <= 0:
            raise ValueError("min_samples must be > 0")

        self.eps = eps
        self.min_samples = min_samples
        self.labels = []
        self.n_clusters = 0

    def distance(self, p, q):
        if len(p) != len(q):
            raise ValueError("Points must have the same length")

        suma = 0.0
        for i in range(len(p)):
            diff = p[i] - q[i]
            suma += diff * diff
        return sqrt(suma)       #eucledis distance

    def region_query(self, X, index):
        neighbors = []
        for j in range(len(X)):
            if self.distance(X[index], X[j]) <= self.eps:
                neighbors.append(j)
        return neighbors

    def expand_cluster(self, X, start_index, neighbors, cluster_id, visited):
        self.labels[start_index] = cluster_id #start point must be core point

        queue = list(neighbors)

        while queue:
            current = queue.pop(0)  # FIFO queue

            if not visited[current]:
                visited[current] = True
                current_neighbors = self.region_query(X, current)


                if len(current_neighbors) >= self.min_samples: #if current point is core point
                    for n in current_neighbors:     #add to queue the neighbourhood of this point (expand cluster)
                        if n not in queue:
                            queue.append(n)

            if self.labels[current] == 0:       #add label
                self.labels[current] = cluster_id

    def fit(self, X):
        if not X:
            raise ValueError("X cannot be empty")

        n = len(X)
        self.labels = [0] * n      # 0 = brak klastra
        visited = [False] * n
        cluster_id = 0

        for i in range(n):
            if visited[i]:
                continue

            visited[i] = True
            neighbors = self.region_query(X, i)

            # noise
            if len(neighbors) < self.min_samples:
                self.labels[i] = -1
            else:
                # new cluster, i-point is core point
                cluster_id += 1
                self.expand_cluster(X, i, neighbors, cluster_id, visited)

        self.n_clusters = cluster_id
        return self

    def fit_predict(self, X):
        self.fit(X)
        return self.labels
