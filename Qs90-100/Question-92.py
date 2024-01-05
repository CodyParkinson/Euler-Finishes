'''
12/18/2023

Q: A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
For example,

44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

A: 8581146

'''

# Another brute, so be patient!

ccnt = 0
for i in range(1, 10000000):

	x = i
	while True:
		y = str(x)
		lst = list(y)
		num = 0

		for b in lst:
			d = int(b)**2
			num += d

		x = int(num)
		if x == 89:
			ccnt += 1
			break
		elif x == 1:
			break

print(ccnt) 
