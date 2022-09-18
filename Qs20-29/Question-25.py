'''
09/11/2022

Q: The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

A: 4782

'''

# Create a list of the Fibonacci Sequence
listOfFibs = [1]
fib = 1
# Only calculate until the length of the number is greater than 999
while len(str(fib)) < 1000:
    fibNew = fib + listOfFibs[-1]
    listOfFibs.append(fibNew)
    fib = listOfFibs[-2]
# Print last index and add one, because once again, Python starts at index 0.
print(listOfFibs.index(fibNew) + 1)
