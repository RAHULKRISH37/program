% Prolog Program to implement a Family Tree

% --- Facts ---
male(john).
male(michael).
male(rahul).
male(rohit).

female(susan).
female(linda).
female(anjali).
female(neha).

parent(john, michael).
parent(susan, michael).
parent(john, linda).
parent(susan, linda).
parent(michael, rahul).
parent(anjali, rahul).
parent(michael, neha).
parent(anjali, neha).

% --- Rules ---

% father(X, Y): X is the father of Y
father(X, Y) :-
    male(X),
    parent(X, Y).

% mother(X, Y): X is the mother of Y
mother(X, Y) :-
    female(X),
    parent(X, Y).

% sibling(X, Y): X and Y share a parent and are not the same
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% brother(X, Y): X is male and a sibling of Y
brother(X, Y) :-
    male(X),
    sibling(X, Y).

% sister(X, Y): X is female and a sibling of Y
sister(X, Y) :-
    female(X),
    sibling(X, Y).

% grandparent(X, Y): X is a grandparent of Y
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% ancestor(X, Y): X is an ancestor of Y
ancestor(X, Y) :-
    parent(X, Y).

ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).
