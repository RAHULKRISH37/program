import gymnasium as gym
import numpy as np

env = gym.make("FrozenLake-v1", is_slippery=False)
Q = np.zeros((env.observation_space.n, env.action_space.n))
alpha, gamma, eps = 0.8, 0.95, 0.1

for _ in range(5000):
    s, _ = env.reset()
    done = False
    while not done:
        a = np.argmax(Q[s]) if np.random.rand() > eps else env.action_space.sample()
        s2, r, done, _, _ = env.step(a)
        Q[s,a] += alpha * (r + gamma * np.max(Q[s2]) - Q[s,a])
        s = s2

print("Learned Q-table:\n", np.round(Q,2))

