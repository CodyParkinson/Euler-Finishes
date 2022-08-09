'''
08/08/2022

A: The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

A: 25164150

'''

# Honestly this one is pretty self explanatory
soSquares = 0
soSum = 0

for i in range(1,101):
    soSquares += i**2
    soSum += i

soSum = soSum**2

print((soSquares-soSum)*-1)