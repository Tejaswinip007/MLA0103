parent(tom,bob).
parent(bob,ann).
parent(ann,liz).

ancestor(X,Y):-
    parent(X,Y).

ancestor(X,Y):-
    parent(X,Z),
    ancestor(Z,Y).