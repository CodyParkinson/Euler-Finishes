'''
01/04/2024

Q: The first known prime found to exceed one million digits was discovered in 1999, and is a 
Mersenne prime of the form 2^6972593; it contains exactly 2098960 digits. Subsequently other Mersenne primes, of 
the form 2^p - 1 have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2357207 digits: 
28433 x 2^7830457 + 1.

Find the last ten digits of this prime number.

A: 8739992577

'''

# I solved this question quite a long time ago - like back in my freshman year! 
# I didn't really go back over the code, it works, so all good!

x = 28433*(2**7830457)+1

lst = []
rng, rng2, up = 1, 10, 1

check = 0
while check < 10:
	check += 1

	for i in range(rng,rng2, up):
		if (x - i)%rng2 == 0:
			lst.append(i)
			x = x - i

	rng, rng2, up = str(rng), str(rng2), str(up)
	rng = rng + '0'
	rng2 = rng2 + '0'
	up = up + '0'

	rng, rng2, up = int(rng), int(rng2), int(up)


lst = lst[::-1]

num = ''
for i in lst:
	i = str(i)
	num = num + i[0]

print(num)