'''
09/11/2022

Q: By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

A: 1074

'''

numbers = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

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
addList = [0] * 15
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