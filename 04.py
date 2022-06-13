# Take 2 numbers as inputs and find their HCF and LCM
def compute_gcd(x,y):
    while(y):
        x, y=y, x%y
    return x
def compute_lcm(x,y):
    lcm = (x*y)
    return lcm
num1 = 54
num2 = 24

print("The L.C.M is: ", compute_lcm(num1, num2))
print("The H.C.F is ", compute_gcd(num1, num2))