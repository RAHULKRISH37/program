import random


size = 4


wumpus = (random.randint(0, size-1), random.randint(0, size-1))
pit = (random.randint(0, size-1), random.randint(0, size-1))
gold = (random.randint(0, size-1), random.randint(0, size-1))
agent = (0, 0)  # start position


while len({wumpus, pit, gold, agent}) < 4:
    wumpus = (random.randint(0, size-1), random.randint(0, size-1))
    pit = (random.randint(0, size-1), random.randint(0, size-1))
    gold = (random.randint(0, size-1), random.randint(0, size-1))

print("=== WUMPUS WORLD GAME ===")
print("Agent starts at (0, 0)\n")


moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]


for step in range(10):
    move = random.choice(moves)
    new_x = max(0, min(size-1, agent[0] + move[0]))
    new_y = max(0, min(size-1, agent[1] + move[1]))
    agent = (new_x, new_y)

    print(f"Step {step+1}: Agent moved to {agent}")

    if agent == wumpus:
        print("💀 Agent was eaten by the Wumpus! Game Over.")
        break
    elif agent == pit:
        print("☠️ Agent fell into a Pit! Game Over.")
        break
    elif agent == gold:
        print("🏆 Agent found the Gold! You Win!")
        break
else:
    print("😐 Agent wandered around but found nothing...")

print("\nWumpus:", wumpus, "| Pit:", pit, "| Gold:", gold)
