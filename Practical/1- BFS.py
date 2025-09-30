
from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    
    def BFS(self, start):
        visited = set()          # To track visited nodes
        queue = deque([start])   # Queue initialized with start node
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")  # Process the node

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Example usage
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("BFS starting from node 2:")
g.BFS(2)