'''
01/20/2022

Q: The smallest number expressible as the sum of a prime square, prime cube, and prime 
fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2**2 + 2**3 + 2**4
33 = 3**2 + 2**3 + 2**4
49 = 5**2 + 2**3 + 2**4
47 = 2**2 + 3**3 + 2**4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, 
and prime fourth power?

A: 1097343

'''

# Generate primes - use itertools product to create all combinations of numbers - multiply and add to list

# Function to generate 3 prime lists
# Doing primes up to the sqrt(50mil) takes the program a few minutes to run vs. a second with 3 (see below)
def primeGen(x):

    # Sieve out the primes
    start = 0
    upTo = x
    primeListTF = [True for i in range(start, upTo)]
    primeUp = 2
    while primeUp*primeUp < upTo:
        if primeListTF[primeUp] == True:
            for i in range(primeUp * primeUp, upTo, primeUp):
                primeListTF[i] = False
        primeUp += 1

    # create a list of the prime numbers - instead of T/F
    primes, num = [], 0
    for i in primeListTF:
        if i == True:
            primes.append(num)
        num += 1
    return primes[2:]

# Back to the trusty itertools!
from itertools import product
testNum = 50_000_000
combs = product(primeGen(int(testNum**(1/2))+1), primeGen(int(testNum**(1/3))+1), primeGen(int(testNum**(1/4))+1)) 

# Create a list to track products:
prodList = [False]*testNum

# Loop and find product sums
for i in combs:
    y = list(i)
    z = y[0]**2 + y[1]**3 + y[2]**4
    if z < testNum:
        prodList[z] = True

print(prodList.count(True))
