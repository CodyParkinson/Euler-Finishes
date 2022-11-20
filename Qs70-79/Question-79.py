'''
11/18/2022

Q: A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

A: 73162890

'''

'''
This was a pen and paper solve, with just a little programming sprinkled in. I left my prints in to show my though process below.
Basically, I printed the numbers in an ordered set. From this set I created a dictionary of the index of each of the values. Because
we know they must be in order, the first number should only be at index 0 and the final number will be at index 2.
This gave us the first and last numbers. Next, I just went to each number one at a time and figured where they had to be based on their
index. For example, the second number could only be at index 0 or 1. If it is at 1, the first number had to be a 7. 
A final note, if you look at the passcodes, you can see that each number only comes up once, so I figured this had to be so in the 
answer.

'''

# Open file
with open('p079_keylog.txt', 'r') as keylog:
    numbers = keylog.read()

# Take the file and add each number to a list
keylog = []
num = ''
for i in numbers:
    if i in '1234567890':
        num = num + i
    else:
        keylog.append(num)
        num = ''

# Print the sorted list
print(sorted(set(keylog)), "\n\n")

# Create a dictionary of indexes
dictOfPos = {}
for i in set(keylog):
    for b in i:
        if b not in dictOfPos:
            dictOfPos[b] = [i.index(b)]
        else:
            dictOfPos[b].append(i.index(b))

# Print the indexes for easy reading
for i in range(10):
    if str(i) in dictOfPos:
        print(i, dictOfPos[str(i)])
print('\n\n')
print(73162890)