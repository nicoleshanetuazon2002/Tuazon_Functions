print("CS112: COMPUTER PROGRAMMING 1 - PRE- FINAL EXAM")
print("Created by: Nicole Shane P. Tuazon")


def is_prime(num):
    # Function to check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def smallest_factor(n):
    # Function to find the smallest factor of n
    if n < 2:
        return None  # No prime factor for numbers less than 2
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n


def find_prime_numbers_in_range(start, end):
    # Function to find and display prime numbers within a given range
    if start < 0 or end < start:
        print("Invalid input. Please enter valid numbers.")
        return
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)


while True:
    # Get user input for the operation selection
    choice = int(input("Choose operation:\n1. Find smallest factor of n\n2. Find prime numbers in range\nEnter choice (1 or 2): "))

    if choice == 1:
        # Get user input for the number to find the smallest factor
        num_to_factor = int(input("Enter a number to find the smallest factor: "))
        result = smallest_factor(num_to_factor)
        print(f"The smallest factor of {num_to_factor} is: {result}")

    elif choice == 2:
        # Get user input for the starting and ending numbers
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
        find_prime_numbers_in_range(start, end)

    else:
        print("Invalid choice. Please enter 1 or 2.")

    # Ask the user if they want to continue
    cont = input("Do you want to perform another operation? (yes/no): ").lower()
    if cont != "yes":
        print("Program terminated.")
        break