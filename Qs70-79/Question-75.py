'''
11/16/2022

Q: It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

A: 161667

'''

'''
This problem gave me quite the headache. From the beginning I was using https://en.wikipedia.org/wiki/Pythagorean_triple#Enumeration_of_primitive_Pythagorean_triples
to find ways to generate pythagorean triples. My problem was I was still checking too many numbers. I learned from https://www.mathblog.dk/project-euler-75-lengths-of-wire-right-angle-triangle/ that you only have to generate numbers up to m**0.5. This sped it up dramatically. This makes sense too because
you can up scale each of the triplets to form a new triplet, triplet + triplet == new triplet. Keep doing this. You only have to check unique values up to sqrt(1.5mil)

'''

# Pythagorean Triplets man
import math

# Create a list of 0's. add 1 to the index of the perimeter as it is found. 
listOfSides = [0] * 1_500_001

# Loop up to square root of 1.5mil
for i in range(2, int((1_500_000)**0.5)):
    for d in range(1, i):
        # The numbers must be coprime and they have to equal an odd number (explained very well in wiki)
        if math.gcd(i, d) == 1 and (i+d)%2 == 1:
            a = i**2 - d**2
            b = i**2 + d**2
            c = 2*d*i 

            # SumUp is the perimeter. Move it up by adding the original sum to get new triplets
            sumUp = sum([a,b,c])
            while sumUp < 1_500_001:
                listOfSides[sumUp] += 1
                sumUp += a + b + c

# Print the total amount of 1's, if it is not 1, there were multiple triplets found for that perimeter
print(listOfSides.count(1))


















'''
listOfSquares = []
for i in range(1, 1_500_001):
    listOfSquares.append(i**2)


triplets = []
for i in listOfSquares:
    for b in listOfSquares[listOfSquares.index()]:
        if i-b < 0 or i+b > 1_500_00:
            break
        if i-b in listOfSquares:
            x = sorted([int((i-b)**0.5), int(i**0.5), int(b**0.5)])
            if x not in triplets:
                triplets.append(x)

dictOfSums = {}
for i in triplets:
    if sum(i) not in dictOfSums:
        dictOfSums[sum(i)] = [i]
    else:
        dictOfSums[sum(i)].append(i)

total = 0
for i in dictOfSums:
    if len(dictOfSums[i]) == 1:
        total += 1

print(total)
'''