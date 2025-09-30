import random

# Distance of route
def route_distance(route, dist):
    return sum(dist[route[i]][route[(i+1)%len(route)]] for i in range(len(route)))

# Fitness
def fitness(route, dist):
    return 1 / route_distance(route, dist)

# Initial population
def init_pop(size, n):
    pop = []
    base = list(range(n))
    for _ in range(size):
        r = base[:]
        random.shuffle(r)
        pop.append(r)
    return pop

# Selection (pick best of 2)
def select(pop, dist):
    return min(random.sample(pop, 2), key=lambda r: route_distance(r, dist))

# Crossover (simple)
def crossover(p1, p2):
    cut = random.randint(0, len(p1)-1)
    child = p1[:cut] + [c for c in p2 if c not in p1[:cut]]
    return child

# Mutation (swap)
def mutate(route, rate=0.1):
    if random.random() < rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]
    return route

# GA for TSP
def ga_tsp(dist, pop_size=6, gens=10):
    n = len(dist)
    pop = init_pop(pop_size, n)
    best = min(pop, key=lambda r: route_distance(r, dist))
    best_dist = route_distance(best, dist)

    for g in range(gens):
        new_pop = []
        for _ in range(pop_size):
            p1, p2 = select(pop, dist), select(pop, dist)
            child = mutate(crossover(p1, p2))
            new_pop.append(child)
        pop = new_pop
        cur = min(pop, key=lambda r: route_distance(r, dist))
        cur_dist = route_distance(cur, dist)
        if cur_dist < best_dist:
            best, best_dist = cur, cur_dist
        print(f"Gen {g+1}: Best Distance = {best_dist}")
    return best, best_dist

# Example with 4 cities
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_route, best_distance = ga_tsp(dist_matrix)
print("\nBest Route:", best_route)
print("Best Distance:", best_distance)