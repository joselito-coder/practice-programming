# Rounding
# Problem 6
# This problem can be found at this link: https://www.codeabbey.com/index/task_view/rounding

"""
Author: Joselito
Date: 19-11-2021
Purpose: return the  result of dividing two numbers, rounded to the nearest integer.
"""

def print_round_div(num_array):
    result = []

    for i in num_array:
        result.append(str(floor(int(i[0]) / int(i[1]))))
    
    print(" ".join(result))


if __name__ == '__main__':
    num_of_tries = int(input())

    total_num_arr = []

    for i in range(num_of_tries):
        pair = input().split()
        total_num_arr.append(pair)

    print_round_div(total_num_arr)


