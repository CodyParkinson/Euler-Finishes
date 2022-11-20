'''
11/16/2022

Q: It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

A: 190569291

'''

'''
This question is exactly question 31, Coin sums. See my answer to 31 for code explanation
I only altered the total and coins list

'''

total = 100
coins = []
for i in range(1, 100):
    coins.append(i)

combList = [1]
combList += [0]*total

for i in coins:
    for b in range(i, total+1):
        combList[b] += combList[b-i]

print(combList[-1])