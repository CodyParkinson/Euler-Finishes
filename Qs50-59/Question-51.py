'''
10/7/2022

Q: By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

A: 121313

'''

'''
So I am quite proud of this code - I ended up working on this problem for about a week before I had to look up a hint. My problem was that I did not read the question closely enough. I had it stuck in my head that you had to replace two digits in the number. I started looking for numbers in the 10's of billions, but I had no luck. Finally, I found this site https://www.mathblog.dk/project-euler-51-eight-prime-family/ looking for a hint. It immediatly hit me when looking over their analysis that I did not think to check more than two number positions. As soon as I figured this out, I only had to change a few numbers, which I have labeled below, and the number came out super easy. Goes to show that you should ALWAYS really read the question before going after a solution. 
'''

# Sieve Method - After some good research, I have settled on a new method of developing Primes - Sieve of Eratosthenes
# This creates a boolean list of primes - the index corresponds to the number value 
# upTo is arbitrary and I manually changed it depending on what numbers I am checking - continued to just move it up until I solved the problem. 
start = 0
upTo = 1_000_000
primeListTF = [True for i in range(start, upTo)]
primeUp = 2
while primeUp*primeUp < upTo:
    if primeListTF[primeUp] == True:
        for i in range(primeUp * primeUp, upTo, primeUp):
            primeListTF[i] = False
    primeUp += 1


# This creates a dictionary list that is used to add to the 0's that are found 
# I created this because I was manually changing the values of the dictionary a lot when testing different lengths of numbers - this made it easier to add and delete
#   But a manual dictionary would also have worked
from itertools import permutations
permListValues = [100_000, 10_000, 1_000, 100, 10]
permDic = {}
for i, b in zip(range(len(permListValues) + 1), permListValues):
    permDic[i] = b


# The loop of the numbers - loop through all odds from range upTo/10 to keep the length of the number the same so it matches the permutation dictionary
breakMe = False
for i in range(int(upTo/10) + 1, upTo, 2):
    if breakMe:
        break
    # Numbers must have repeats in it or don't check - use the repeat to add to - I use 1's so I don't accidentally start with a 0 - which shortens the length of the number
    # Little snip I liked from Geeks for Geeks
    isOne = [i for i, one in enumerate(str(i)) if one == '1']
    # If there is more than three 1's, I use permutations to check the combinations of values - the final number must be the same so skip permutations that end in a 1
    if len(isOne) >= 3 and isOne[-1] != 5:
        permsOfIndex = list(permutations(isOne, 3))
        permsOfIndexShort = []
        for d in permsOfIndex:
            if sorted(d) not in permsOfIndexShort:
                permsOfIndexShort.append(list(d))
        # Not the most efficient, but take the number convert to string to list, change value to 0 (if not first), and convert back to integer
        for b in permsOfIndexShort:
            check = list(str(i))
            if b[0] != 0:
                check[b[0]] = '0'
                check[b[1]] = '0'
            check = int(''.join(check))
            listOfPrime = []
            # Another zero check and if it ends in 5, it can't be prime so skip
            if check > int(upTo/10) and check % 5 != 0:
                # Add the permDic values to the number and check if it is in the prime list - because it is multiples of 10, can just add the perm dictions to the last to move up
                for c in range(0, 10):
                    if check < upTo:
                        if primeListTF[check] == True:
                            listOfPrime.append(check)
                    check += permDic[b[0]] + (permDic[b[1]]) + (permDic[b[2]])
            # Print i, as it will be the smallest value, and break the loops
            if len(listOfPrime) == 8:
                breakMe = True
                print(i)
            
            listOfPrime = []