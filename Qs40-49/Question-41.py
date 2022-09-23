'''
9/23/2022

Q: We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?

A: 7652413

'''

# Import itertools so we can easily find all permutations
import itertools

# So I kinda cheated (not really) but I found that 1-9 has no primes and neither does 1-8, but when I changed it to 1-7 - it gave a value which was correct
nums = ['1','2','3','4','5','6','7']
perms = itertools.permutations(nums)

# Loop through all iterations and see if it is prime, save the largest prime only
final = 0
for i in perms:
    number = int(''.join(i))
    if number % 2 != 0:
        for b in range(3, int(number/2), 2):
            if number % b == 0:
                break
        else:
            if number > final:
                final = number

print(final)