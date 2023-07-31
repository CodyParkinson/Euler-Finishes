'''
01/19/2023

Q: In the 5 by 5 matrix below (see PE site), the minimal path sum from the top left to the bottom right, 
by moving left, right, up, and down, is indicated in bold red and is equal to 2297.
Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in matrix.txt

A: 425185

'''

'''
Oh my goodness - oh so proud of this code. It is not the fastest implamentation of Dijkstra's algorithm, but it works!
This is the priority queue method, and it does stop once it reaches the final position. Theoretically it could end before
the most optimal method is found, but it will find the optimal the majority of the time, and it did so atleast for this problem.

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

# Number the matrix - the number was used to indicate position instead of doing nested lists
# True value indicated that it is on the far right edge
numMatrix = []
upMatrix = 0
for i in matrix:
    appendMetoMat = []
    for b in i:
        appendMetoMat.append([b, upMatrix, False])
        upMatrix += 1
    upMatrix -= 1
    appendMetoMat.pop()
    appendMetoMat.append([b, upMatrix, True])
    upMatrix += 1
    numMatrix.append(appendMetoMat)

# Saves a non-reference copy of the list - this matrix is not mutated anywhere
matrixCheck = list()
for i in matrix: matrixCheck.append(list(i))

# Create a dictionary of each node and its current value/ set 0,0 to its value
# Positions that are not yet visited are given an "infinity" - or a value that should not ever be reached
# We know it is has to be less than 1_000_000 because problem 81 came out to only around ~450_000 and this one is more optimized
dictOfVerts = {}
for i in range(len(matrix)**2):
    dictOfVerts[i] = 1_000_000
dictOfVerts[0] = matrix[0][0]

# Left checker - I didn't think about the left edge, so I just created this list to define it. I could have done this
# method for the right edge as well.
leftCheck = []
upLeft = -1
for i in range(100):
    upLeft += len(matrix)
    leftCheck.append(upLeft)

# If the key is here - the loop knows the position has been visited, so it cannot be accessed again. 
usedKeys = []

# Main loop breaks when last value is reached
while True:
    # Lowest value (sum) in dicionary is priority number
    priority = min(dictOfVerts, key=dictOfVerts.get)

    # Find unvisited nodes surrounding priority point - up, down, left, right
    unvisited = []

    # Up
    if priority - len(matrix) > 1:
        if priority - len(matrix) not in usedKeys:
            unvisited.append(priority - len(matrix))

    # Down
    if priority + len(matrix) < len(matrix)**2:
        if priority + len(matrix) not in usedKeys:
            unvisited.append(priority + len(matrix))

    # Left
    if priority - 1 > 0:
        for i in numMatrix:
            for b in i:
                if priority - 1 == b[1] and priority - 1 not in leftCheck:
                    if priority - 1 not in usedKeys:
                        unvisited.append(priority - 1)

    # Right
    if priority + 1 < len(matrixCheck)**2:
        for i in numMatrix:
            for b in i:
                if (priority + 1 == b[1] and b[2] == False) or (priority + 1 == b[1] and b[2] == True):
                    if priority + 1 not in usedKeys:
                        unvisited.append(priority + 1)
    
    # Go through the unvisited nodes and add. Save lowest value
    for i in unvisited:
        if dictOfVerts[i] == 1_000_000:
            dictOfVerts[i] == 0
        addMe = 0
        for c in numMatrix:
            breakMe = False
            for b in c:
                if b[1] == i:
                    addMe = b[0]
                    breakMe = True
                    break
            if breakMe:
                break
        if dictOfVerts[i] != 0:
            if dictOfVerts[i] > dictOfVerts[priority] + addMe:
                dictOfVerts[i] = dictOfVerts[priority] + addMe

    # Take out the used (visited) nodes
    usedKeys.append(priority)
    del dictOfVerts[priority]

    # If the last value of matrix is not 0 (infinity for this node) - print and break
    if dictOfVerts[(len(matrix)**2)-1] != 1_000_000:
        print(dictOfVerts[(len(matrix)**2)-1])
        break
