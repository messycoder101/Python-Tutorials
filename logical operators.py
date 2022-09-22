# Logical operators are and, or, not

# Example
has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit: # and operator
    print("Congratulations! You're eligible for a loan.")
if has_high_income or has_good_credit: # or operator
    print("Congratulations! You're eligible for a loan.")
if has_good_credit and not has_criminal_record: # not operator
    print("Congratulations! You're eligible for a loan.")
