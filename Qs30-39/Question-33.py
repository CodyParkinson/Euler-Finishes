'''
9/19/2022

Q: The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

A: 100

'''
# Create a list of the cancelling fractions by checking numbers that have atleast one shared value
DCF = []
for i in range(10,100):
    for b in range(10,100):
        div = b/i
        checkVal = 0
        if str(i)[0] == str(b)[1] and '0' not in str(b) and '0' not in str(i):
            checkVal = int(str(b)[0])/int(str(i)[1])
        elif str(i)[1] == str(b)[0] and '0' not in str(b) and '0' not in str(i):
            checkVal = int(str(b)[1])/int(str(i)[0])

        if checkVal == div:
            DCF.append([i,b])

# Take out duplicates and same values
final = []
for i in DCF:
    if i[0] != i[1]:
        final.append(i)
    elif len(final) == 4:
        break

# Find the largest common factor
numer = 1
denom = 1
for i in final:
    numer *= i[0]
    denom *= i[1]
denomList = []
numerList = []
for i in range(1, numer):
    if (numer%i) == 0:
        numerList.append(i)
for i in range(1, denom):
    if (denom%i) == 0:
        denomList.append(i)
finalList = []
for i in numerList:
    if i in denomList:
        finalList.append(i)

# Flip the numerator and denominator, divide each by the highest common factor to get final answer
print(int((denom/max(finalList))/(numer/max(finalList))))

