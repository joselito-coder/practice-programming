""" 
Author: Joselito
Date: 10-11-2021
Purpose: Sum pairs of numbers and print them
"""

                    # Sums in Loop
# Problem #3
# Now we are given several pairs of values and we want to calculate sum for each pair.
# Input data will contain the total count of pairs to process in the first line.
# The following lines will contain pairs themselves - one pair at each line.
# Answer should contain the results separated by spaces.

# Take the number of pairs
num_of_pairs = int(input())

# init Array for storing all the pairs
pairs_array = []

for i in range(num_of_pairs):
    # split the num into a pair
    pair = input().split()
    # use list comprehension to create the pair as a list of array
    pair = [int(p) for p in pair ]
    pairs_array.append(pair)

for pairs in pairs_array:
    print(sum(pairs),end=" ")

