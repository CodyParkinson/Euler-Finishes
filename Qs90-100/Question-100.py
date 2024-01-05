'''
01/04/2024

Q: If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs,
and two discs were taken at random, it can be seen that the probability of taking two blue discs,
P(BB) = (15/21)x(14/20) = 1/2

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, 
is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 discs in total, determine the number of blue discs that 
the box would contain.

A: 756872327473

'''

# Definitely not a 30%! A great way to end the first 100!

x, y = 1, 1

while True:
    # Generate the next solution
    x, y = 3 * x + 4 * y, 2 * x + 3 * y

    disks = (x + 1) // 2
    blue = (y + 1) // 2

    if disks > 10**12:
        print(blue)
        break