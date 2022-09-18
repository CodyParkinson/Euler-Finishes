'''
09/18/2022

Q: Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

A: 443839

'''

# Iterate through each number and add it together. I originally took it to 10 million, there is probably a better way to check but I dropped it down so it will run faster
listOfFifths = []
for i in range(10,450000):
    total = 0
    for b in str(i):
        total += int(b) ** 5
    if total == i:
        listOfFifths.append(i)
print(sum(listOfFifths))