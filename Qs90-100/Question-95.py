'''
01/04/2024

Q: The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of
28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the poroper divisors of 284 is 220,
forming a chain of two numbers. FOr this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 -> 14288 -> 15472 -> 14536 -> 14264 -> 12496 ...

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.

A: 14316

'''

# Takes about a minute to solve. The problem does not necessarily 'find' the correct answer. 
# Instead, I found a relatively large chain and tested its lowest number on the Euler site.
# And it was correct!

# Only for square root
import math

# Used for testing of lower numbers for faster calculations early on
upTo = 1_000_000

# A dictionary was used to match numbers to their sums of divs, a list was used for easier searching
dictOfDivs = {}
listOfDivs = []
longestChain = []

# Simple loop to calculate the sums of divs
for a in range(2, upTo, 2):
    divs = set()
    for i in range(1, int(math.sqrt(a)) + 1):
        if a % i == 0:
            divs.add(i)
            divs.add(int(a/i))

    dictOfDivs[a] = sum(divs) - a
    listOfDivs.append(sum(divs) - a)

# Loop through dictionary and construct chains, break when chain repeats, and break if number isn't in dictionary
for i in dictOfDivs:
    count = [i]
    x = dictOfDivs[i]

    while x not in count:
        if x in listOfDivs and x < upTo and x % 2 == 0:
            count.append(x)
            x = dictOfDivs[x]
        else:
            break

    if count[0] == x and len(count) > len(longestChain):
        longestChain = count

        if len(longestChain) > 10:
            break

print(min(longestChain))