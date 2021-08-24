"""
File: similarity.py
Name: Ryan Lei
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    After the user input a DNA sequence and another DNA sequence that
    the user would like to match, this function will find the best
    match of the first inputted DNA sequence.
    """
    # Let user input the long DNA sequence.
    long_sequence = input('Please give me a DNA sequence to search: ')
    # Let user input the DNA sequence that user would like to match.
    short_sequence = input('What DNA sequence would you like to match? ')
    # Case-insensitve for the dna that user inputted.
    long_sequence = long_sequence.upper()
    short_sequence = short_sequence.upper()
    print('The best match is '+str(dna_matching(long_sequence, short_sequence)))


def dna_matching(long_sequence, short_sequence):
    """
    :param long_sequence: str, long dna sequence that user inputted.
    :param short_sequence: str, short dna sequence that user wants to match.
    :return: str, show the best dna in long dna sequence.
    """
    # Catch the len of the short dna sequence.
    short_dna_len = len(short_sequence)
    # Catch the len of the long dna sequence.
    long_dna_len = len(long_sequence)
    # Storage the ans string.
    ans = ''
    # Count the highest score in long dna sequence.
    maximum = 0
    # Compare sub dna and short dna sequence.
    # Discuss with TA Wilson on 2020/1/11.
    for i in range(long_dna_len-short_dna_len+1):
        # Catch long dna string.
        sub_dna = long_sequence[i:i+len(short_sequence)]
        # Count for the correction of similarity.
        count = 0
        # Compare each character in sub dna and short sequence dna.
        for j in range(short_dna_len):
            a = sub_dna[j]
            b = short_sequence[j]
            # When the same dna appears, sub dna score one point.
            if a == b:
                count += 1
        # When the score of dna in long dna sequence, replace the lower score.
        if count > maximum:
            maximum = count
            ans = sub_dna
    return ans





###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
