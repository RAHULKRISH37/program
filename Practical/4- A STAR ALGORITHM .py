import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position  
        self.parent = parent
        self.g = 0  
        self.h = 0  
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f 

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    goal_node = Node(goal)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.position == goal:
            
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.position)

        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_pos = (current_node.position[0] + dx, current_node.position[1] + dy)

            
            if not (0 <= neighbor_pos[0] < len(grid) and 0 <= neighbor_pos[1] < len(grid[0])):
                continue
            
            if grid[neighbor_pos[0]][neighbor_pos[1]] == 1:
                continue
            
            if neighbor_pos in closed_set:
                continue

            neighbor_node = Node(neighbor_pos, current_node)
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_pos, goal)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            
            if any(n.position == neighbor_node.position and n.f <= neighbor_node.f for n in open_list):
                continue

            heapq.heappush(open_list, neighbor_node)

    return None  


grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(grid, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found.")
