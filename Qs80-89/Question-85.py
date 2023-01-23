'''
01/19/2023

Q: By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles.
Although there exists no rectangular grid that contains exactly two million rectangles, 
find the area of the grid with the nearest solution.

A: 2772

'''

# https://math.stackexchange.com/questions/1656686/how-many-rectangles-can-be-observed-in-the-grid - good method

# Basically just follow the formula from the above source - loop two sides and break if area > 2mil. 
# Save and report the highest side values to find area
num, lst = 0, [0,0]
for i in range(int(2_000)):
    for b in range(int(2_000)):
        x = (((i+1)*i)/2) * (((b+1)*b)/2)
        if x < 2_000_000 and x > num:
            num, lst[0], lst[1] = x, i, b
        elif x > 2_000_000:
            break
print((lst[0])*(lst[1]))
