"""
08/03/2022

Q: The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

A: 6857

"""

# Once a factor is found, divide out. At the end, you will be left with the highest number.
x = 600851475143
y = 3

while x > 1:
    if x%y == 0:
        x = x/y
    y += 2

# Subtract 2 because y will have 2 added to it before it checks and breaks the loop.
print(y-2)



