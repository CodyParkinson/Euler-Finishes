'''
9/19/2022

Q: We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

A: 45228

'''

# Create a list of the products to turn into a set later - easy way to check for duplicates
listOfPan = []

# Loop through numbers to get all combinations
for i in range(1,2000):
    for b in range(1,1000):
        nums = "123456789"
        x = i*b 
        multString = str(x) + str(i) + str(b)
        # If a 0 is in the num, it is not pandigital per the requirements. The length of the string also must be 9.
        if '0' not in multString and len(multString) == 9:
            for c in nums:
                if c not in multString:
                    break
                elif c == '9' and c in multString:
                    listOfPan.append(x)

# Create a set and print the total of the sums
setPan = set(listOfPan)
total = 0
for i in setPan:
    total += i
print(total)

