% Prolog Program to count number of vowels

% --- Check if a character is a vowel ---
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).
vowel(A) :- char_type(A, upper), char_lower(A, L), vowel(L).

% --- Count vowels in a list ---
count_vowels([], 0).  % Base case
count_vowels([H|T], Count) :-
    vowel(H),             % If head is a vowel
    count_vowels(T, RestCount),
    Count is RestCount + 1.

count_vowels([H|T], Count) :-
    \+ vowel(H),
