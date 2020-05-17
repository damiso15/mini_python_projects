# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a
# mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random,
# generating a new password every time the user asks for a new password. Include your run-time code in a main method.
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random
import string
import string_utils


user_option = input("""
Choose Either: 1, 2 or 3.
1 ===> Weak
2 ===> fairly strong
3 ===> very strong
Please Pick an Option:
""")
strength = {'weak': '1', 'fairly strong': '2', 'very strong': '3'}
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
symbols = string.punctuation
password = ''


def gen_password():
    lower_case_pass = ''.join(random.choice(lower_case) for i in range(length))
    upper_case_pass = ''.join(random.choice(upper_case) for i in range(length))
    numbers = ''.join(map(str, random.sample(range(1, 9), length)))
    characters = ''.join(random.choice(symbols) for i in range(length))
    auto_password = lower_case_pass + upper_case_pass + numbers + characters
    password = string_utils.shuffle(auto_password)
    print(f"\nYour auto generated password is: {password}")

    return password


while user_option != '1' or '2' or '3':
    print("\nWRONG OPTION")
    user_option = input("""
Choose Either: 1, 2 or 3.
1 ===> Weak
2 ===> fairly strong
3 ===> very strong
Please Pick an Option:
""")

else:

    if user_option == '1':
        password = strength.get('weak')
        length = 2
        gen_password()

    elif user_option == '2':
        password = strength.get('fairly strong')
        length = 5
        gen_password()

    elif user_option == '3':
        password = strength.get('very strong')
        length = 7
        gen_password()


