% Prolog Program for STUDENT - TEACHER - SUBJECT CODE Database

% Facts
handles(mr_rajesh, cs101).
handles(ms_priya, cs102).
handles(mr_arun, cs103).
handles(ms_kavya, cs104).

enrolled(wasim, cs101).
enrolled(rahul, cs102).
enrolled(anjali, cs103).
enrolled(neha, cs104).
enrolled(arjun, cs101).

% Rule to find which teacher teaches a student
teaches(Teacher, Student) :-
    enrolled(Student, SubCode),
    handles(Teacher, SubCode).

% Rule to find which subject code a
