"""
File: quadratic_solver.py
Name: Alice Liu
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This program calls stanCode Quadratic Solver!
	"""
	a = int(input('First Number: '))
	b = int(input('Second Number: '))
	c = int(input('Third Number: '))
	discriminant = b*b-4*a*c
	if discriminant > 0:
		x1 = (-b + math.sqrt(discriminant)) / (2 * a)
		x2 = (-b - math.sqrt(discriminant)) / (2 * a)
		print(str(x1)+','+str(x2))
	else:
		if discriminant == 0:
			x = (-b + math.sqrt(discriminant)) / (2 * a)
			print(str(x))
		else:
			print('no real roots')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
