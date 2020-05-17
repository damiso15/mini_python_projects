# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#
#   My name is Michele
# Then I would see the string:
#
#   Michele is name My
# shown back to me.


def reverse_word(user):

    # user = input("Enter a sentence\n")
    words = user.split(" ")
    reverse = words[::-1]
    # output = ""
    # for element in reverse:
    #     output += element + " "
    # print(output)

    output = " "
    return f"\n{output.join(reverse)}"

    # output = " ".join(map(str, reverse))
    # print(output)


user = input("Enter a sentence\n")
result = reverse_word(user)
print(result)