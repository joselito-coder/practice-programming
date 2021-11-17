# Maximum of array
# Problem 6
# This problem can be found at this link: https://www.codeabbey.com/index/task_view/maximum-of-array

"""
Author: Joselito
Date: 17-11-2021
Purpose: to find the minimum and the maximum number in an array using linear search
"""

def print_min_max(numbers):
    """
        This function prints the max number and min number found inside a list of numbers 
    """
    numbers = [int(i) for i in numbers ]

    min_number = 999999999999999999999999
    max_number = 0

    # find the max number 
    for number in numbers:
        if number > max_number:
            max_number = number

    # Find the min number
    for number in numbers:
        if number < min_number:
            min_number = number
        
    print(max_number,min_number)


if __name__ == '__main__':
    numbers = input().split()

    print_min_max(numbers)