% Prolog Program to implement Best-First Search Algorithm

% --- Facts: Graph edges ---
edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 1).
edge(b, e, 4).
edge(c, f, 1).
edge(d, goal, 1).
edge(e, goal, 1).
edge(f, goal, 1).

% --- Facts: Heuristic values (h(n)) ---
heuristic(a, 5).
heuristic(b, 4).
heuristic(c, 2).
heuristic(d, 2).
heuristic(e, 3).
heuristic(f, 1).
heuristic(goal, 0).

% --- Best-First Search ---
best_first_search(Start, Goal, Path
