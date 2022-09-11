'''
09/11/2022

Q: Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

A: 871198282

'''

with open('names.txt') as file:
   namesOpen = file.read()
namesOpen = namesOpen.split(",")
names = []
for i in namesOpen:
    names.append(i[1:-1])
names.sort()

# Create a list of letters and check for it's index in the list. Add one to this value as python lists start at 0.
import string
letters = list(string.ascii_uppercase)
total = 0
for i in names:
    namePlacement = names.index(i) + 1
    nameSum = 0
    for b in i:
        if b in letters:
            nameSum += letters.index(b) + 1
    total += namePlacement * nameSum

print(total)
