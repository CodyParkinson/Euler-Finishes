'''
01/04/2024

Q: Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any
calculator would confirm 2^11 = 2048 < 3^7 = 2187

However, confirming that 632385^518061 > 519432^525806 would be much more difficult as both numbers
contain over three million digits. 

In the file, which line has the greatest numerical value?

A: 709

'''

# You can estimate the number of digits in the result using log10. 
# Interestingly enough, there are multiple numbers in the file with the same number of digits in the answer
# There isn't very many, so I plugged them in unitl I found that it was 709 (which of course was the last one).

import math

with open('base_exp.txt', 'r') as file:
    lines = []
    for line in file:
        number_list = [int(num) for num in line.split(',')]
        lines.append(number_list)

big, lin, count = 0, 0, 0
for i in lines:
    if math.floor(i[1] * math.log10(i[0])) + 1 >= big:
        big = math.floor(i[1] * math.log10(i[0])) + 1
        lin = count

    count += 1

print(lin + 1)