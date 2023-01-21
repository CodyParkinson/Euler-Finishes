'''
11/21/2022

Q: It is well known that if the square root of a natural number is not an integer, then it is irrational. 
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits 
for all the irrational square roots.

A: 40886

'''

# Remember to not work with Fractions! 
# The trick is to change the 'i' of the loop by a factor 100 as you move down
# Basically you are just moving the decimal place

total = 0
for i in range(2, 100):
    # Check if number is irrational or not
    if i**0.5 % 1 != 0:
        # Create a list of numbers
        listOfNums = []
        while len(listOfNums) != 100:
            # Add numbers 0-9 to end of list
            for b in range(10):
                newNum = ''.join(listOfNums) + str(b)
                # If the new square is larger, break and subtract one
                if int(newNum)**2 > i:
                    listOfNums.append(str(b-1))
                    i*=100
                    break
                elif b == 9:
                    listOfNums.append(str(b))
                    i*=100
                    break
        # Add the total of the list to the sum. 
        total += sum(map(int, listOfNums))
print(total)
