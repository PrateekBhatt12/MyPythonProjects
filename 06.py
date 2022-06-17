# Write a program to print whether a number is even or odd, also take input from the user
Number = int(input("Enter your number: "))

if Number % 2 == 0:
    print(f"{Number} is an evennumber.")
else:
    print(f"{Number} is an odd number.")
