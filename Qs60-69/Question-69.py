'''
10/28/2022

Q: Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively 
prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

A: 510510

'''

'''
This problem gave me way more problems than it should have. First, I tried using this ternary tree https://en.wikipedia.org/wiki/Coprime_integers - 
this gave me memroy and overflow errors. After trying this method for a few hours, I realized I was just generating way too much data. 
It works really well on the low end, but at the larger numbers, it begins to suffer. 
This led me to do more research where I got a hint from https://www.xarg.org/puzzle/project-euler/problem-69/ and I solved it instantly. 
I like this guys site and he is the same one that helped me on the coin summations problem. After reading his explanation - 
well i was more confused, but I pondered on it and the logic is sound:

By multiplying the primes together - we decrease the denominator, this is good because it is (value/relative primes). 
We want the highest value with the lowest denominator. By taking out all of the primes you also eliminate all the numbers that make up primes - 
example by multiplying 2*3*5 to get 30, you have taken out 2,3,5 but all of their multiples so for 2 it would be 2,4,6,... 28; 3,6,9... 27; 5,10,15...25 
- their lowest common denominators. Once the value is maximal under 1_000_000 - you have your answer.

'''

# Reuse, Reduce, Recycle
start = 0
upTo = 500
primeListTF = [True for i in range(start, upTo)]
primeUp = 2
while primeUp*primeUp < upTo:
    if primeListTF[primeUp] == True:
        for i in range(primeUp * primeUp, upTo, primeUp):
            primeListTF[i] = False
    primeUp += 1

total = 1
moveUp = 0
for i in primeListTF:
    if i == True and moveUp != 0:
        total *= moveUp
    if total > 1_000_000:
        total = total/ moveUp
        break
    moveUp += 1

print(int(total))
    


