'''
08/08/2022

Q:By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

A: 104743

'''

# A very simple way of finding prime numbers, does not detect even integers, so only feed odds
def findPrime(x):
    for i in range(3,int((x/2))+2, 2):
        if x%i == 0:
            return False
        elif i >= (x/2):
            return x

# Create a list of prime numbers up to 10,001
listOfPrimes = [2,3,5,7,11,13]
start = 13

while len(listOfPrimes) < 10001:
    start += 2
    check = findPrime(start)
    if check != False:
        listOfPrimes.append(start)

# Print 10,000 because python starts checking lists at position 0
print(listOfPrimes[10000])
