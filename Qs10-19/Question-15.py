'''
08/29/2022

Q: Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

A: 137846528820

'''

# A little bit of statistics make this very nice - use the combination equation.
import math
print((math.factorial(40))/(math.factorial(20)*math.factorial(20)))
