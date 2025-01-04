from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False

def findCriticalAndPseudoCriticalEdges(n: int, roads: List[List[int]]) -> List[int]:
    edges = [(a, b, distance, i) for i, (a, b, distance) in enumerate(roads)]
    edges.sort(key=lambda x: x[2])  # Sort by weight
    
    def kruskal(exclude_edge=-1, include_edge=-1):
        uf = UnionFind(n)
        weight = 0
        edges_used = 0
        
        # Include an edge if specified
        if include_edge != -1:
            a, b, w, _ = edges[include_edge]
            if uf.union(a, b):
                weight += w
                edges_used += 1

        for i, (a, b, w, _) in enumerate(edges):
            if i == exclude_edge:
                continue
            if uf.union(a, b):
                weight += w
                edges_used += 1

        # Check if all nodes are connected (n - 1 edges used in the MST)
        return weight if edges_used == n - 1 else float('inf')

    # Find MST weight
    mst_weight = kruskal()

    critical, pseudo_critical = [], []
    for i in range(len(edges)):
        # Check if it's a critical edge
        if kruskal(exclude_edge=i) > mst_weight:
            critical.append(edges[i][3])
        # Check if it's a pseudo-critical edge
        elif kruskal(include_edge=i) == mst_weight:
            pseudo_critical.append(edges[i][3])

    return [len(critical), len(pseudo_critical)]

# Example usage
n = 5
roads = [
    [0, 1, 1],
    [0, 2, 2],
    [1, 2, 3],
    [1, 3, 4],
    [3, 4, 5]
]
print(findCriticalAndPseudoCriticalEdges(n, roads))
