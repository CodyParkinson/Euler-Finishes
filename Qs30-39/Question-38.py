'''
9/22/2022

Q: Take the number 192 and multiply it by each of 1, 2, and 3:
192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

A: 932718654

'''

# Create lists of numbers and break once the length is greater than 9 - save the concat in a list if it has the numbers 1-9 and print the max of the list. 
concats = []
for i in range(1, 1_000_000):
    total = ''
    for b in range(1, 1_000_000):
        total += str(i*b)
        if len(total) >= 9:
            break
    if '0' not in total and len(total) == 9:
        for i in "123456789":
            if i not in total:
                break
        else:
            concats.append(int(total))

print(max(concats))




