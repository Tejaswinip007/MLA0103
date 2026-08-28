# Banking Loan Eligibility
# First-Order Logic Implementation

# Customer knowledge base

customers = {
    "Ravi": {
        "income": 60000,
        "credit_score": 750,
        "employment": "employed",
        "existing_loans": 1,
        "repayment": "good"
    },

    "Priya": {
        "income": 30000,
        "credit_score": 650,
        "employment": "employed",
        "existing_loans": 2,
        "repayment": "good"
    },

    "Rahul": {
        "income": 25000,
        "credit_score": 580,
        "employment": "unemployed",
        "existing_loans": 3,
        "repayment": "poor"
    },

    "Anitha": {
        "income": 50000,
        "credit_score": 720,
        "employment": "employed",
        "existing_loans": 0,
        "repayment": "good"
    },

    "Suresh": {
        "income": 50000,
        "credit_score": 750,
        "employment": "employed",
        "existing_loans": 1,
        "repayment": "average"
    }
}


# First-Order Logic rules

def is_eligible(name):
    
    person = customers[name]

    income = person["income"]
    credit_score = person["credit_score"]
    employment = person["employment"]
    loans = person["existing_loans"]
    repayment = person["repayment"]

    # Rule 1

    rule1 = (
        income >= 40000
        and credit_score >= 700
        and employment == "employed"
        and loans <= 2
        and repayment == "good"
    )

    # Rule 2

    rule2 = (
        income >= 50000
        and credit_score >= 750
        and employment == "employed"
        and loans <= 2
        and repayment == "average"
    )

    if rule1:
        return "Eligible - Rule 1"

    elif rule2:
        return "Eligible - Rule 2"

    else:
        return "Not Eligible"


# Evaluate all customers

for name in customers:

    result = is_eligible(name)

    print(name, ":", result)