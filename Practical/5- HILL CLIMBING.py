import random

# Objective function
def f(x):
    return -(x - 3) ** 2 + 9   # maximum at x=3

# Hill climbing algorithm
def hill_climbing(max_iterations=1000, step_size=0.1):
    # Start from a random point between -10 and 10
    current_x = random.uniform(-10, 10)
    current_value = f(current_x)

    for _ in range(max_iterations):
        # Generate a neighbor by moving slightly left or right
        neighbor = current_x + random.choice([-step_size, step_size])
        neighbor_value = f(neighbor)

        # If neighbor is better, move there
        if neighbor_value > current_value:
            current_x, current_value = neighbor, neighbor_value;

    return current_x, current_value

# Run the algorithm
best_x, best_value = hill_climbing()
print("Best solution found:")
print("x =", round(best_x, 4))
print("f(x) =", round(best_value, 4))
