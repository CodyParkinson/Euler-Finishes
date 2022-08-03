'''
08/03/2022

Q: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

A: 233168

'''

# Find the multiples in range 1000
multiples3 = []
multiples5 = []

for i in range(1000):
    if i%3 == 0:
        multiples3.append(i)
    if i%5 == 0:
        multiples5.append(i)

# Add lists together
merged = multiples3 + multiples5

# Create set to exlclude duplicates
final_set = set(merged)

# Find Sum
final_sum = 0
for i in final_set:
    final_sum += i

print(final_sum)