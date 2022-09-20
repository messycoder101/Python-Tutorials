# Program to convert kilo to lbs and vice versa

choice = input("Hello, would you like to convert weight in 'kg' or 'lbs' ?")
if choice == 'kg':
    lbs = input("Hello, please input weight in 'lbs': ")
    kg = int(lbs)*0.453592
    print(f"The weight in kilograms is {kg} kg")

else:
    kg = input("Hello, please input weight in 'kgs': ")
    lbs = int(kg)/0.453592
    print(f"The weight in pounds is {lbs} lbs")
