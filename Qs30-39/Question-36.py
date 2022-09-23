'''
9/20/2022

Q: The decimal number, 585 = 1001001001(2) (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)

A: 872187

'''

# Find palindromes of numbers one to a million
palindromeNums = []
for i in range(1,1_000_000):
    if str(i)[::-1] == str(i):
        palindromeNums.append(i)

# Convert numbers from above into binary and check to see if they are also palidromic
final = []
for i in palindromeNums:
    binary = str(bin(i))[2:]
    if binary[::-1] == binary:
        final.append(i)

print(sum(final))
