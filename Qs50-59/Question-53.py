'''
10/10/2022

Q: There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (5..3) = 10

In general, (n..r) = n!/r!(n-r)!, where r <= n, n! = n * (n-1) * 3 * 2 * 1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: (23..10) = 1144066.

How many, not necessarily distinct, values of (n..r) for 1 <= n <= 100 are greater than one-million?

A: 4075

'''

# Just use the math method and loop through each iteration with the formula above
import math

total = 0
for i in range(20, 101):
    for b in range(1, i + 1):
        if  math.factorial(i)/(math.factorial(b)*math.factorial(i-b)) > 1_000_000:
            total += 1

print(total)