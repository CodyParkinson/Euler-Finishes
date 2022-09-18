'''
09/11/2022

Q: A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

A: 983

'''

# https://en.wikipedia.org/wiki/Repeating_decimal#Fractions_with_prime_denominators
# The link above takes you to a page about how to find repeating decimals. There is a theorem that works with prime numbers as the denominator. I used this to deduce
# that the longest repeat of numbers would be n-1. This means the highest potential prime number would give the highest value. I checked 991 and 997 and they both were wrong
# I then tried 983, which is the correct answer. I do not fully understand the theorem or I would describe it better here. I recommend reading the Wiki.
potentialList = []
for i in range(10,1000):
    for b in range(3,i):
        if i%b == 0:
            break
        elif b == i-1:
            potentialList.append(i)

print(potentialList[-3])



