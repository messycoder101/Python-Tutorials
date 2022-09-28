print("This is a simple program to add two numbers :) \nPlease enter the first number:")
a=int(input())

if a >= 0:
    print("Please enter the second number:")
else:
    print("Please enter a valid number:")

b=int(input())
if b>=0:
    c=a+b
else:
    print("Please enter a valid number")

print("The sum of the two numbers is: "+ str(c))

