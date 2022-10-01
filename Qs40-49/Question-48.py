'''
9/27/2022

Q: The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

A: 9110846700

'''

# Thank goodness for the power of computers!
total = 0
for i in range(1,1001):
    total += i**i
print(str(total)[-10:])