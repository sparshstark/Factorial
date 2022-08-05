def add(a,b):
    sum1 = a+b
    return sum1

def subtract(a,b):
    dif = a-b
    return dif

x=int(input("Enter a Number"))
y=int(input("Enter a Number"))
print("1. Add")
print("2. Subtract")
c = int(input("Enter your choice :"))
if c == 1:
    print("Answer is", add(x,y))
elif c == 2:
    print("Answer is", subtract(x,y))
else :
    print("ERROR")
