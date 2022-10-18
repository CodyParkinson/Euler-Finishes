'''
10/12/2022

Q: Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

A: 26241

'''

# prime number function
def isPrimeFunc(num):
    if num == 1 or num%2 == 0 or num == 2 or num == 4 or num == 6 or num == 8:
        return False
    elif num == 3 or num == 5 or num == 7:
        return True
    else:
        for i in range(3, int(num**0.5)+ 1, 2):
            if num%i == 0:
                return False
                break
        else:
            return True

# Used kinda the same code from Question 28 about spiral sums of the diags - instead of summing, used the function to check if prime
isPrime, isNotPrime = 0, 0
move, moveUp = 3, 2
check = 0
primesprime = [[],[]]
while True:
    if isPrimeFunc(move) == True:
        isPrime += 1
    else:
        isNotPrime += 1
    move+=moveUp
    check+=1
    if check == 3:
        moveUp += 2
        check = -1
    if isPrime != 0 and isNotPrime != 0:
        if isPrime/(isNotPrime+isPrime) < (0.10) and (isNotPrime + isPrime)&4 == 0:
            # I don't quite know why I need to subtract one, but the answer came out as a positive and the side lengths have to be negative, so I just subtracted one and it was right
            print(moveUp-1)
            break