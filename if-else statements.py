''' Program to ask for user input
    and print if it's a Hot, Normal or Cold day.
'''
feeling = input("Hello, are you feeling Hot, Cold or Normal today?\n")
if feeling.lower() == 'hot':
    print("It's a Hot Day!")
elif feeling.lower() == 'cold':
    print("It's a Cold Day!")
else :
    print("It's a Normal Day!")

'''
is_hot = True
is_cold = True
if is_hot:
    print("It's a Hot Day!")
elif is_cold:
    print("It's a Cold Day")
else:
    print("It's a Normal Day")'''