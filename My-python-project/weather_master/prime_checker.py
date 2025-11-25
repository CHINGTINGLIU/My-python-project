"""
File: prime_checker.py
Name: Alice Liu
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program asks user input a number to check the prime number is or not.
	"""
	print('Welcome to the prime checker!')
	while True:
		n = int(input('n:'))
		if n == EXIT:
			print('Have a good one!')
			break
		elif is_prime(n):
			print(str(n)+'is a prime number.')
		else:
			print(str(n)+'is not a prime number.')


def is_prime(n):
	"""
	:param n: int >1
	: False-->not a prime num; True--->is a prime number
	"""
	for i in range(2, n):  
		if n % i == 0:
			return False
	return True



if __name__ == "__main__":
	main()
