'''
9/22/2022

Q: If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?

A: 840

'''

# Createa a dictionary perimeters as keys and side lengths as values
dictOfVals = {}
for a in range(1,500):
    for b in range(a+1,500):
        c = (a**2 + b**2)**(1/2)
        # Verify that c is a whole integer - if not, pass
        if int(c) == c:
            c = int(c)
            perimeter = a + b + c
            if perimeter <= 1000:
                if perimeter not in dictOfVals:
                    dictOfVals[perimeter] = []
                    dictOfVals[perimeter].append([a, b, c])
                else:
                    dictOfVals[perimeter].append([a, b, c])

highest = 0
num = 0
for i in dictOfVals:
    if len(dictOfVals[i]) > highest:
        highest = len(dictOfVals[i])
        num = i

# Print the key with the highest amount of values
print(num)
