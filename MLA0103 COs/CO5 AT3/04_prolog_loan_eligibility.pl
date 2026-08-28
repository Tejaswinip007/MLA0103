
% ==========================================
% Banking Loan Eligibility
% Prolog Implementation
% ==========================================

% ------------------------------------------
% Customer Facts
% ------------------------------------------

customer(ravi, 60000, 750, employed, 1, good).

customer(priya, 30000, 650, employed, 2, good).

customer(rahul, 25000, 580, unemployed, 3, poor).

customer(anitha, 50000, 720, employed, 0, good).

customer(suresh, 50000, 750, employed, 1, average).


% ------------------------------------------
% Rule 1
% ------------------------------------------

loan_eligible(Name) :-
    customer(Name, Income, CreditScore, Employment, Loans, Repayment),
    Income >= 40000,
    CreditScore >= 700,
    Employment = employed,
    Loans =< 2,
    Repayment = good.


% ------------------------------------------
% Rule 2
% ------------------------------------------

loan_eligible(Name) :-
    customer(Name, Income, CreditScore, Employment, Loans, Repayment),
    Income >= 50000,
    CreditScore >= 750,
    Employment = employed,
    Loans =< 2,
    Repayment = average.


% ------------------------------------------
% Check Loan Eligibility
% ------------------------------------------

check_loan(Name) :-
    loan_eligible(Name),
    write(Name),
    write(' is ELIGIBLE for the loan.'),
    nl.

check_loan(Name) :-
    \+ loan_eligible(Name),
    write(Name),
    write(' is NOT ELIGIBLE for the loan.'),
    nl.

