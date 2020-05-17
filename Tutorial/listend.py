# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

import random


def list_ends(num):

    # num = int(input("Enter your number. Number must be greater than 20: "))

    gen_list = random.sample(range(1, num), 10)
    print(f"\nYour auto generated list is: {gen_list}")

    new_list = [gen_list[0], gen_list[-1]]
    return f"\nThe first and last elements are: {new_list}"


number = int(input("Enter your number. Number must be greater than 20: "))
result = list_ends(number)
print(result)


# num = int(input("Please enter the number of Fibonacci sequence to generate: "))
# gen_list = random.sample(range(1, 1000), num)
# while num > 10:
#     print("\nNumber most not be greater than 10")
#     num = int(input("\nPlease enter the number of Fibonacci sequence to generate: "))
#
# else:
#     print(f"\n{gen_list}")