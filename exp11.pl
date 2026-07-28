% Graph

edge(a,b).
edge(a,c).
edge(b,d).
edge(b,e).
edge(c,f).
edge(c,g).

% Best First Search (Simple)

best_first(Start,Goal):-
    edge(Start,Goal),
    write('Path: '),
    write(Start),
    write(' -> '),
    write(Goal),nl.

best_first(Start,Goal):-
    edge(Start,X),
    best_first(X,Goal).