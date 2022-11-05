'''
10/27/2022

Q: By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

A: 7273

'''

# Used all the same code from Question 18 - just had to add an open file and change the dummy list length

# Open File
with open('p067_triangle.txt', 'r') as triangle:
    numbers = triangle.read()

# I use numpy later to add lists together
import numpy as np

# Convert the string of numbers into a list of integers
listOfNums = []
num = ''
for i in numbers:
    if i in '1234567890':
        num += i
    else:
        num = ''
    if len(num) == 2:
        listOfNums.append(int(num))

# Convert the list of integers into seperate lists that represent the line it is in
listOfLines = []
line = []
upLine = 1
for i in listOfNums:
    line.append(i)
    if len(line) == upLine:
        listOfLines.append(line)
        line = []
        upLine += 1

# Create a dummy list first to add to the bottom line. This should be the only change needed for the later problem.
# This list is updated with the new values from below it, so it holds the currenent highest values.
addList = [0] * 100
# Read the list from "bottom up"
for i in reversed(listOfLines):
    # Add the new highest values to the list above it
    i = np.add(addList, i)
    newLine = []
    listStop = 0
    # Check neighboring values and only append the highest one. 
    while listStop < len(i)-1 and len(i) > 1:
        if i[listStop] > i[listStop + 1]:
            newLine.append(i[listStop])
        else:
            newLine.append(i[listStop + 1])
        listStop += 1
    # This list should match the length of the next list which should be one shorter than the previous
    addList = newLine
    # Print the very last value (the highest)
    if len(i) == 1:
        print(i[0])


