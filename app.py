# -----------------------------------------
# SIMPLE CALCULATOR SYSTEM
# -----------------------------------------
# This program performs basic arithmetic:
# Addition, Subtraction, Multiplication, Division
# -----------------------------------------

def add(a, b):
    # Returns the sum of a and b
    return a + b

def subtract(a, b):
    # Returns the difference of a and b
    return a - b

def multiply(a, b):
    # Returns the product of a and b
    return a * b

def divide(a, b):
    # Returns the quotient of a and b
    # Includes check to avoid division by zero
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

# -------------------------------
# MAIN PROGRAM LOOP
# -------------------------------
print("===== SIMPLE CALCULATOR SYSTEM =====")
print("Select operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division\n")

# User selects an operation
choice = input("Enter choice (1/2/3/4): ")

# User inputs two numbers
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

# Processing based on user's choice
if choice == '1':
    print("\nResult:", add(num1, num2))

elif choice == '2':
    print("\nResult:", subtract(num1, num2))

elif choice == '3':
    print("\nResult:", multiply(num1, num2))

elif choice == '4':
    print("\nResult:", divide(num1, num2))

else:
    print("\nInvalid choice. Try again!")