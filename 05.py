# Keep taking numbers as inputs till the user enters ‘x’, after that print sum of all.
sum = 0.0
count = 0

while True:#This will make this while loop into a infinite while loop
    number = float(input("Enter the number: "))
    sum += number

    choice =  input("Add another number? (y/n): ")
    if choice.casefold() == 'n':
        break

print(sum)

