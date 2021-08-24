"""
File: caesar.py
Name: Ryan Lei
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
    User will input a number to shift ALPHABET. And user will be
    asked to input a code. After that, any code will be deciphered
    to a new code.
    """
    # User input the translation of the ALPHABET.
    secret_number = int(input('Secret number: '))
    # User input the ciphered string.
    secret_code = input("What's the ciphered string? ")
    # Put upper tools.
    secret_code = secret_code.upper()
    # Store the new alphabet.
    new_alph = new_alphabet(secret_number)
    # Pick the index from new alphabet, and Use the index from new alphabet to catch the index in the original alphabet.
    # Discuss with TA Wilson on 2021/1/12
    secret_answer = generate_new_code(secret_code, new_alph)
    print(secret_answer)


def generate_new_code(secret_code, new_alph):
    """
    :param secret_code: str, the secret_code that user inputted.
    :param new_alph: str, new alphabet that user translated.
    :return: int, the index of secret_code in new_alphabet.
    """
    ans = ''
    for i in range(len(secret_code)):
        # Separate the character from secret code.
        ch_in_secret_code = secret_code[i]
        # Catch the index from new alphabet.
        new_ind = new_alph.find(ch_in_secret_code)
        # If there is a space or other character in the secret code, input the original character in answer.
        if new_ind == -1:
            # Combine the original character in the secret code.
            # Discuss with TA Wilson on 2021/1/13.
            ans += ch_in_secret_code
        else:
            # Catch and combine the alphabet from the original ALPHABET.
            ans += ALPHABET[new_ind]
    return ans


def new_alphabet(secret_number):
    """
    :param secret_number: int, secret_number >= 0
    :return: str, the shifted ALPHABET.
    """
    # Discuss with TA Wilson on 2021/1/8
    translation_alphabet = ''
    i = len(ALPHABET)-secret_number
    # Pick the alphabet that user wants to translate.
    translation_alphabet = ALPHABET[i:]
    # Combine all the alphabet.
    translation_alphabet += ALPHABET[:i]
    return translation_alphabet









#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
