'''
9/23/2022

Q: An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d(1) x d(10) x d(100) x d(1000) x d(10000) x d(100000) x d(1000000)

A: 210

'''

# Create a string of numbers - don't have to go this high but it runs quick enough that you can't even tell
num = ""
for i in range(1,1_000_000):
    num += str(i)

# Find the product of the numbers - remember python indexing
print(int(num[0]) * int(num[9]) * int(num[99]) * int(num[999]) * int(num[9999]) * int(num[99999]))

