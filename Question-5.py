'''
08/08/2022

Q: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

A: 232792560

'''

# The number must go in increments of 20, becasue 20 has to divide out equally.
num = 20

# Create simple loop with a stop when a number is reached.
go = True
while go:
    num += 20
    for i in range(1,21):
        if num%i != 0:
            break
        if i == 20:
            print(num)
            go = False
