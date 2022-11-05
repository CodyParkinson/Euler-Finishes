'''
9/27/2022

Q: Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 - 22 = 48, is not pentagonal.
Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk - Pj| is minimised; what is the value of D?

A: 5482660

'''

# Create a list of an arbitrary amount of pentagon numbers
pentNums = []
for i in range(1,10_000):
    pentNums.append(int((i*((3*i)-1))/2))

# Loop through the lists (set the second loop to start where the first starts to stop duplicate checks) and see what values can go both ways
# This loop is slow and could be optimized 10 fold, so if you run it, be prepared to wait a bit
for i in pentNums:
    check = False
    for b in pentNums[pentNums.index(i):]:
        if i + b in pentNums:
            if abs(i-b) in pentNums:
                print(abs(i-b))
                check = True
    if check:
        break
                

    