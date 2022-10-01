'''
9/27/2022

Q: The first two consecutive numbers to have two distinct prime factors are:
14 = 2 x 7
15 = 3 x 5
The first three consecutive numbers to have three distinct prime factors are:
644 = 2² x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.
Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

A: 134043

'''

# Create a list of primes to check
listOfPrimes = [2,3]
for i in range(5, 1000, 2):
    for b in range(3,int(i/2),2):
        if i%b == 0:
            break
    else:
        listOfPrimes.append(i)

# Loop through an arbitrary amount of numbers until break
# The trick is to keep checking a number to see if a prime goes into it multiple times, example: 8  2*2*2, but this is only a prime factor of 2, so 2 needs checked multiple times
# Once a prime is checked for multiples, just loop through primes list until basically primeCheck = 1
primos = []
for i in range(10,10000000):
    iPrimes = []
    primeCheck = i
    for b in listOfPrimes:
        check = True
        while check:
            if b <= primeCheck:
                if primeCheck % b == 0:
                    iPrimes.append(b)
                    primeCheck = int(primeCheck/b)
                else:
                    check = False
            else:
                check = False

    # If set length == 4, append number to primos list. Once length of primos == 4, break and print the first value
    if len(set(iPrimes)) == 4:
        # Append first value
        if len(primos) == 0:
            primos.append(i)
        # If the previous value is one less than the current, append it
        elif primos[-1] == i - 1:
            primos.append(i)
        # If the values are not touching, reset primos, but make sure to append the new value
        else:
            primos = []
            primos.append(i)
        
        if len(primos) == 4:
            print(primos[0])
            break
    