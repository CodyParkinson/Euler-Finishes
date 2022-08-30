'''
08/29/2022

Q: The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
Once the chain starts the terms are allowed to go above one million.

A: 837799

'''

# Need to keep track of the longest chain and the current number
longestChain = 0
largestNum = 0
num = 14

# Run until num reaches one million. This is not a very efficient program - it takes a few seconds (Maybe 30) to run
while num < 1_000_000:
    check = num
    chain = 0
    while check != 1:
        if check%2 == 0:
            check = check/2
        else:
            check = check*3 + 1
        chain += 1
    if chain > longestChain:
        longestChain = chain
        largestNum = num

    num += 1

print(largestNum)