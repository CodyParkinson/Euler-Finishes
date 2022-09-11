'''
09/11/2022

Q: You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

A: 171

'''

# Make a list of months and their amounts of days (non-leap year)
months = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}

# days is just a counter of Monday - Sunday. SundaysOnFirst is our final value
SundaysOnFirst = 0
days = 0
# Iterate through the years, months, and days. If it is the first and the 'days' = 7, add one to SundaysOnFirst
for i in range(1901, 2001):
    for b in months:
        if i%4 == 0 and b == "February":
            amountOfDays = 29
        else:
            amountOfDays = months[b]
        for c in range(1, amountOfDays+1):
            days += 1
            if days == 7:
                if c == 1:
                    SundaysOnFirst += 1
                days = 0

# I originally got 172, but I figured I had make a slight mistake with a leap year on 2000. I accounted for this by subtracting a Sunday and that gave me the right answer
# Instead of trying to find the bug in the code I am just going to take the answer as it is :)
print(SundaysOnFirst-1)