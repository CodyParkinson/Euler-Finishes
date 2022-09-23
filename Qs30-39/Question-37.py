'''
09/21/2022

Q: The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

A: 748317

'''

# Create a simple prime finder that returns True and False for values
def primeFinder(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num%2 != 0:
        for i in range(3, int(num/2)):
            if num%i == 0:
                return False
                break
        else:
            return True
    else:
        return False



# The value must start with 2,3,5,7. All other numbers will not be prime when going right to left. Don't check all the numbers once a prime is found add another number in front of it and check again to see if it is prime. Basically just concatinate the integers until a max value is found
primeRL = []
for i in [2,3,5,7]:
    checkPrimes1 = [i]
    checkPrimes2 = []
    while len(checkPrimes1) > 0:
        for c in checkPrimes1:
            for b in range(1,10, 2):
                num = str(c) + str(b)
                if primeFinder(int(num)):
                    checkPrimes2.append(num)
        checkPrimes1 = checkPrimes2
        checkPrimes2 = []
        for b in checkPrimes1:
            primeRL.append(b)

# Use the list from above and check what integers are also prime when going from left to right. Only need to check the values from above as they are the only ones that can be possible. Just gradually decrease the string and check to make sure it is prime. In the end you are left with a list that is 11 digits long, so just print the sum. 
primeLR = []
for i in primeRL:
    check = str(i)
    while len(check) > 1:
        check = check[1:]
        if primeFinder(int(check)) != True:
            break
    else:
        primeLR.append(int(i))

print(sum(primeLR))