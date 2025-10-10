% Prolog program to find the sum of integers from 1 to N

sum(1, 1).                       % Base case
sum(N, Result) :-
    N > 1,
    N1 is N - 1,                 % Decrement N
    sum(N1, SubResult),          % Recursive call
    Result is N + SubResult.     % Add current N to sub-result
