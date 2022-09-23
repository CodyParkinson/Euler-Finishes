'''
9/20/2022

Q: 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.

A: 40730

'''

# Always use math when possible, much faster than writing loops
import math

# Loop through values and find if factorials add up to num - honestly super easy
# I did cheat though and I just kept increasing the range by a factor of 10 until the sum stopped increasing, there is probabably a better "mathier" way to figure range
fac = 0
for i in range(3, 100000):
    total = 0
    for b in str(i):
        total += math.factorial(int(b))
    if total == i:
        fac += total
print(fac)