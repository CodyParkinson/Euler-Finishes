'''
9/20/2022

Q: The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?

A: 55

'''

# Create a list of all numbers that do not contain an even number, if there is an even number it cannot be prime when circaling through it
numLists = []
evens = "02468"
for i in range(11,1_000_000):
    for b in str(i):
        if b in evens:
            break
    else:
        numLists.append(i)

# Loop through nums list to find all values that are prime - this also creates a list of all prime numbers under one million
primes = []
for i in numLists:
    for b in range(3, int(i/2), 2):
        if i%b == 0:
            break
    else:
        primes.append(i)

# Circle through all of the prime numbers, if the new circle number is not in the prime list, it is not prime
circular = []
for i in primes:
    primeCheck = str(i)
    for b in primeCheck:
        if int(primeCheck) not in primes:
            break
        primeCheck = primeCheck[1:] + primeCheck[0]
    else:
        circular.append(i)

# Started checking all 11, so add 4 to account for 2, 3, 5, 7 
print(len(circular) + 4)
    