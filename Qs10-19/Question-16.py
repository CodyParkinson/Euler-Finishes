'''
08/29/2022

Q: 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2**1000?

A: 1366

'''

# Solve the equation - python cannot iterate through integers so just convert to string then convert back
num = 2**1000
sumNum = 0
for i in str(num):
    sumNum += int(i)
print(sumNum)