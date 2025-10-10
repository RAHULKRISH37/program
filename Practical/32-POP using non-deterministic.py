import random

# Define actions as tuples: (action_name, preconditions, effects)
actions = [
    ("GetKey", [], ["HasKey"]),
    ("OpenDoor", ["HasKey"], ["DoorOpen"]),
    ("EnterRoom", ["DoorOpen"], ["InRoom"])
]

# Partial Order Plan
plan_steps = ["Start", "Finish"]
causal_links = []
ordering_constraints = [("Start", "Finish")]

# Open preconditions for "Finish" (goal)
open_preconditions = ["InRoom"]

# Non-deterministic POP procedure
while open_preconditions:
    p = open_preconditions.pop(0)  # select a precondition
    # Non-deterministically choose an action that achieves p
    candidates = [a for a in actions if p in a[2]]
    if not candidates:
        print(f"No action found to achieve {p}")
        break
    action = random.choice(candidates)
    print(f"Selected action: {action[0]} to achieve {p}")
    
    # Add action to plan
    if action[0] not in plan_steps:
        plan_steps.insert(-1, action[0])
        # Add preconditions of this action to open_preconditions
        for pre in action[1]:
            if pre not in open_preconditions:
                open_preconditions.append(pre)
        # Add causal link
        causal_links.append((action[0], p, "Finish"))
        # Add ordering constraints
        ordering_constraints.append(("Start", action[0]))
        ordering_constraints.append((action[0], "Finish"))

print("\nFinal Plan Steps (Partial Order):", plan_steps)
print("Causal Links:", causal_links)
print("Ordering Constraints:", ordering_constraints)
