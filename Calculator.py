def add (x,y):
    return x + y
def subtract (x,y):
    return x - y
def multiply (x,y):
    return x * y
def divide (x,y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("1. Add 2. Subtract 3. Multiply 4. Divide")
operation = input("What would you like to do?")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if operation == "1":
    print(add(x,y))
elif operation == "2":
    print(subtract(x,y))
elif operation == "3":
    print(multiply(x,y))
elif operation == "4":
    print(divide(x,y))
else:
    print("Invalid operation.")