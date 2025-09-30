
import math
import random

# Objective function to minimize
def objective(x):
    return x**2 + 10 * math.sin(x)

# Simulated Annealing algorithm
def simulated_annealing(objective, bounds, temp, cooling_rate, max_iter):
    # Step 1: Initialize with a random solution
    current_x = random.uniform(bounds[0], bounds[1])
    current_energy = objective(current_x)

    # Track best solution
    best_x, best_energy = current_x, current_energy

    for i in range(max_iter):
        # Step 2: Generate new candidate solution
        new_x = current_x + random.uniform(-1, 1)
        # Keep solution inside search bounds
        new_x = max(bounds[0], min(new_x, bounds[1]))
        new_energy = objective(new_x)

        # Step 3: Calculate change in energy
        delta = new_energy - current_energy

        # Step 4: Decide whether to accept new solution
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_x, current_energy = new_x, new_energy

        # Step 5: Update best solution
        if new_energy < best_energy:
            best_x, best_energy = new_x, new_energy

        # Step 6: Decrease temperature
        temp = temp * cooling_rate

    return best_x, best_energy

# Parameters
bounds = [-10, 10]     # Search space
temp = 1000            # Initial temperature
cooling_rate = 0.95    # Cooling factor
max_iter = 1000        # Iterations

best_solution = simulated_annealing(objective, bounds, temp, cooling_rate, max_iter)
print("Best Solution: x = %.5f, f(x) = %.5f" % best_solution)
