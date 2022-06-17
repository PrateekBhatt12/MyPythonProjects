#Write a program to input principal, time, and rate (P, T, R) from the user and find Simple Interest.
Principal = int(input("Enter your principal amount: "))
Time = int(input("Enter the time taken: "))
Rate = int(input("The rate of interest charged: "))

Simple_Interest = Principal*Rate*Time

print(f"The simple interest by your given values is calculatede to be Rupees {Simple_Interest}.")