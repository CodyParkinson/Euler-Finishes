'''
07/27/2023

Q: For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

A: 743

'''

'''
I did not forget about finishing up these first 100 problems. I started getting into SwiftUI, and I have put Python on the backburner. But, I am back to finish
these up and close out this project! This is also me letting everyone know that from this problem forward - I will be using the assistance of Chat-GPT 4. I have
been trying to learn how to best interact with AI and create the best prompts. I am very interested in how AI can be used to help solve problems. Especially those
of the non-Euler kind. But, this is a great test for prompting.

This is not to say that I did not code, much of this code is still mine, but I use the prompting to help build the framework. This is where I find AI to be truly
remarkable. I save so much time letting the AI pour the foundation for me to build on. I was able to release my first IOS app in a fraction of the time of most
programmers, and the code passed all of Apple's security checks. This means that not only does the code work, but it can be made safe! 

This is just my extra note, and if you have problems with AI, please let me know, but otherwise I am very excited on its uses!

'''



# Roman numerals mapping
roman_to_int_mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman_to_int(roman):
    """Converts a Roman numeral to an integer."""
    total = 0
    i = 0

    while (i < len(roman)):
        # If this is the subtractive case.
        if i+1 < len(roman) and roman_to_int_mapping[roman[i]] < roman_to_int_mapping[roman[i+1]]:
            total -= roman_to_int_mapping[roman[i]]
        else:
            total += roman_to_int_mapping[roman[i]]
        i += 1
    return total

# Mapping from integer to Roman numerals
int_to_roman_mapping = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
keys = sorted(int_to_roman_mapping.keys(), reverse=True)

def int_to_roman(n):
    """Converts an integer to a Roman numeral."""
    result = ''
    for value in keys:
        count = n // value
        result += int_to_roman_mapping[value] * count
        n -= value * count
    return result



def load_text_file_to_list(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines from the file and store them in a list
            lines = file.readlines()

        # Remove the newline characters from each line and create the list
        data_list = [line.strip() for line in lines]

        return data_list
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Replace 'your_file.txt' with the actual path to your text file
file_path = 'roman.txt'
loaded_list = load_text_file_to_list(file_path)




characters_saved = 0
for roman in loaded_list:
    decimal = roman_to_int(roman)
    minimal_roman = int_to_roman(decimal)
    characters_saved += len(roman) - len(minimal_roman)

print(characters_saved)
