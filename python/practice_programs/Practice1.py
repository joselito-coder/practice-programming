# This problem is taken from  https://www.codeabbey.com

#     Test data contains "input data" or "test-case" - two numbers which we want to sum.
#     Your answer - is where you put your result after processing test data.
#     Your solution - is where you save your program code. It would not be checked (at least automatically), but it will help you reuse your code in the next tasks. You can revisit the task any time to see your submitted solution.

# Example:
# input data:
# 3 5
# answer:
# 8


# Take user input
print("input data:")
a,b = input().split()

# Typecast values
a,b = int(a),int(b)

print("\nanswer:")
print(a+b)