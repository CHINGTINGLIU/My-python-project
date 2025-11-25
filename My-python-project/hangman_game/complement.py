"""
File: complement.py
Name: Alice Liu
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""

# This constant controls when to stop
EXIT = ''


def main():
    """
    This program uses string manipulation to tackle a real world problem - finding the
    complement strand of a DNA sequence.
    """

    print(build_complement('ATC'))   # TAG
    print(build_complement(''))  # DNA strand is missing.
    print(build_complement('ATGCAT'))  # TACGTA
    print(build_complement('GCTATAC'))  # CGATATG


def build_complement(string):
    ans = ''
    if string == EXIT:
        return 'DNA strand is missing.'
    else:
        for i in range(len(string)):
            ch = string[i]
            if ch == 'A':
                ans += 'T'
            elif ch == 'T':
                ans += 'A'
            elif ch == 'G':
                ans += 'C'
            elif ch == 'C':
                ans += 'G'
        return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
