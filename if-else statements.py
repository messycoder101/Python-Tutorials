#.................................................................................
# 1 Program to ask for user input and print if it's a Hot, Normal or Cold day.
#.................................................................................

'''
feeling = input("Hello, are you feeling Hot, Cold or Normal today?\n")
if feeling.lower() == 'hot':
    print("It's a Hot Day!")
elif feeling.lower() == 'cold':
    print("It's a Cold Day!")
else :
    print("It's a Normal Day!")'''
#.................................................................................
# 2 Program to tell down payment of property
#.................................................................................
'''Uncomment from this line to the last line

property_price = input("Hello, please enter property cost!:\n") # to calculate down payment amount
int(property_price)
#   check credit score first
credit = input("Hello, please share your credit score (it is between 0-1000):\n")
# multiplier = 1 # initializing multiplier (it's value changes with credit score)--example of OVERLOADING

if 1000> int(credit) >= 500:
    down_pay = int(property_price) * 0.1  # formula to calculate down payment
    print(f"Congratulations, you have a great credit score.\nYou only have to pay 10% down payment!!\nYour down payment is Euro {down_pay}")
elif 0< int(credit) < 500:
    down_pay = int(property_price)*0.2 # formula to calculate down payment
    print(f"Congratulations, your credit is score acceptable and you can pay 20% down payment to proceed!!\nYour down payment is Euro {down_pay}")
else :
    print("Please enter a credit score between 0-1000.") 

# Uncomment till here'''