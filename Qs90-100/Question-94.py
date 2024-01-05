'''
01/03/2024

Q: It is easily proved that no equilateral triangle exists with integral length sides and integral area. 
However, the almost equilateral triangle 5 5 6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs 
by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose 
perimeters do not exceed one billion.

A: 518408346

'''

# This program takes a long time to run, but it does produce the right answer.
# It is based on the fact that the area must return an integer when calculting.
# No need to calculate the whole area, only need to calculate the square root portion.

# Just needed for square root
# isqrt returns an integer, so no floating points to calculate
import math

billion = 1_000_000_000
total = 0

# Run this for perimeter + 1
for i in range(3, billion, 2):
    x = (4 * (i**2)) - (i+1)**2
    y = math.isqrt(x)

    if x == y**2:
        peri = (i * 3) + 1
        if peri < billion:
            total += peri
        else:
            break

# Run this for perimeter - 1
for i in range(3, billion, 2):
    x = (4 * (i**2)) - (i-1)**2
    y = math.isqrt(x)

    # If the square root **2 == the original number, it is a perfect square
    if x == y**2:
        peri = (i * 3) - 1
        if peri < billion:
            total += peri
        else:
            break

print(total)