'''
10/17/2022

Q: The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
How many n-digit positive integers exist which are also an nth power?

A: 49

'''

# Loop and check that the length == the power
total = 0
for i in range(1, 1000):
    for b in range(1,100):
        if len(str(i**b)) == b:
            total += 1
print(total)