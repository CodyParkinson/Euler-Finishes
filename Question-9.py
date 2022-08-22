'''
08/21/2022

Q: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

A: 31875000

'''

# Create variables to hold the a and b values. We don't need to save c as it is calculated each time
a = 1
b = 2

while True:
    # Since we know that a<b, we just check a up to b, then we step up b while resetting a to 1
    if a < b:
        a += 1
    elif a == b:
        a = 1
        b += 1
    
    # C is actuall c^2, so we have to take the square root of it to actually get c
    c = a**2 + b**2
    if a + b + c**.5 == 1000:
        print(a*b*(c**.5))
        break