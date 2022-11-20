'''
11/17/2022

Q: Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO O
OOO OO
OOO O O
OO OO O
OO O O O
O O O O O
Find the least value of n for which p(n) is divisible by one million.

A: 55374

'''

'''
What a rough problem, I have no idea how it all works, all I know is that it does. If you feel like running this very naive, brute force code,
please be willing to wait 30 minutes. 

I originally wrote the code below without using the wiki or any other source. I figured I could just reuse the code from the previous problems.
The problem was it was just taking way too much time to solve. So, I started looking into the wiki on partitions 
https://en.wikipedia.org/wiki/Partition_%28number_theory%29#Recurrence_formula
I am still not very familiar with all the math nomenclature, so I wasn't quite sure how to implament the wiki material. 
In the process though, I learned that looking through the combList below, I did not have to resolve for problems. Becuase the comblist builds on previous
solutions, the list contains the pattern here https://oeis.org/A000041 
I just looped through this list and got the answer I has looking for. I used 100_000 as an arbitrary number. I knew that it look a few minutes to solve for
10,000 so I started the code, walked away, and crossed by fingers when I came back that it would have an answer. Lo and behold, one came out.

This problem stretches this code to its limits. If you were to look for any bigger of a number, it would just take too long to solve. I recommend this site
https://blog.dreamshire.com/project/source/pe78.py for code that is much more efficient. But hey... a solve is a solve!

'''

# This is the code from problem 77, with some modifications.
def findSums(num):
    total = num
    coins = list(range(1,num))
    combList = [1]
    combList += [0]*total
    for i in coins:
        for b in range(i, total+1):
            combList[b] += combList[b-i]
    return combList

# Loop through the combList and if the num%1mil == 0. Print and break
x = findSums(100_000)
for i in x:
    if i % 1_000_000 == 0:
        print(x.index(i))
        break

