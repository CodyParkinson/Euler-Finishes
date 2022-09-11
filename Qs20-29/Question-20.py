'''
09/11/2022

Q: n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

A: 648

'''

# Thank goodness for the power of computers
import math
bigNum = str(math.factorial(100))
sumOfNum = 0
for i in bigNum:
    sumOfNum += int(i)
print(sumOfNum)