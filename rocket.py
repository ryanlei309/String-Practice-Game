"""
File: rocket.py
Name: Ryan Lei
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


# This constant determines rocket size.
SIZE = 3


def main():
	"""
	This program will print the rocket.
	"""
	head_rocket()
	belt_rocket()
	upper_rocket()
	lower_rocket()
	belt_rocket()
	head_rocket()


def head_rocket():
	"""
	This for loop build the head of the rocket.
	"""
	for i in range(SIZE):
		# Discuss with TA Wilson on 2021/1/10
		for j in range(-i+SIZE):
			print(' ', end="")
		for j in range(i+1):
			print('/', end="")
		for j in range(i+1):
			print('\\', end="")
		print("")


def belt_rocket():
	"""
	This for loop build the belt of the rocket.
	"""
	print('+', end="")
	for i in range(SIZE*2):
		print("=", end="")
	print('+')


def upper_rocket():
	"""
	This for loop build the upper part of the rocket.
	"""
	for i in range(SIZE):
		print('|', end="")
		for j in range(-i+SIZE-1):
			print('.', end="")
		for j in range(i+1):
			print('/'+'\\', end="")
		for j in range(-i+SIZE-1):
			print('.', end="")
		print('|')


def lower_rocket():
	"""
	This for loop build the upper part of the rocket.
	"""
	for i in range(SIZE):
		print('|', end="")
		for j in range(i):
			print('.', end="")
		for j in range(-i+SIZE):
			print('\\'+'/', end="")
		for j in range(i):
			print('.', end="")
		print('|')






###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()