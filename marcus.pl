% Facts

man(marcus).
pompeian(marcus).
ruler(caesar).

tried_to_assassinate(marcus, caesar).

% Rules

roman(X) :-
    pompeian(X).

person(X) :-
    man(X).

% Romans who tried to assassinate Caesar hate Caesar
hates(X, caesar) :-
    roman(X),
    tried_to_assassinate(X, caesar).

% Romans who did not try to assassinate Caesar are loyal
loyal(X, caesar) :-
    roman(X),
    not(tried_to_assassinate(X, caesar)).

% Everyone is loyal to someone
loyal(X, friend) :-
    person(X).