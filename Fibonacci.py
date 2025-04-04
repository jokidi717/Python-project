#Welcoming the user to the Fibonacci Sequence program
print("Welcome to the Fibonacci Sequence Program.")

def fibonacci_sequence(n):
    if n <= 0:  # Ensure valid input
        print("Please enter a positive integer.")  
        return  # Exit early for invalid input

    # Initializing the first two Fibonacci numbers
    a, b = 2, 3
    print("Fibonacci sequence up to", n, "terms:")

    for _ in range(n):  # Generate Fibonacci sequence
        print(a, end=" ")
        a, b = b, a + b  # Update values

    print()  # New line for better formatting

# Get user input
n = int(input("Enter the number of terms: "))
fibonacci_sequence(n)