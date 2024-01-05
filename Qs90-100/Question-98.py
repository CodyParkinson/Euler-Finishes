'''
01/04/2024

Q: By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 
1296 = 36^2. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, 
also forms a square number: 9216 = 96^2. We shall call CARE (and RACE) a square anagram word pair and specify further 
that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common 
English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

All anagrams formed must be contained in the given text file.

A: 18769

'''

# Each number must only contain unique values, this really spees up the program.
# Other than that pretty straight forward.

with open('words.txt', 'r') as file:
    content = file.read()
    content = content.replace('"', '').split(',')


# Step 1: Find all the anagrams
import itertools
from collections import defaultdict

def find_anagram_pairs(words):
    # Group words by their sorted characters
    grouped_words = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        grouped_words[sorted_word].append(word)

    # Find groups with more than one word (anagrams)
    anagram_pairs = []
    for group in grouped_words.values():
        if len(group) > 1:
            for pair in itertools.combinations(group, 2):
                anagram_pairs.append(pair)

    return anagram_pairs

anagram_pairs = find_anagram_pairs(content)

anagramLong = []
for i in anagram_pairs:
    if len(i[0]) == 5:
        anagramLong.append(i)



# Step 2: Create a list of all squares up to length 9 (longest word is 9 letters)
listOfSquares = []
for i in range(2, 32_000):
    x = i**2
    if x < 1_000_000_000:
        listOfSquares.append(x)

listOfUniques = []
for i in listOfSquares:
    if len(str(i)) == len(set(str(i))) and len(str(i)) == 5:
        listOfUniques.append(i)



# Step 3: Assign digits to letters and see if they are square numbers
finals = []
for i in anagramLong:
    for c in listOfUniques:
        dictOfLetters = {}
        for a, b in zip(i[0], str(c)):
            dictOfLetters[a] = b

        numb = ''
        for d in i[1]:
            numb += dictOfLetters[d]


        if int(numb) in listOfUniques:
            finals.append(int(numb))
            finals.append(c)

print(max(finals))





