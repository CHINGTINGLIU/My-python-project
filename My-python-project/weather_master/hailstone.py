"""
File: hailstone.py
Name: Alice Liu
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

# This number controls when to stop the program
EXIT = 1


def main():
    """
    This program implements a console program "hailstone sequence",which asks user to
    input a number to match what is shown in the sample run until 1.
    """
    print('This program computes Hailstone sequences.')
    n = int(input('Enter a number: '))
    count = 0
    while True:
        if n == EXIT:
            break
        elif odd(n) is True:
            print(str(n) + 'is odd,so I make 3n+1:' + str(3 * n + 1))
            n = 3 * n + 1        # 應在print完之後將x reassign為3 * x + 1才可以做下一次運算
            count += 1
        else:
            print(str(n)+'is even,so I take half:'+str(n//2))
            n = n // 2
            count += 1
    print('It took ' + str(count) + 'steps to reach 1.')


def odd(num):      # function的括弧內要傳入num，function的世界裡才有原物料可以製造答案
    """
    odd = True
    even = False
    """
    if num % 2 == 1:
        return True
    else:
        return False



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
