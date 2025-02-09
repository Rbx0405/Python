def sum_of_natural_numbers(n):
    # Base case: if n is 0, return 0
    if n <= 0:
        return 0
    else:
        # Recursive case: add n to the sum of numbers from 1 to n-1
        return n + sum_of_natural_numbers(n - 1)

# Example usage:
n = int(input("Enter a positive integer: "))

if n < 0:
    print("Please enter a positive integer.")
else:
    result = sum_of_natural_numbers(n)
    print(f"The sum of the first {n} natural numbers is: {result}")