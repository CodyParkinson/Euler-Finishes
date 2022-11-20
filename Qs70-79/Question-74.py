'''
11/15/2022

Q: The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

A: 402

'''

# This problems takes a few seconds to run, so patience is a virtue
import math

# Create a function that takes in a num and returns the sum of its factorials
def addFacts(num):
    total = 0
    for i in str(num):
        total += math.factorial(int(i))
    return total

# Loop numbers and if their sum is not in the list, add it to the list, if it is - break. 
# The problem states that the longest chain is 60, so once a chain is == len(60), break it and add to the total
total = 0
for i in range(1, 1_000_000):
    listOfNums = [i]
    while True:
        i = addFacts(i)
        if i not in listOfNums:
            listOfNums.append(i)
            if len(listOfNums) == 60:
                total += 1
                break
        else:
            break

print(total)


