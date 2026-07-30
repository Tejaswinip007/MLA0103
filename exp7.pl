% Gender
female(pam).
female(liz).
female(ann).
female(pat).

male(tom).
male(bob).
male(jim).

% Parent relationships
parent(pam,bob).
parent(tom,bob).

parent(pam,liz).
parent(tom,liz).

parent(bob,ann).
parent(bob,pat).

parent(liz,jim).

% Mother
mother(X,Y) :-
    female(X),
    parent(X,Y).

% Father
father(X,Y) :-
    male(X),
    parent(X,Y).

% Grandfather
grandfather(X,Y) :-
    male(X),
    parent(X,Z),
    parent(Z,Y).

% Grandmother
grandmother(X,Y) :-
    female(X),
    parent(X,Z),
    parent(Z,Y).

% Sister
sister(X,Y) :-
    female(X),
    parent(P,X),
    parent(P,Y),
    X \= Y.

% Brother
brother(X,Y) :-
    male(X),
    parent(P,X),
    parent(P,Y),
    X \= Y.