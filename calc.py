''' A simple calculator made on Python3
    Run on the command line!

    - Author: Sasank Ganapathiraju
'''

print("Python Calculator")
print("Directions:")
print("Add (+)")
print("Subtract (-)")
print("Multiply (*)")
print("Divide (/)")

# Operations
def add (x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

# Get input
num1 = int(input("First number: "))
operator = input("Operation: ")
num2 = int(input("Second number: "))

# Process input
if operator == "+":
    print(num1,"+",num2,"=", add(num1,num2))
elif operator == "-":
    print(num1,"-",num2,"=", subtract(num1,num2))
elif operator == "*":
    print(num1,"*",num2,"=", multiply(num1,num2))
elif operator == "/":
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid input")