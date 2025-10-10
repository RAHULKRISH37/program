% Prolog program for Academic Database with Name and DOB

% Facts
student(wasim, '12-05-2002').
student(rahul, '21-09-2001').
student(anjali, '03-11-2003').
student(neha, '27-01-2002').
student(arjun, '15-07-2001').

% Rule to find DOB by name
find_dob(Name, DOB) :-
    student(Name, DOB).
