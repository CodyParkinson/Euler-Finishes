'''
12/18/2023

Q: (See PE for full question) How many right triangles can be formed?

A: 14234

'''

# Takes ~10 seconds on my machine, very brute force

import itertools

upTo = range(51)
possible = 0

combs = list(itertools.product(upTo, repeat=2))

for i in combs:

    # Length of line from (0,0) - Line 1
    a = pow(i[0], 2) + pow(i[1], 2) 

    if i != (0,0):
        for j in combs:
            if j != (0,0):

                # Length of line from (0,0) - Line 2
                b = pow(j[0], 2) + pow(j[1], 2)

                # distance between the two points
                c = (pow((abs(j[0] - i[0])), 2) + pow((abs(j[1] - i[1])), 2))

                x = sorted([a, b, c])

                # Check if the points make a right triangle
                if i == j:
                    pass
                elif x[0] + x[1] == x[2]:
                    possible += 1

print(int(possible/2))