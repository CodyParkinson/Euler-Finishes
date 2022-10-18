'''
10/18/2022

Q: How many continued fractions for N <= 10,000 have an odd period? (See full question on PE site)

A: 1322

'''

'''
This problem gave a lot of fuss. After a few days of playing around with ideas - I had written some code that hard calculated each of the numbers in the period. The problem was that it worked with values that had a period of less than 15. This is due to float precision. After 15, the precision of the float was not correct, so it would not calculate the correct periods. I tried lots of different approaches, but I ultimately started to look for hints on moving forward - I first visited the wiki https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion which gives a decent explanation. After trying to decode the algorithm, I found this site https://www.ivl-projecteuler.com/overview-of-problems/20-difficulty/problem-64 which he also states that he does not like his answer as he doesn't understand it. I just followed along with his logic and fixed my code to reflect it.

In the end this code does work, and it is very fast, but I do not understand the logic of it. I have now spent about 4 hours just starting at the logic trying to figure out how it works, so I think I'll have to come back to it later to try and figure it out a bit more. I have commented what I could as to make it easier to read in the future. 

'''

# total is just the amount of periods that are odd
total = 0

# Loop through the range 2 to 9_999 (10_000 is a perfect square)
for i in range(2, 10_000):

    # This logic checks that the number is not a perfect square, if it is, skip it
    if (i**0.5).is_integer() == False:

        # Create a list of the found periods, I don't add the first value as it does not repeat.
        listOfPeriod = []

        # The periodNum is the integer value of the root
        periodNum = int(i**0.5)

        # Save the first periodNum for the later logic check - it will repeat once the final period number is twice the original periodNum
        firstOut = periodNum

        # This is where I start to get confused, I am not sure why you start with the numerator as 0 and the denominator as 1, but it works out
        numer = 0
        denom = 1

        # Loop until period is twice the original periodNum
        while True:

            # I believe if you do the math by hand, you'll see that you have to take the reciprical, so I think that's why the denom is on the top
            # But these next lines, I have not figured out how they fully function
            nextNum = int(denom * periodNum - numer)
            nextDen = int((i - nextNum**2) / denom)
            newPeriodNum = int((firstOut + nextNum) / nextDen)

            # Append the new periodNum and save the values to loop again
            listOfPeriod.append(newPeriodNum) 
            periodNum = newPeriodNum
            numer = nextNum
            denom = nextDen  

            # Logic to check that the loop needs to be broken
            if periodNum >= firstOut * 2:
                if len(listOfPeriod)%2 != 0:
                    total += 1
                break

# Print the final total        
print(total)
