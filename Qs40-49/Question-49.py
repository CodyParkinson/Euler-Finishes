'''
9/27/2022

Q: The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?

A: 296962999629

'''

# Create a list of primes to check only check those that are 4 digits long
listOfPrimes = []
for i in range(1001, 10000, 2):
    for b in range(3,int(i/2),2):
        if i%b == 0:
            break
    else:
        listOfPrimes.append(str(i))

# Use the trusty itertools to find permutations of the prime numbers, create a list of permutations that are also prime
from itertools import permutations
listOfPerms = []
for i in listOfPrimes:
    checkList = []
    checkList.append(i)
    for b in permutations(i, 4):
        b = ''.join(list(b))
        if b != i:
            if b in listOfPrimes:
                checkList.append(b)
    # Create a set of primes so values are only counted once
    if len(set(checkList)) >= 3:
        listOfPerms.append(set(checkList))

# Sort the list to make it easier to find value differences
finalList = []
for i in listOfPerms:
    if sorted(i) not in finalList:
        finalList.append(sorted(i))

# Loop through the sorted list and find if the difference between values is the same
for i in sorted(finalList):
    broken = False
    if len(i) == 3:
        if int(i[1]) - int(i[0]) == int(i[2]) - int(i[1]):
            print(''.join(i))
    # If there are more than 3 permuations that are prime, they need to be check, use itertools again to find permutations with length of 3
    for b in permutations(i,3):
        if int(b[1]) - int(b[0]) == int(b[2]) - int(b[1]):
            # This is just clean up code so the answer looks pretty, without this it will print 4 values, the original value, found value and the reverse due to permutation rules
            if ''.join(list(b)) == '148748178147' or ''.join(list(b)) == '814748171487':
                pass
            else:
                print(''.join(list(b)))
                broken = True
                break
    if broken:
        break

    
