'''
10/27/2022

Q: Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring? (See PE site for full question)

A: 6531031914842725

'''

# All original code - not super fast, but not slow enough that I would complain
# The trick to this problem is the 16 digit hint - a 10 must be on the outer ring as the inner ring duplicates, so it would be 17 digit.
final = 0

# This function returns a list of lists that do not contain 10, 10 cannot be duplicated, and the loop below will always have a 10 already
def createListForPerm(lst):
    returnList = []
    for i in lst:
        if 10 not in lst:
            returnList.append(i)
    return returnList

# Itertools again? You know it buddy, create a dictionary of lists with the same sum - only check lists that have the same sum
from itertools import permutations

numList = [1,2,3,4,5,6,7,8,9,10]
dictOfSums = {}
for i in permutations(numList, 3):
    if sum(list(i)) not in dictOfSums:
        dictOfSums[sum(list(i))] = []
        dictOfSums[sum(list(i))].append(list(i))
    else:
        dictOfSums[sum(list(i))].append(list(i))

# Loop through the dictionary and permutate the values that don't have 10
for i in dictOfSums:
    for x in dictOfSums[i]:
        # Since we know a 10 must exists - check it first - the ring is, well, a ring so it is cyclical, if it doesn't start with 10 skip it
        if x[0] != 10:
            continue
        permMe = createListForPerm(dictOfSums[i])
        sumPerms = permutations(permMe, 4) # Don't create a list of 5 values, only 4 because the 'x' list is already found - this greatly reduces permutations
        solutionsList = []
        for b in sumPerms:
            check = x
            for c in list(b): # Loop through the list of lists and make sure the last number matches the middle number of the next list
                if check[2] == c[1]:
                    check = c
                    if c == b[-1]:
                        if c[2] == x[1]:
                            for d in numList: # Make sure all values 1-10 present
                                if d not in x and d not in b[0] and d not in b[1] and d not in b[2] and d not in b[3]:
                                    break
                            else:
                                y = [x, b[0], b[1], b[2], b[3]]
                                solutionsList.append(y)
                else:
                    break

        # Concat the list to a single string - since 10 is always first, the list is sorted with the smallest value first
        for b in solutionsList:
            smallest = sorted(b)[0]
            q = b.index(smallest)
            sortedList = []
            while True:
                sortedList.append(b[q])
                q += 1
                if q > len(b)-1:
                    q = 0
                elif q == b.index(smallest):
                    break
            numStr = ''
            for c in sortedList:
                numStr += str(c[0]) + str(c[1]) + str(c[2])
            if int(numStr) > final:
                final = int(numStr)

print(final)