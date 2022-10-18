'''
10/12/2022

Q: It is possible to show that the square root of two can be expressed as an infinite continued fraction.
In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

A: 153

'''

'''
One of the coolest problems to solve - this is a great example of "math is weird"!
So, don't do any wacky coding or try to solve the problem with brute force, just know the next numerator in series is == to the previous num + previous den*2
So, 3/2 -> (3+(2*2))/(3+2) = 7/5 -> (7+(5*2))/(7+5) = 17/12 ... 
'''

num, den, total = 3, 2, 0
for i in range(1000):
    num, den = num + den*2, num + den
    if len(str(num)) > len(str(den)): total += 1
print(total)
    
