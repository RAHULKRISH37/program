% Prolog Program to suggest a Dieting System based on Disease

% --- Facts ---
diet(diabetes, 'Low sugar, high fiber diet with whole grains, vegetables, and lean proteins. Avoid sweets and sugary drinks.').
diet(hypertension, 'Low-sodium diet with fruits, vegetables, whole grains, and lean meat. Avoid processed and salty foods.').
diet(obesity, 'Low-calorie diet with more salads, fruits, and fiber-rich food. Avoid fried and fast food.').
diet(anemia, 'Iron-rich diet including spinach, red meat, lentils, and vitamin C rich fruits.').
diet(heart_disease, 'Low-fat, low-cholesterol diet with nuts, fish, oats, and olive oil. Avoid red meat and butter.').
diet(kidney_disease, 'Low-protein, low-sodium diet with fresh fruits, rice, and boiled vegetables. Avoid processed foods.').
diet(ulcer, 'Bland diet with milk, banana, oatmeal, and non-spicy soft foods. Avoid caffeine and spicy food.').

% --- Rule ---
suggest_diet(Disease) :-
    diet(Disease, Diet),
    write('Recommended Diet for '), write(Disease), write(':'), nl,
    write(Diet), nl.

suggest_diet(Disease) :-
    \+ diet(Disease, _),
    write('Sorry, no diet information available for '), write(Disease), write('.'), nl.
