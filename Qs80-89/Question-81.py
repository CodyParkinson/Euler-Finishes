'''
12/2/2022

Q: In the 5 by 5 matrix (see PE site), the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
Find the minimal path sum from the top left to the bottom right by only moving right and down.

A: 427337

'''

# Very similar to question 18, don't calculate all routes, just add together both possible routes to a single point and keep the smallest one

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

# The first line of the matrix must be calculated first
throughMat = []
ver = 0
for i in matrix[0]:
    ver += i
    throughMat.append(ver)
newMatrix = throughMat

# Move down the matrix. If the number to the left is smaller, add that one, else add the one above it
for i in matrix[1:]:
    throughMat = []
    times = 0
    for b in i:
        if times == 0:
            throughMat.append(b + newMatrix[0])
        else:
            if throughMat[-1] < newMatrix[times]:
                throughMat.append(throughMat[-1] + b)
            else:
                throughMat.append(newMatrix[times] + b)
        times += 1
    newMatrix = throughMat

print(newMatrix[-1])
