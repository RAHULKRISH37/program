
import math
import random

def objective(x):
    return x**2 + 10 * math.sin(x)


def simulated_annealing(objective, bounds, temp, cooling_rate, max_iter):
    
    current_x = random.uniform(bounds[0], bounds[1])
    current_energy = objective(current_x)


    best_x, best_energy = current_x, current_energy

    for i in range(max_iter):
        
        new_x = current_x + random.uniform(-1, 1)
        
        new_x = max(bounds[0], min(new_x, bounds[1]))
        new_energy = objective(new_x)

        
        delta = new_energy - current_energy

        
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_x, current_energy = new_x, new_energy

        
        if new_energy < best_energy:
            best_x, best_energy = new_x, new_energy

        
        temp = temp * cooling_rate

    return best_x, best_energy


bounds = [-10, 10]     
temp = 1000            
cooling_rate = 0.95   
max_iter = 1000        

best_solution = simulated_annealing(objective, bounds, temp, cooling_rate, max_iter)
print("Best Solution: x = %.5f, f(x) = %.5f" % best_solution)
