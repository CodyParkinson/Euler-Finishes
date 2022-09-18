'''
09/18/2022

Q: Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

A: 669171001

'''

# First find the area of the square. This is how many numbers you'll have to generate
areaOfSquare = 1001 * 1001
listOfSquare = []
for i in range(1, areaOfSquare+1):
    listOfSquare.append(i)

# Next, need to generate a list of the diags. The pattern is every time you move to the next outer ring, each diagonal is 2 more numbers away than the previous circle
listOfDiags = [1]
move = 2
moveUp = 2
check = 0
for i in listOfSquare:
    if move > len(listOfSquare):
        break
    listOfDiags.append(listOfSquare[move])
    move+=moveUp
    check+=1
    if check == 3:
        moveUp += 2
        # Negative one, because the first circle checks only the first three since '1' was appended up top before it even starts. It then needs to check 4 moves
        check = -1
print(sum(listOfDiags))