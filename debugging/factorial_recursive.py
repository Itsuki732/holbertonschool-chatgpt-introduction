#!/usr/bin/python3
import sys

def factorial(n):
	"""
	Function Description:
		Computes the factorial of a non-negative integer n using recursion.
		The factorial of a number n (denoted n!) is the product of all positive integers 
		less than or equal to n. By definition, 0! is 1.

	Parameters:
		n (int): A non-negative integer whose factorial is to be calculated.

	Returns:
		int: The factorial of the given integer n.
	"""
	if n == 0:
		return 1  # Base case: 0! is defined as 1
	else:
		return n * factorial(n-1)  # Recursive case: n! = n * (n-1)!

# Get input from the command line argument and convert it to integer
f = factorial(int(sys.argv[1]))

# Print the calculated factorial
print(f)
