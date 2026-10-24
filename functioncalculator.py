def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a/b


try: 

    num1 = float(input("Enter the first number: "))
    operation = input("Choose the operation (add, subtract, multiply, divide")
    num2 = float(input("Enter the second number: "))


if operation == "add"
    result = add(num1, num2)
elif operation == "subtract":
    result = subtract(num1, num2)
elif operation == "multiply":
    result = multiply(num1, num2)
elif operation == "divide":
    result = divide(num1, num2)
else:
    result ="Invalid operation"

print("Result:" result)

except ValueError:
print("Error: Invalid input. Please enter a valid number.")

except ZeroDivisionError:
print("Error: Cannot divide by zero.")



