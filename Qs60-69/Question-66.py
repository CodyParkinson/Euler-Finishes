'''
10/26/2022

Q: Consider quadratic Diophantine equations of the form:

x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13x180^2 = 1.
It can be assumed that there are no solutions in positive integers when D is square.
By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 - 2x2^2 = 1
2^2 - 3x1^2 = 1
9^2 - 5x4^2 = 1
5^2 - 6x2^2 = 1
8^2 - 7x3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

A: 661

'''

'''
I figured this problem would be tricky, so here are my notes:
1. I first figured out this is a classic Pell Equation - https://artofproblemsolving.com/wiki/index.php/Pell_equation
2. My original nieve method only worked up to a few hundred, as it was trying to brute force solve for x in the equation x = (D(y**2) + 1) ** 0.5 - it worked great until numbers became way too large to just loop through - it was trying to find if x was a whole value. I found the code - https://stackoverflow.com/questions/2489435/check-if-a-number-is-a-perfect-square and I really liked this implementation of finding whole square values without floats. I ended up keeping this code as to skip squares later on in the problem.
3. I read a bunch of articles and papers on the Pell Equation, Brahmagupta's Identity, and the Chakravala Method. I am really trying to learn math nomenclature and build my knowledge on how to approach these problems. I found this article - https://sydney4.medium.com/pells-equation-and-the-chakravala-method-d4587f141b40 and all I can say is Sydney Birbrower, this is an amazing article. I ended up copying her code (the functions new_triple and chakravala) and tweaking it to meet my needs. Mostly there were errors when abk came out to 0 and overflow errors from too large of values. After fixing these, I looped the values and got the answer. 

I am so greatful for those who have built this great repositories online with information - they really are so helpful when trying to solve these problems that I just have never really encountered anything like before.

'''

def isSquare(num):
    xCheck = num//2
    check = set([num])
    while xCheck * xCheck != num:
        xCheck = (xCheck + (num // xCheck)) // 2
        if xCheck in check:
            return False
            break
        check.add(xCheck)
    else:
        return True

def new_triple(abk, m):
    a_1 = int((m * abk[0] + n * abk[1]) // abs(abk[2]))
    b_1 = int((abk[0] + m * abk[1]) // abs(abk[2]))
    k_1 = int((m**2 - n) // abk[2])
    return (a_1, b_1, k_1)

def chakravala(abk, n):
    possible_ms = []
    first_m = 0
    
    for i in range(abs(abk[2])):
        if (abk[0] + abk[1] * i) % abk[2] == 0:
            first_m = i
            
    possible_ms = [first_m + abs(i * abk[2]) for i in range(10)]
    
    least_m2 = possible_ms[0]
    for m in possible_ms:
        if abs(m**2 - n) < abs(least_m2**2 - n):
            least_m2 = m
    
    abk = new_triple(abk, least_m2)
    
    if abk[2] == 1 or abk[2] == 0:
        return abk
    else:
        return chakravala(abk, n)
      
final = [0, 0]
for i in range(2, 1001):
    if isSquare(i) == False:
        n = i  # any number not a square
        c = 5  # arbitrary starting number
        abk = (c, 1, c**2 - n)

        abk = (c, 1, c**2 - n)
        x = chakravala(abk, n)
        if x[0] > final[0]:
            final[0] = x[0]
            final[1] = i
print(final[1])