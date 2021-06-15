print("Functions in Python")


a = 8
b = 20

def add():
    print(a + b)

def sub():
    print(a - b)

def mul():
    print(a * b)

def even_or_odd(var):
    
    if (var % 2 == 0):
        print(var, "is Even")
    else:
        print(var, "is ODD")

def factorial(var):

    fact = 1
    
    for i in range(1,var+1):
        fact = fact * i

    print("Factorial of", var,"is",fact)

print("********************")
print("Press 1 for add")
print("Press 2 for sub")
print("Press 3 for mul")
print("Press 4 for even/odd")
print("Press 5 for Factorial")
print("********************")

choice = int(input("Enter your choice: "))


if (choice == 1):
    add()
    
if (choice == 2):
    sub()
    
if (choice == 3):
    mul()
    
if (choice == 4):
    
    even_or_odd(a)
    even_or_odd(b)

if (choice == 5):
    
    factorial(a)
    factorial(b)



