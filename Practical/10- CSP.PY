variables = ['A', 'B', 'C', 'D']
domains = {v: ['Red', 'Green', 'Blue'] for v in variables}

constraints = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

def is_safe(var, value, assignment):
    for neighbor in constraints[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True

def backtrack(assignment={}):
    if len(assignment) == len(variables):
        return assignment
    
    unassigned = [v for v in variables if v not in assignment][0]
    for value in domains[unassigned]:
        if is_safe(unassigned, value, assignment):
            assignment[unassigned] = value
            result = backtrack(assignment)
            if result:
                return result
            assignment.pop(unassigned)
    return None

solution = backtrack()
print("Solution:", solution)