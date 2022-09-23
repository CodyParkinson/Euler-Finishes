'''
9/23/2022

Q: The nth term of the sequence of triangle numbers is given by, t(n) = (1/2)n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

A: 162

'''

# Create a dictionary of letters and their corresponding index value
import string
letters = string.ascii_uppercase
dictLetters = {}
for i in letters:
    dictLetters[i] = letters.index(i) + 1

# Create a list of triangle nums
triangle_nums = []
for i in range(1,100):
    triangle_nums.append(int((1/2) * i * (i + 1)))


# Open the file and extract the names to a string
with open("words.txt", 'r') as namesFile:
    names = str(namesFile.readlines())

# Because names is one long string, it needs converted into individual names
namesList = []
addName = ''
for i in names:
    if i in letters:
        addName += i 
    elif i not in letters and addName != '':
        namesList.append(addName)
        addName = ''
    else:
        pass

# Check each name to see if it is a triangle
tris = 0
for i in namesList:
    nameTotal = 0
    for b in i:
        nameTotal += dictLetters[b]
    if nameTotal in triangle_nums:
        tris += 1

print(tris)
