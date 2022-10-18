'''
10/17/2022

Q: The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

A: 127035954683

'''

# Create a list of cubes up to 10,000 - sort the cubes numerically and save this value
listOfCubes = []
for i in range(10_000):
    listOfCubes.append(sorted(str(i**3)))

# Turn the list into a "Set" - can't use set() because it is a list of lists
setOfCubes = []
for i in listOfCubes:
    if i not in setOfCubes:
        setOfCubes.append(i)

# If the sorted numerical list matches another one, we know it is a permutation of the cube - if we find 5 of them print the index ** 3 to get the number
for i in setOfCubes:
    numOfSames = 0
    for b in listOfCubes:
        if b == i:
            numOfSames += 1
    if numOfSames >= 5:
        print(listOfCubes.index(i)**3)
        break