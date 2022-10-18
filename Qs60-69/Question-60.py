'''
10/13/2022

Q: The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

A: 26033

'''

# Always recycle old code if it works! I mean, how many Euler prime questions are there?
def isPrimeFunc(num):
    if num == 1 or num%2 == 0 or num == 2 or num == 4 or num == 6 or num == 8:
        return False
    elif num == 3 or num == 5 or num == 7:
        return True
    else:
        for i in range(3, int(num**0.5)+ 1, 2):
            if num%i == 0:
                return False
                break
        else:
            return True

# Create a boolean list of primes - this is just really fast to calculate, don't need a million, but it's so fast that who cares
primeUpTo = 1_000_000
primeListTF = [True for i in range(0, primeUpTo)]
primeUp = 2
while primeUp*primeUp < primeUpTo:
    if primeListTF[primeUp] == True:
        for i in range(primeUp * primeUp, primeUpTo, primeUp):
            primeListTF[i] = False
    primeUp += 1

# Create a list of prime values to use
numPrimes, primeUp = [], 0
for i in primeListTF:
    if i == True:
        numPrimes.append(primeUp)
    primeUp += 1
# This is the amount of prime numbers, I slowly moved this up manually until a value was finally found
numPrimes = numPrimes[3:1070]

# My favorite import - except this time we are using combinations
from itertools import combinations
listOfPerms = []
for i in combinations(numPrimes, 2):
    # This is a good trick to the code - we know that both values must work, so only save one - example don't save (3,7) and (7,3) only save (3,7)
    if isPrimeFunc(int(str(list(i)[0]) + str(list(i)[1]))) == True and isPrimeFunc(int(str(list(i)[1]) + str(list(i)[0]))) == True:
        listOfPerms.append(i)

# A deep loop that checks to see that all of the new values match the value a from the list of perms
'''
I thought this might need a longer explanation, so here it is.
The above list, we know, contains values that work both ways, so if (7,109) works, we know that (109, 7) works. If one of them didn't work, neither value is saved.
This is really important for the loop below, we can then check if 7 to 109 works - we don't have to check the opposite.
The loop works like this - take the first tuple and append both values, we know both of these must work, next check the second part of the tuple as index 0. Loop through the matches
until index 0 also has a match with the original tuple index 0. Do this for the rest of the loop. If they all match, in the final loop append the values and print.
Follow the code and you'll see that it really isn't that complicated. Originally I tried to brute force but I estimated it would take a millenia to calculate all the possible
permutations - so this is much better.
'''
breakMe = False
for i in listOfPerms:
    for b in listOfPerms:
        finalList = [i[0], i[1]]
        if b[0] == i[1]:
            if (i[0], b[1]) in listOfPerms:
                for c in listOfPerms:
                    if c[0] == b[1]:
                        if (b[0], c[1]) in listOfPerms and (i[0], c[1]) in listOfPerms:
                            for d in listOfPerms:
                                if d[0] == c[1]:
                                    if (c[0], d[1]) in listOfPerms and (b[0], d[1]) in listOfPerms and (i[0], d[1]) in listOfPerms:
                                        finalList.append(b[1])
                                        finalList.append(c[1])
                                        finalList.append(d[1])
                                        print(sum(finalList))
                                        breakMe = True
                                        break
    if breakMe:
        break
