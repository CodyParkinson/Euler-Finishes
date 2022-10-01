'''
9/27/2022

Q: It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2x1**2
15 = 7 + 2x2**2
21 = 3 + 2x3**2
25 = 7 + 2x3**2
27 = 19 + 2x2**2
33 = 31 + 2x1**2

It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

A: 5777

'''

# Create a list of primes
listOfPrimes = [3]
for i in range(5, 10000, 2):
    for b in range(3,int(i/2),2):
        if i%b == 0:
            break
    else:
        listOfPrimes.append(i)

# Loop through an arbitrary amount of numbers until a break occurs
for i in range(9, 10000, 2):
    finalCheck = False
    if i not in listOfPrimes:
        check = False
        # Loop through primes and values until the value is equal or greater than 'i'
        for b in listOfPrimes:
            if b < i:
                total = 0
                for c in range(1,100):
                    total = b + 2*(c**2)
                    if total == i:
                        check = True
                    elif total > i or check == True:
                        break
            if check == True:
                break
            # if a value is not found and 'b's are greater than i, break out and print value
            elif check == False and b > i:
                finalCheck = True
                print(i)
                break
    if finalCheck == True:
        break
                
