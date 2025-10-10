% Prolog Program to implement the Monkey–Banana Problem

% State representation:
% state(MonkeyPosition, BoxPosition, MonkeyOnBox, HasBanana)

% Initial state:
% Monkey is at door, box is at window, monkey is on floor, doesn't have banana.
initial_state(state(at_door, at_window, on_floor, has_not)).

% Goal state:
goal_state(state(_, _, on_box, has)).

% Actions and transitions

% 1. Monkey walks from one position to another
move(state(_, Box, on_floor, Has), walk(X, Y), state(Y, Box, on_floor, Has)).

% 2. Monkey pushes box from one place to another
move(state(Pos, Pos, on_floor, Has), push_box(Pos, NewPos), state(NewPos, NewPos, on_floor, Has)).

% 3. Monkey climbs onto the box
move(state(Pos, Pos, on_floor, Has), climb(Pos), state(Pos, Pos, on_box, Has)).

% 4. Monkey grasps the banana
move(state(center_room, center_room, on_box, has_not), grasp, state(center_room, center_room, on_box, has)).

% Recursive rule to reach goal
can_get_banana(State) :-
    goal_state(State).

can_get_banana(State1) :-
    move(State1, Move, State2),
    write('Monkey performs action: '), write(Move), nl,
    can_get_banana(State2).
