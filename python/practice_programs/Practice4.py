# Minimum of Two
# Problem #4
# Most programs should be able to make some choices and decisions. And we are going to practice conditional programming now.
# This is usually done by a kind of if ... else statements which may look like:
# IF some_condition THEN
#     do_something
# ELSE
#     do_other_thing
# ENDIF
# Depending on your programming language syntax could be different and else part is almost always optional. You can read more in wikipedia article on Conditional statements.
# Of two numbers, please, select one with minimum value. Here are several pairs of numbers for thorough testing.
# Input data will contain number of test-cases in the first line.
# Following lines will contain a pair of numbers to compare each.
# For Answer please enter the same amount of minimums separated by space, for example:

# data:
# 3
# 5 3
# 2 8
# 100 15
# answer:
# 3 2 15

""" 
Author: Joselito
Date: 14-11-2021
Purpose: Find the mininum of two numbers in a list and add that num to a seperate list
"""

# Function to give the min of the  numbers in a list
def minOfTwo(numbers):
    min_num = 100000000000000

    for number in numbers:
        number = int(number)
        if number < min_num:
            min_num = number
    
    return int(min_num)


# Take user input
num_of_pairs = int(input())
pairs_list = []
for i in range(num_of_pairs):
    pair = input().split()
    pairs_list.append(pair)

# Create an array with min of the two numbers
min_of_two_list = [str(minOfTwo(number)) for number in pairs_list]


print(' '.join(min_of_two_list))
