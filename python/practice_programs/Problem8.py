# Problem 8
# This problem can be found at this link: https://pynative.com/python-basic-exercise-for-beginners/

# Given two integer numbers return their product only if the product is less than 1000, else return their sum.

def mult_res(number1,number2):
    product = number1 * number2

    if product < 1000:
        return product
    else:
        return number1 + number2

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

print(mult_res(num1,num2))
