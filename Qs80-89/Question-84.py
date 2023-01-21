'''
01/19/2022

Q: In the game, Monopoly, the standard board is set up in the following way: (See PE site)

A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they 
advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 
2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, 
if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top
of the respective pile and, after following the instructions, it is returned to the bottom of the pile. 
There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; 
any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
1. Advance to GO
2. Go to JAIL
Chance (10/16 cards):
1. Advance to GO
2. Go to JAIL
3. Go to C1
4. Go to E3
5. Go to H2
6. Go to R1
7. Go to next R (railway company)
8. Go to next R
9. Go to next U (utility company)
10. Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at 
that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing 
on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final 
square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and 
being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their 
next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that 
correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, 
and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.

A: 101524

'''

# Just create a model of the board and see what squares pop up using a random number generator from 1-4 for two dice. 
# Very easy problem, just time consuming

# Use random number generator
import random

# List of Squares with the 3rd value be the amount of lands
listOfSquares = [
    [0, "GO", 0],
    [1, "A1", 0],
    [2, "CC1", 0],
    [3, "A2", 0],
    [4, "T1", 0],
    [5, "R1", 0],
    [6, "B1", 0],
    [7, "CH1", 0],
    [8, "B2", 0],
    [9, "B3", 0],
    [10, "JAIL", 0],
    [11, "C1", 0],
    [12, "U1", 0],
    [13, "C2", 0],
    [14, "C3", 0],
    [15, "R2", 0],
    [16, "D1", 0],
    [17, "CC2", 0],
    [18, "D2", 0],
    [19, "D3", 0],
    [20, "FP", 0],
    [21, "E1", 0],
    [22, "CH2", 0],
    [23, "E2", 0],
    [24, "E3", 0],
    [25, "R3", 0],
    [26, "F1", 0],
    [27, "F2", 0],
    [28, "U2", 0],
    [29, "F3", 0],
    [30, "G2J", 0],
    [31, "G1", 0],
    [32, "G2", 0],
    [33, "CC3", 0],
    [34, "G3", 0],
    [35, "R4", 0],
    [36, "CH3", 0],
    [37, "H1", 0],
    [38, "T2", 0],
    [39, "H2", 0],
]

# List of Community Chest - NA is just place holder for other cards
listOfCC = [
    "GO",
    "Jail",
    "NA",
    "NA",
    "NA",
    "NA",
    "NA",
    "NA",
    "NA",
    "NA",
    "NA",
    "NA",
    "NA",
    "NA",
    "NA",
    "NA",
]

# List of Chance Cards - NA is just place holder for other cards
listOfCH = [
    "GO",
    "JAIL",
    "C1",
    "E3",
    "H2",
    "R1",
    "NextR",
    "NextR",
    "NextU",
    "Back3",
    "NA",
    "NA",
    "NA",
    "NA",
    "NA",
    "NA",
]

# Keep track of player position, amount of snake eyes, and what card in CC and CH player is on.
playersPos = 0
snakeEyes = []
CCup, CHup = 0, 0

# Only takes 100_000 dice rolls to get number every time!
for i in range(100_000):
    playersPosList = [random.randint(1,4) + random.randint(1,4)]
    playersPos += sum(playersPosList)

    # Went past Go - reset number 
    if playersPos > 39:
        playersPos -= 40

    # Snake Eyes
    if snakeEyes == []:
        snakeEyes.append(playersPosList)
    else:
        if len(snakeEyes) == 1:
            if playersPosList in snakeEyes:
                snakeEyes.append(playersPosList)
            else:
                snakeEyes = []
        elif len(snakeEyes) == 2:
            if playersPosList in snakeEyes:
                snakeEyes = []
                playersPos = 10
            else:
                snakeEyes = []

    # Go to Jail
    if playersPos == 30:
        playersPos = 10

    # Chance Space
    if playersPos in [7, 22, 36]:
        if CHup == 0:
            playersPos = 0
        elif CHup == 1:
            playersPos = 10
        elif CHup == 2:
            playersPos = 11
        elif CHup == 3:
            playersPos = 24
        elif CHup == 4:
            playersPos == 39
        elif CHup == 5:
            playersPos == 5
        elif CHup == 6 or CHup == 7:
            if playersPos == 7:
                playersPos = 15
            elif playersPos == 22:
                playersPos = 25
            elif playersPos == 36:
                playersPos = 5
        elif CHup == 8:
            if playersPos == 7:
                playersPos = 12
            elif playersPos == 22:
                playersPos = 28
            elif playersPos == 36:
                playersPos = 12
        elif CHup == 9:
            playersPos -= 3
        else:
            pass
        CHup += 1
        if CHup == 16:
            CHup = 0

    # Community Chest Space
    if playersPos in [2, 17, 33]:
        if CCup == 0:
            playersPos = 0
        elif CCup == 1:
            playersPos == 10
        else:
            pass
        CCup +=1
        if CCup == 16:
            CCup = 0

    # Add player position to list of landed square
    for i in listOfSquares:
        if playersPos == i[0]:
            listOfSquares[playersPos][2] += 1

# Sort list by top three lands, and print the concatenated string
sortedMax = sorted(listOfSquares, key=lambda x: x[2])
print(str(sortedMax[-1][0]) + str(sortedMax[-2][0]) + str(sortedMax[-3][0]))