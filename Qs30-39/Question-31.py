'''
09/18/2022

Q: In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can £2 be made using any number of coins?

A: 73682

'''

'''
I will always make a note if I had to lookup help to solve a problem. This is the first one I have done this on. I felt after 2 solid days of not getting the
correct values, it was time to try and seek out help. I took my inspiration from https://blog.dreamshire.com/project-euler-31-solution/ This is honestly a really
slick solution, and I tried to rework it below and add comments. It seems like no one on the blog knows how the question works, so hopefully these comments can help.
I really hate to look up help, but I am looking to advance my skills not just get stuck on a simple combinations problem for weeks. Kudos to Mike Molony

I am also attaching this website that does a really great job explaining how the array works https://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/
The basic trick really is - once a value is issued, how many combinations it takes using the specified coins is saved. Moving to the next value - take the current coin and subtract it from value to get value - coin. Add the amount of combinations it takes to get to that value to the original value's previous coin and there is the answer. Please see the website above for the sheets that go over this in not so confusing a way. 
It really is super simple, and with this program can go up to some pretty high values in under a second. I recommend building an array by hand to see it work itself out. Once written, it is much more clear to see.
'''

# List the max amount of money and coins
total = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

# Create a list of 'combinations' each position represents the 200 maximum ways of combination, don't go over 200 as 1 is the lowest amount
combList = [1]
combList += [0]*total


# Loop through the coins
for i in coins:
    # The trick is to find all of the possible locations that the coins could be. Don't need to try every combination, just know how many times a coin combination could possibly appear.
    for b in range(i, total+1):
        combList[b] += combList[b-i]


# The final value of the list is the correct amount of combinations
print(combList[-1])