
# Banking Loan Eligibility
# Production Rules Implementation

def check_loan(income, credit_score, employment, existing_loans, repayment):

    # Rule 1
    if (income >= 40000 and
        credit_score >= 700 and
        employment == "employed" and
        existing_loans <= 2 and
        repayment == "good"):

        return "Eligible - Rule 1"

    # Rule 2
    elif (income >= 50000 and
          credit_score >= 750 and
          employment == "employed" and
          existing_loans <= 2 and
          repayment == "average"):

        return "Eligible - Rule 2"

    # No rule satisfied
    else:
        return "Not Eligible"


# Test customers

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

    result = check_loan(
        income,
        credit_score,
        employment,
        loans,
        repayment
    )

    print(name, ":", result)
