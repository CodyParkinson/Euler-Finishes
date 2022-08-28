'''
08/28/2022

Q: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

A: 142913828922

'''

# Start at 17 to match when the range starts
primeSum = 17

# Only need to check odd numbers, could be optimized by automatically not checking multiples of 5, but this works pretty fast otherwise
for i in range (9, 2_000_000, 2):

    # Check only to the square root of "i" - past this, all possible numbers have been checked
    for b in range(3, i, 2):
        if i%b == 0:
            break

        # If b**2 is greater than "i" - add it to the primeSum
        elif (b**2) > i:
            primeSum += i
            break

# Solution could be optimized much better - so give it a few seconds to load
print(primeSum)