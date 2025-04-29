# Kruskal's Algorithm in Python with letter-based vertices

# Disjoint Set (Union-Find) data structure
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Kruskal's algorithm to find MST with letter-based vertices
def kruskal(vertices, edges):
    # Mapping vertices (letters) to indices
    vertex_map = {v: i for i, v in enumerate(vertices)}
    
    mst = []
    # Step 1: Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Step 2: Initialize Disjoint Set
    dsu = DisjointSet(len(vertices))
    
    # Step 3: Iterate through edges and apply union-find
    for u, v, weight in edges:
        # Map letters to indices
        u_index = vertex_map[u]
        v_index = vertex_map[v]
        
        # Step 4: Check if adding this edge creates a cycle
        if dsu.find(u_index) != dsu.find(v_index):
            mst.append((u, v, weight))
            dsu.union(u_index, v_index)
    
    return mst

# Example usage
if __name__ == "__main__":
    # Lista de nos
    vertices = ['a', 'b', 'c', 'd', 'e', 'p']
    
    # lista de arestas no formatadas como (no, no, peso)
    edges = [
        ('a', 'b', 7),
        ('a', 'c', 6),
        ('b', 'c', 4),
        ('b', 'd', 4),
        ('b', 'e', 3),
        ('c', 'd', 4),
        ('c', 'e', 3),
        ('d', 'e', 3),
        ('d', 'p', 7),
        ('e', 'p', 2)
    ]

    #roda o algoritimo e atribui a arvore a MST
    mst = kruskal(vertices, edges)
    #printa o resultado percorrendo a arvore
    print("Edges in the Minimum Spanning Tree:")
    result = 0
    for u, v, weight in mst:
        result += weight
        print(f"({u}, {v}) with weight {weight}")
    print(result)
