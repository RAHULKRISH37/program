% Prolog Program to implement Forward Chaining

% --- Facts ---
fact(sunny).
fact(warm).
fact(cloudy).

% --- Rules ---
rule(play_outside, [sunny, warm]).
rule(stay_home, [rainy]).
rule(take_umbrella, [cloudy, rainy]).

% --- Forward Chaining Algorithm ---
forward_chain(Goal) :-
    fact(Goa
