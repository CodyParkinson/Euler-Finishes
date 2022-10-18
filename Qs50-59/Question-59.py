'''
10/12/2022

Q: Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

A: 129448

'''

'''
I had to do a lot of research to figure out how to even begin this problem - super fun and easy once you figure out what XOR cryptographry is. At first I thought I was going to have to figure out how to convert it to binary and do the checking myself - luckily python is smart enough to do this on its own - provided you give it the ascii numbers 
'''

# Important imports
from string import ascii_lowercase
from itertools import permutations

# Open the text document and extract the cipher
with open('p059_cipher.txt') as cipherTXT:
   cipher = cipherTXT.read()

cipher = cipher.split(',')
letters = list(permutations(ascii_lowercase, 3))

for i in letters:
    i = list(i) * int(len(cipher)/3)
    message = ''
    asciiSum = 0
    for b,c in zip(cipher, i):
        message += chr(int(b)^ord(c))
        asciiSum += int(b)^ord(c)
    # Very common words - did have to do a little guessing at first to find enough words that it would be a real match
    if 'the' in message and 'and' in message and 'if' in message:
        print(asciiSum)
        break