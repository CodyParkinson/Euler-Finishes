'''
07/30/2023

Q: Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 
2-digit numbers.

For example, the square number 64 could be formed by placing a 6 next to a 4.

In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 
01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing (0,5,6,7,8,9) on one cube and (1,2,3,4,8,9) on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like (0,5,6,7,8,9)
and (1,2,3,4,6,7) allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

(1,2,3,4,5,6) is equivalent to (3,6,4,1,2,5)
(1,2,3,4,5,6) is distinct from (1,2,3,4,5,9)

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set (1,2,3,4,5,6,9) 
for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?

A: 1217

'''

'''
I must admit I had no idea what this question was asking, and after 3 days of trying, I decided to look for other help.
I ended up looking at a hint at - https://blog.dreamshire.com/project-euler-90-solution/ - Well I took more than a hint,
and I ended up rewriting the code as to learn how it worked. This really is a very easy combinations problem, so maybe
I will come back later and try to optimise the code a bit in my own way. For now, I am just happy to be onto the next!

'''

# Combinatorics baby!
from itertools import combinations

# List of square numbers represented as tuples of required digits
squareNumbers = [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5), (3, 6), (4, 6), (8, 1)]

# Generate all possible combinations of digits on a cube
allCubeCombinations = list(combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 6], 6))

def isValidArrangement(cube1, cube2):
    # Check if all square numbers can be formed using the given digits on the two cubes
    for digit1, digit2 in squareNumbers:
        if (digit1 in cube1 and digit2 in cube2) or (digit1 in cube2 and digit2 in cube1):
            continue
        return False
    return True

def countValidArrangements():
    validCount = 0
    # Iterate through all cube combinations
    for i, cube1 in enumerate(allCubeCombinations):
        # Avoid redundant checks by only considering combinations before the current index
        for cube2 in allCubeCombinations[:i]:
            if isValidArrangement(cube1, cube2):
                validCount += 1
    return validCount

# Call the function to get the result
final = countValidArrangements()
print(final)


