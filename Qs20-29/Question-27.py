'''
09/18/2022

Q: Euler discovered the remarkable quadratic formula:

n**2 = n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0<= n <= 41. However, when n=40, 40**2 + 40 + 41 = 40(40+1) is divisible by 41, and certainly when n=41, 41**2 + 41 + 41 is clearly divisible by 41.

The incredible formula n**2 - 79n +1601 was discovered, which produces 80 primes for the consecutive values 0<=n<=79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:
n**2 + an + b, where |a| < 1000 and |b| <= 1000

where |n| is the modulus/absolute value of n
e.g. |-1| = 1
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

A: -59231

'''

# list of the largest prime consecs.
largestConsec = 0
BigA = 0
BigB = 0

# This is just a prime number check, used this instead of doing it inline to make it look cleaner
def primeCheck(number):
    for i in range(3, round(number/2 + 2), 2):
        if number % i == 0:
            return False
            break
        elif i > number/2:
            return True
            break

# Loop through all the values
for a in range (-999, 1000):
    for b in range(-1000, 1001):
        # Only check if b is also a prime, as when you plug in zero, b will be the only value, so it must be prime
        if abs(b)>1 and primeCheck(abs(b)):
            isPrime = True
            currentNum = 0
            primeUp = 0
            while isPrime:
                num = abs(currentNum**2 + a * currentNum + b)
                if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num <= 1:
                    isPrime = False
                else:
                    isPrime = primeCheck(num)
                    if isPrime == True:
                        primeUp += 1
                currentNum += 1
                if primeUp > largestConsec:
                    largestConsec = primeUp
                    BigA = a 
                    BigB = b
# Prints a negative number which is correct
print(BigA*BigB)
