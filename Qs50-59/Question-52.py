'''
10/10/2022

Q: It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

A: 142857

'''

# Simply go up numbers by 1, turn the number into list and sort the list, if the multiple does not equal the list, move up, if 2-6 all equal the original list, break and print value
moveUp = 2
while True:
    check = sorted(list(str(moveUp)))
    for i in range(2,7):
        if sorted(list(str(moveUp * i))) != check:
            break
    else:
        print(moveUp)
        break
    moveUp += 1
