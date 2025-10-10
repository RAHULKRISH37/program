% Prolog Program to implement Backward Chaining

% --- Facts ---
fact(sunny).
fact(warm).
fact(cloudy).
fact(rainy).

% --- Rules ---
rule(play_outside, [sunny, warm]).
rule(stay_home, [rainy]).
rule(take_umbrella, [cloudy, rainy]).

% --- Backward Chaining Algorithm ---
backward_chain(Goal) :-
    fact(Goal),
    write('Goal achieved: '), write(Goal), nl.

backward_chain(Goal) :-
    rule(Goal, Conditions),
