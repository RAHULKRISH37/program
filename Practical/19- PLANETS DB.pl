% Prolog Program for PLANETS Database (PLANETSDB)

% Facts: planet(Name, DistanceFromSun_MillionKm, Diameter_Km, NumberOfMoons)
planet(mercury, 57.9, 4879, 0).
planet(venus, 108.2, 12104, 0).
planet(earth, 149.6, 12742, 1).
planet(mars, 227.9, 6779, 2).
planet(jupiter, 778.5, 139820, 79).
planet(saturn, 1434, 116460, 83).
planet(uranus, 2871, 50724, 27).
planet(neptune, 4495, 49244, 14).

% Rule to find planets with more than a given number of moons
planets_with_moons(Moons) :-
    planet(Name, _, _, Count),
    Count > Moons,
    write(Name), write(' has '), write(Count), write(' moons.'), nl.

% Rule to find planets within a certain distance from the Sun
planets_within_distance(Distance) :-
    planet(Name, Dist, _, _),
    Dist =< Distance,
    write(Name), write(' is within '), write(Distance), write(' million km.'), nl.
