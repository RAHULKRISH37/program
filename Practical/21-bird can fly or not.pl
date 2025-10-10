% Prolog Program to check if a particular bird can fly or not

% Facts
bird(canary).
bird(eagle).
bird(pigeon).
bird(parrot).
bird(penguin).
bird(ostrich).

can_fly(canary).
can_fly(eagle).
can_fly(pigeon).
can_fly(parrot).

cannot_fly(penguin).
cannot_fly(ostrich).

% Rule to check and display result
check_flight(Bird) :-
    can_fly(Bird),
    write(Bird), write(' can fly.'), nl.

check_flight(Bird) :-
    cannot_fly(Bird),
    write(Bird), write(' cannot fly.'), nl.

check_flight(Bird) :-
    \+ can_fly(Bird),
    \+ cannot_fly(Bird),
    write('Information about '), write(Bird), write(' is not available.'), nl.
