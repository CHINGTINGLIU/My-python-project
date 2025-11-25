"""
File: rocket.py
Name: Alice Liu
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    This program should implement a console program that draws ASCII art - a rocket.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():

    total_width = 2 * SIZE + 2 
    for i in range(SIZE):
        wings = "/" * (i + 1) + "\\" * (i + 1)  # /\ 、//\\、///\\\\ ...
        spaces = (total_width - len(wings)) // 2
        print(" " * spaces + wings)


def belt():
    print('+', end='')
    for i in range(2 * SIZE):
        print('=', end='')
    print('+')


def upper():
    for i in range(SIZE):
        print('|', end='')
        for j in range(SIZE - i-1):
            print('.', end='')
        for j in range(i+1):
            print('/', end='')
            print('\\', end='')
        for j in range(SIZE - i - 1):
            print('.', end='')
        print("|")


def lower():
    for i in range(SIZE):
        print("|", end="")
        for j in range(i):
            print(".", end="")
        for j in range(SIZE - i):
            print("\\/", end="")
        for j in range(i):
            print(".", end="")
        print("|")


if __name__ == "__main__":
    main()

