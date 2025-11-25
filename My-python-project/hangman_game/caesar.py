"""
File: caesar.py
Name: Alice Liu
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program asks user to input a number to produce shifted ALPHABET as the cipher table.
    """
    x = int(input('Secret number: '))
    old_word = input("What's the ciphered string?").upper()
    ans = decode(x, old_word)
    print('The deciphered string is :' + ans)


def decode(num, input_text):
    new_seq = new_sequence(num)
    ans = ''
    for ch in input_text:
        if new_seq.find(ch) != -1:
            ans += ALPHABET[new_seq.find(ch)]
        else:
            ans += ch
    return ans


def new_sequence(num):
    first_half = ALPHABET[:len(ALPHABET)-num]
    second_half = ALPHABET[len(ALPHABET)-num:]

    return second_half + first_half


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
