'''
9/29/2022

Q: The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?

A: 997651

'''

# Instead of just creating a large list of primes up to a million, just check them with this function
def isPrime(num):
    for i in range(2,int(num/2)):
        if num%i == 0:
            return False
            break
    else:
        return True

# Still create a short list of primes in order to draw from for addition
listOfPrimes = [2,3]
for i in range(5, 5000, 2):
    for b in range(3,int(i/2),2):
        if i%b == 0:
            break
    else:
        listOfPrimes.append(i)

# Need to check the highest value, the highest consecuative value, and have a value to move the list to the next value to check for length
listUp = 0
highest = 0
plusHighest = 0
while listOfPrimes[listUp] < listOfPrimes[-2]:
    total = 0
    plusUp = 0
    for i in listOfPrimes[listUp:]:
        total += i
        plusUp += 1
        if total > 1_000_000:
            smallPrimes = listOfPrimes[:listOfPrimes.index(i) + 1]
            break
    # The above code will break a million, so the total needs to be walked back until a prime is found, save the highest value witht the highest consecuative
    minus = -1
    while True:
        total -= smallPrimes[minus]
        minus -= 1
        plusUp -= 1
        if isPrime(total):
            if total > highest and plusUp > plusHighest:
                highest = total
                plusHighest = plusUp
            break
    listUp += 1
print(highest)
