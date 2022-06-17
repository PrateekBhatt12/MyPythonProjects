#To calculate Fibonacci Series up to n numbers.
Number = int(input("Enter the number until which you need the fibonacci series: "))

num1, num2 = 0 , 1
count = 0

while count < Number:
    print(num1)
    nth = num1 + num2
    num1 = num2
    num2 = nth
    count+=1
    
    