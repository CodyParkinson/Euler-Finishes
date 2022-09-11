'''
09/11/2022

Q: Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

A: 31626

'''

# Create a dictionary of all values under 10000 with the sum of their divisors
dictOfValues = {1:1}
for i in range(2, 10000):
    sumOfDivs = 0
    for b in range(1, i):
        if i%b == 0:
            sumOfDivs += b
    dictOfValues[i] = sumOfDivs

# Iterate through the dictionary. If they match like how it states in the question - add it to the list and print the sum at the end
amicables = []
for i in dictOfValues:
    check = dictOfValues[i]
    if check < 10000:
        if i == dictOfValues[check] and check == dictOfValues[i] and i != check:
            amicables.append(i)

print(sum(amicables))