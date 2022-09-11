'''
09/11/2022

Q: A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

A: 4179871

'''

# First thing to do is make a list of all of the abundant numbers for use in checking 
listOfAbundants = []
for i in range(3, 28124):
    sumOfNums = 0
    for b in range(1, i):
        if i%b == 0:
            sumOfNums += b
    if sumOfNums > i:
        listOfAbundants.append(i)

# Go through the numbers 1-28124 and check to see if any combination of the numbers in the abundant list add up to this number
listOfSumNonAb = [1,2]
for i in range(3, 28124):
    for b in listOfAbundants:
        plus = i - b
        if plus < 0:
            listOfSumNonAb.append(i)
            print(i)
            break
        elif plus in listOfAbundants:
            break

# This program is VERY slow to run. It is not optimized in the least, so if you do run it, know it takes a few minutes.
print(sum(listOfSumNonAb))

