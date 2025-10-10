import numpy as np
import random

# Maze environment
# 0 = free cell, -1 = wall, 1 = goal
maze = np.array([
    [0, 0, 0, 0, 1],
    [0, -1, -1, 0, -1],
    [0, 0, 0, 0, 0],
    [0, -1, 0, -1, 0],
    [0, 0, 0, 0, 0]
])

# Q-table initialization
states = [(i, j) for i in range(maze.shape[0]) for j in range(maze.shape[1])]
actions = ['up', 'down', 'left', 'right']
Q = {(s, a): 0 for s in states for a in actions}

# Parameters
alpha = 0.1      # learning rate
gamma = 0.9      # discount factor
epsilon = 0.2    # exploration rate
episodes = 1000

# Helper functions
def is_valid(pos):
    i, j = pos
    return 0 <= i < maze.shape[0] and 0 <= j < maze.shape[1] and maze[i, j] != -1

def step(state, action):
    i, j = state
    if action == 'up':
        i -= 1
    elif action == 'down':
        i += 1
    elif action == 'left':
        j -= 1
    elif action == 'right':
        j += 1
    next_state = (i, j)
    if not is_valid(next_state):
        next_state = state  # stay in same place if invalid
    reward = 1 if maze[next_state] == 1 else -0.01  # small penalty each step
    return next_state, reward

# Q-Learning
for episode in range(episodes):
    state = (4, 0)  # start position
    while maze[state] != 1:
        # ε-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = random.choice(actions)
        else:
            q_values = [Q[(state, a)] for a in actions]
            action = actions[np.argmax(q_values)]
        
        next_state, reward = step(state, action)
        # Q-value update
        Q[(state, action)] += alpha * (reward + gamma * max(Q[(next_state, a)] for a in actions) - Q[(state, action)])
        state = next_state

# Test learned policy
state = (4, 0)
path = [state]
while maze[state] != 1:
    q_values = [Q[(state, a)] for a in actions]
    action = actions[np.argmax(q_values)]
    next_state, _ = step(state, action)
    path.append(next_state)
    state = next_state

print("Learned path from start to goal:")
print(path)
