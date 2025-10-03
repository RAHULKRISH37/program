import random

def f(x):
    return -(x - 3) ** 2 + 9   


def hill_climbing(max_iterations=1000, step_size=0.1):
    
    current_x = random.uniform(-10, 10)
    current_value = f(current_x)

    for _ in range(max_iterations):
        
        neighbor = current_x + random.choice([-step_size, step_size])
        neighbor_value = f(neighbor)

        
        if neighbor_value > current_value:
            current_x, current_value = neighbor, neighbor_value;

    return current_x, current_value


best_x, best_value = hill_climbing()
print("Best solution found:")
print("x =", round(best_x, 4))
print("f(x) =", round(best_value, 4))
