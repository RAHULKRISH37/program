from itertools import permutations

def travelling_salesman_brute_force(graph, start):
    n = len(graph)
    cities = list(range(n))

    cities.remove(start)

    min_path = float("inf")
    best_route = []

    for perm in permutations(cities):
        current_path = [start] + list(perm) + [start]
        current_cost = 0

        for i in range(len(current_path) - 1):
            current_cost += graph[current_path[i]][current_path[i+1]]

        if current_cost < min_path:
            min_path = current_cost
            best_route = current_path

    return best_route, min_path


# Example: Distance Matrix (Graph)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 40, 0]
]

best_route, min_cost = travelling_salesman_brute_force(graph, 0)
print("Best Route:", best_route)
print("Minimum Cost:", min_cost)
