'''
11/17/2022

Q: It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?

A: 71

'''

# Create an arbitrary length list of primes 
upTo = 1_000_000
primeListTF = [True for i in range(0, upTo)]
primeUp = 2
while primeUp*primeUp < upTo:
    if primeListTF[primeUp] == True:
        for i in range(primeUp * primeUp, upTo, primeUp):
            primeListTF[i] = False
    primeUp += 1

# Create a function to find all the primes up to a specific number
def getPrimes(num):
    primeList = []
    for i in range(2, num):
        if primeListTF[i]:
            primeList.append(i)
    return primeList

# Use the code from problem 31. total = input number, coins = all primes up to given number
def findSums(num):
    total = num
    coins = getPrimes(num)
    combList = [1]
    combList += [0]*total
    for i in coins:
        for b in range(i, total+1):
            combList[b] += combList[b-i]
    return combList[-1]

# Loop arbitrary amount of numbers until the amount of sums > 5k.
for i in range(10, 1_000_000):
    if findSums(i) > 5000:
        print(i)
        break