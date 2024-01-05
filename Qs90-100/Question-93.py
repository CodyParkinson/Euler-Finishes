'''
12/18/2023

Q: By using each of the digits from the set, {1,2,3,4}, exactly once, and making use of the four arithmetic operations
(+,-,x,/)) and brackets/parentheses, it is possible to form different positive integer targets.

Note that concatenations of the digits are not allowed.

Using the set, {1,2,3,4}, it is possible to obtain thirty-one different target numbers of which 36
is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a<b<c<d, for which the longest set of consecutive positive integers,
1 to n can be obtained, giving your answer as a string: abcd.

A: 1258

'''

# Crazy using GPT to help write, maybe AI will take over the world... For now, it sure is useful!

from itertools import permutations, product, combinations

def generate_all_expressions(digits):
    
    # Create a list of all the different ways the four digits could be combined with operators and parenthesis

    op_symbols = ['+', '-', '*', '/']
    expressions = set()

    for numbers in permutations(digits):
        for ops_comb in product(op_symbols, repeat=3):

            # Basically all this is is: Num Oper Num Oper Num Oper Num, parenthesis are built in as well
            # Thank you GPT for this (Saved a bunch of time after failing to get it just right)
            exprs = [
                f"({numbers[0]} {ops_comb[0]} {numbers[1]}) {ops_comb[1]} ({numbers[2]} {ops_comb[2]} {numbers[3]})",
                f"(({numbers[0]} {ops_comb[0]} {numbers[1]}) {ops_comb[1]} {numbers[2]}) {ops_comb[2]} {numbers[3]}",
                f"{numbers[0]} {ops_comb[0]} (({numbers[1]} {ops_comb[1]} {numbers[2]}) {ops_comb[2]} {numbers[3]})",
                f"{numbers[0]} {ops_comb[0]} ({numbers[1]} {ops_comb[1]} ({numbers[2]} {ops_comb[2]} {numbers[3]}))"
            ]

            expressions.update(exprs)

    return expressions


def longest_consecutive_sequence(expressions):
    
    # Need to find the longest chain of numbers
    nums = []
    for i in expressions:
        
        # Using the eval parses the expression together. Could divide by zero, so must use a try/except to check
        try:
            result = eval(i)
            if result == int(result) and result > 0:
                nums.append(int(result))
        except:
            pass
    
    # Check for numbers in order
    for i in range(1, 10000):
        if i not in nums:
            return i 


def find_best_digit_set():
    
    # Take the two functions above and find the best chain
    longest = 0
    best = None

    # Pretty slick to use combinnations and parse into the expressions, works too good!
    for digits in combinations(range(1, 10), 4):
        expressions = generate_all_expressions(digits)
        num = longest_consecutive_sequence(expressions)

        if num > longest:
            longest = num
            best = digits

    print(str(best[0]) + str(best[1]) + str(best[2]) + str(best[3]))

# Find the best digit set
find_best_digit_set()