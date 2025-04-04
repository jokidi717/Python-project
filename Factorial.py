# Welcome the user to the Factorial Calculation program
print("Welcome to the Factorial Calculation program!")

# Ask the user which factorial they want to calculate
number = int(input("Please enter a positive integer: "))

# Ensure that the user input is a positive integer
while number < 0:
    print("Factorial is not defined for negative numbers.")
    number = int(input("Please enter a positive integer: "))

# Generate the factorial of the given number using a for loop
factorial = 1
for i in range(1, number + 1):
    factorial *= i

# Output the result
print(f"The factorial of {number} is {factorial}")