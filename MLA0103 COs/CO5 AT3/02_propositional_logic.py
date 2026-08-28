# Banking Loan Eligibility
# Propositional Logic Implementation


def loan_eligibility(income, credit_score, employment,
                     existing_loans, repayment):

    # Convert conditions into propositions

    I = income >= 40000
    C = credit_score >= 700
    E = employment == "employed"
    L = existing_loans <= 2
    R = repayment == "good"

    A = income >= 50000
    H = credit_score >= 750
    G = repayment == "average"

    # Rule 1:
    # I AND C AND E AND L AND R -> Eligible

    rule1 = I and C and E and L and R

    # Rule 2:
    # A AND H AND E AND L AND G -> Eligible

    rule2 = A and H and E and L and G

    # Final decision

    if rule1:
        return "Eligible - Rule 1"

    elif rule2:
        return "Eligible - Rule 2"

    else:
        return "Not Eligible"


# Customer data

customers = [
    ("Ravi", 60000, 750, "employed", 1, "good"),
    ("Priya", 30000, 650, "employed", 2, "good"),
    ("Rahul", 25000, 580, "unemployed", 3, "poor"),
    ("Anitha", 50000, 720, "employed", 0, "good"),
    ("Suresh", 50000, 750, "employed", 1, "average")
]


# Display results

for customer in customers:

    name, income, credit_score, employment, loans, repayment = customer

    result = loan_eligibility(
        income,
        credit_score,
        employment,
        loans,
        repayment
    )

    print(name, ":", result)