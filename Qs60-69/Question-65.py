'''
10/24/2022

Q: Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e. (See full question on PE site)

A: 272

'''

# An easy question once you figure out that every third number in the series is: continued fraction number * [-1] + [-2] 
#(Using the numList and knowing that the continued fraction is +2 each time up)
# I did have to end up looking up a hint to help figure out the third values, the other values are just the previous added together.
numList = [2,3,8,11]
upMe, moveUp = 4, 4

while len(numList) != 100:
    moveUp += 1
    if moveUp % 3 == 0:
        numList.append(upMe * numList[-1] + numList[-2])
        upMe += 2
    else:
        numList.append(numList[-1] + numList[-2])

# Loop the last number and add it up
total = 0
for i in str(numList[-1]): total += int(i)
print(total)


