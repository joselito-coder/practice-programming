# This problem is taken from  https://www.codeabbey.com

# Input data has the following format:
#     first line contains N - amount of values to sum;
#     second line contains N values themselves.
# Answer should contain a single value - the sum of N values.
# Example:
# input data:
# 8
# 10 20 30 40 5 6 7 8
# answer:
# 126

# Take user input
num_of_args = int(input())
args = input().split()

# Create an array of num of args
args = args[:num_of_args]

# Init result
result = 0

# Loop through the array of numbers
for i in args:
    result += int(i)

print(result)