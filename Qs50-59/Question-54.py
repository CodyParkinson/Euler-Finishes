'''
10/11/2022

Q: In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

A: 376

'''

'''
This comment is just to say that this is probably one of my best 'codes' yet. This just flowed, I finished this problem in about an hour and a half, and I could not be more thrilled. You basically write a poker playing script, there is really no tricks I could think of, so I just wrote it all as if I was creating an game. I may come back later and finish out some of the final logic. I wrote only the last two 'tie' rules, so if those were finished, you would have a fully functional game!
'''

# I just alwasy hate writing out the alphabet
from string import ascii_uppercase

# Open the text document and extract the hands
with open('poker.txt') as poker:
   pokerHandsText = poker.read()

# Sort the hands into lists of lists for easy iteration
pokerHands = []
pOne, bothHands, together = [], [], ''
for i in pokerHandsText:
    if i in ascii_uppercase or i in '23456789':
        together = str(together) + i
        if len(together) == 2:
            if len(pOne) < 5:
                pOne.append(together)
                together = ''
                if len(pOne) == 5:
                    bothHands.append(pOne)
                    pOne = []
            if len(bothHands) == 2:
                pokerHands.append(bothHands)
                bothHands = []

# Create a function that determines the score of the hand input
def score(hand):
    # This list will determine the highest values
    valScoreList = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    valScoreListInts = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    handValue, handType = [], []
    for i in hand:
        handValue.append(i[0])
        handType.append(i[1])

    # Score to return
    playerScore = 0

    while True:
        # Royal Flush
        if 'T' in handValue and 'J' in handValue and 'Q' in handValue and 'K' in handValue and 'A' in handValue: 
            for i in handType:
                if i != handType[0]:
                    break
            else:
                playerScore = 10
                break
    
        # Straight Flush
        if len(set(handType)) == 1:
            flushCheck = []
            for i in handValue:
                flushCheck.append(valScoreListInts[valScoreList.index(i)])
            SFup = 0
            for i in sorted(flushCheck):
                SFup += 1
                if SFup < 5:
                    if sorted(flushCheck)[SFup] != i+1:
                        break
            else:
                playerScore = 9
                break

        # Four of a Kind
        for i in handValue:
            if handValue.count(i) == 4:
                playerScore = 8
        else:
            if playerScore == 8:
                break

        # Full House
        for i in handValue:
            if handValue.count(i) == 3:
                for b in handValue:
                    if handValue.count(b) == 2:
                        playerScore = 7
                        break
                break
        if playerScore == 7:
            break


        # Flush
        for i in handType:
            if i != handType[0]:
                break
        else:
            playerScore = 6
            break


        # Straight
        straightCheck = []
        for i in handValue:
            straightCheck.append(valScoreListInts[valScoreList.index(i)])
        Sup = 0
        for i in sorted(straightCheck):
            Sup += 1
            if Sup < 5:
                if sorted(straightCheck)[Sup] != i+1:
                    break
        else:
            playerScore = 5
            break


        # Three of a Kind
        for i in handValue:
            if handValue.count(i) == 3:
                playerScore = 4
                break
        if playerScore == 4:
            break


        # Two Pairs
        for i in handValue:
            if len(set(handValue)) == 3:
                playerScore = 3
                break
        if playerScore == 3:
            break


        # One Pair
        for i in handValue:
            if len(set(handValue)) == 4:
                playerScore = 2
                break
        if playerScore == 2:
            break


        # High Card
        playerScore = 1
        break

    handValueReturn = []
    for i in handValue:
        handValueReturn.append(valScoreListInts[valScoreList.index(i)])
    return playerScore, handValueReturn, handType
        
# Input each of the player's hands and determine who has the higher score - if they tie, determine winner based on highest values
playerOne, playerTwo = 0, 0
for i in pokerHands:
    scoreOne, HV1, HT1 = score(i[0])
    scoreTwo, HV2, HT2 = score(i[1])
    if scoreOne > scoreTwo:
        playerOne += 1
    elif scoreOne < scoreTwo:
        playerTwo += 1
    else:
        if scoreOne == 1:
            for i,b in zip(sorted(HV1)[::-1], sorted(HV2)[::-1]):
                if i > b:
                    playerOne += 1
                    break
                elif i< b:
                    playerTwo += 1
                    break
        if scoreOne == 2:
            p12, p22 = 0, 0
            for i, b in zip(HV1, HV2):
                if HV1.count(i) == 2:
                    p12 = i 
                if HV2.count(b) == 2:
                    p22 = b 
            if p12 > p22:
                playerOne += 1
            elif p12 < p22:
                playerTwo += 1
            else:
                for i,b in zip(sorted(HV1)[::-1], sorted(HV2)[::-1]):
                    if i > b:
                        playerOne += 1
                        break
                    elif i< b:
                        playerTwo += 1
                        break
        # This comment is for future Cody - if you want to develop this into a whole game, you'll need to finish the ties - everything else should work
        # Problem 54 on EP only contains hands that have ties up to pairs
print(playerOne)