# Minimum of Three
# Problem 5
# The link to this problem can be found: https://www.codeabbey.com/index/task_view/min-of-three

"""
Author: Joseito
Date: 16-11-2021
Purpose: Find the minimum among each of the given triplets.
"""
def min_of_three(num_list):
    # typecast all values into integers
    number_list = [int(numbers) for numbers in num_list ]

    # Check for the smallest number
    min_num = 100000000000000

    for number in number_list:
        number = int(number)
        if number < min_num:
            min_num = number

    return min_num
        

if __name__ == "__main__":
    # take and store user input
    num_of_triplets = int(input())
    triplets = [input().split() for i in range(num_of_triplets)]


    for triplet in triplets:
        print(min_of_three(triplet),end=" ")
