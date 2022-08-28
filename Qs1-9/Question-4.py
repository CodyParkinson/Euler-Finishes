'''
08/03/2022

Q: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

A: 906609

'''

# Create a list of palindromes with 3-digit numbers. We know that 999*999 = 998001. So, no number can be larger than this.
isPalindrome = []

# Since we know the largest number, only need to check three digit positions. 
for i in reversed(range(100, 1000)):
    for b in reversed(range(100, 1000)):
        palindrome = i * b
        palindrome = str(palindrome)
        if palindrome[0] == palindrome[-1]:
           if palindrome[1] == palindrome[-2]:
                if palindrome[2] == palindrome[-3]:
                    if len(palindrome)%2 == 0:
                        isPalindrome.append(palindrome)

# Print the largest number from the list
print(max(isPalindrome))


