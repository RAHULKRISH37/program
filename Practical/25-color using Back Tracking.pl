% Prolog Program for Fruits and their Colors using Backtracking

% --- Facts ---
fruit_color(apple, red).
fruit_color(strawberry, red).
fruit_color(cherry, red).
fruit_color(banana, yellow).
fruit_color(mango, yellow).
fruit_color(orange, orange).
fruit_color(grapes, purple).
fruit_color(kiwi, green).
fruit_color(pear, green).

% --- Rule to find fruits by color ---
find_fruit_by_color(Color, Fruit) :-
    fruit_color(Fruit, Color).
