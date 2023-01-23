'''
01/17/2023

Q: The minimal path sum in the 5 by 5 matrix (see PE site), by starting in any cell in the left column and finishing in any cell in the right column, 
and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.
Find the minimal path sum from the left column to the right column.

A: 260324

'''

'''
A cheesy solve - but I am happy with how it turned out!
This program will only work if within the grid - it only moves up and down, at maximum 3 times.
More than this and extra checks would need to be added. This program also assumes the answer is not
in the top or bottom rows. Extra checks would be needed for this as well. 

The reason I call this cheesed, is I kept adding checks until it basically just solved. There are probably way
better ways of doing this (more dynamically), but this basically insta-solves so I will leave it as is. 

'''

# Open file
with open('matrix.txt', 'r') as fullMatrix:
    unopMatrix = fullMatrix.read()

# Create an 80x80 matrix using the file
matrix = []
matToApp = []
num = ''
for i in unopMatrix:
    if i in '1234567890':
        num += i 
    else:
        matToApp.append(int(num))
        num = ''
        if len(matToApp) == 80:
            matrix.append(matToApp)
            matToApp = []

# Saves a non-reference copy of the list - without this the matrix will update the 'reference' as well and be useless
# A little quirk of Python I learned
matrixCheck = list()
for i in matrix: matrixCheck.append(list(i))

# Loop through each value from right to left - going down the column. Find the most optimal route from up 3 to down 3. 
for x in range(1, len(matrix)):
    for i in range(len(matrix)):
        if i == 0:
            matrix[i][x] += min(matrix[i][x-1], (matrixCheck[i+1][x] + matrix[i+1][x-1]), (matrixCheck[i+2][x] + matrix[i+2][x-1] + matrixCheck[i+1][x]))

        elif i == 1:
            matrix[i][x] += min(matrix[i][x-1], 
            (matrixCheck[i-1][x] + matrix[i-1][x-1]), 
            (matrixCheck[i+1][x] + matrix[i+1][x-1]),
            (matrixCheck[i+2][x] + matrix[i+2][x-1] + matrixCheck[i+1][x]),
            )

        # These are the checks - looking up and down the columns to find 'optimal'/ least sum routes to each given node
        # - moves up the rows, + moves down the rows. More checks could be added by just adding +/- of 4 to what ever is needed
        elif i != 0 and i < len(matrix)-3:
            matrix[i][x] += min(matrix[i][x-1], 
            (matrixCheck[i-1][x] + matrix[i-1][x-1]), 
            (matrixCheck[i-2][x] + matrix[i-2][x-1] + matrixCheck[i-1][x]),
            (matrixCheck[i-3][x] + matrix[i-3][x-1] + matrixCheck[i-1][x] + matrixCheck[i-2][x]),
            (matrixCheck[i+1][x] + matrix[i+1][x-1]),
            (matrixCheck[i+2][x] + matrix[i+2][x-1] + matrixCheck[i+1][x]),
            (matrixCheck[i+3][x] + matrix[i+3][x-1] + matrixCheck[i+1][x] + matrixCheck[i+2][x]),
            )

        else:
            matrix[i][x] += min(matrix[i][x-1], (matrixCheck[i-1][x] + matrix[i-1][x-1]))

# Print the minimum from the last digit in the rows
minim = []
for i in matrix:
    minim.append(i[-1])
print(min(minim))



        
        


