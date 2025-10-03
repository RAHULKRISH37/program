from collections import deque

def water_jug_bfs(m, n, d):
    visited = set()
    queue = deque()
    
    
    queue.append((0, 0))
    visited.add((0, 0))
    
    while queue:
        a, b = queue.popleft()
        print(f"Jug1: {a}, Jug2: {b}")
        
        
        if a == d or b == d:
            print("Target achieved!")
            return True
        
        
        next_states = [
            (m, b),   # Fill Jug1
            (a, n),   # Fill Jug2
            (0, b),   # Empty Jug1
            (a, 0),   # Empty Jug2
            # Pour Jug1 -> Jug2
            (a - min(a, n - b), b + min(a, n - b)),
            # Pour Jug2 -> Jug1
            (a + min(b, m - a), b - min(b, m - a))
        ]
        
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
    
    print("No solution possible.")
    return False



water_jug_bfs(4, 3, 2)