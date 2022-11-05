'''
11/4/2022

Q: Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

A: 8319823

'''

# A slow solve, so be prepared to wait a minute. A very fun problem with some tricks that could be improved upon for better performance.
# I used https://en.wikipedia.org/wiki/Euler%27s_totient_function to solve the problem

# Create a list of primes, a prime number cannot be the answer, so this is a fast way to check 10**7 primes and be able to skip them
start = 0
upTo = 10_000_000
primeListTF = [True for i in range(start, upTo)]
primeUp = 2
while primeUp*primeUp < upTo:
    if primeListTF[primeUp] == True:
        for i in range(primeUp * primeUp, upTo, primeUp):
            primeListTF[i] = False
    primeUp += 1


def factors(num, dnc):
    # Check if prime, if so, skip
    if primeListTF[num] != True:
        # Create a list of the factors using the method in the above wiki
        listOfFactors = []
        # Pull out any evens
        while num % 2 == 0:
            listOfFactors.append(2)
            num = int(num / 2)
        # Find the rest of the distinct prime factors
        for i in range(3,int(num**0.5)+1,2):
            while num % i== 0:
                listOfFactors.append(i)
                num = int(num / i)
        if num > 2:
            listOfFactors.append(num)

        # total is the actual amount from the phi function
        total = 1
        for i in set(listOfFactors):
            total *= int(((i**(listOfFactors.count(i)-1)) * (i-1)))

        # Turn the total and original number into lists, sort the lists, and they should be the same, if they are, they are permutations
        listOfInts = sorted(list(str(total)))
        if sorted(list(str(dnc))) == listOfInts:
            # Return the division to find the lowest value
            return dnc/total, dnc

    
    

x,z = 10,0
# Only check odd numbers -> This was really more of a guess based on earlier testing of the code, I noticed all the perms were odd, so I figured it also had to be
for i in range(1, 10_000_000, 2):
    y = factors(i, i)
    if y != None:
        if y[0] < x:
            x = y[0]
            z = y[1]

print(z)
