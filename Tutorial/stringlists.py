# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

palindrome = input("Enter your word: ")
new_word = palindrome[::-1]

if palindrome == new_word:
    print(f"This word '{palindrome.upper()}' is a palindrome")

else:
    print(f"This word '{palindrome.upper()}' is not a palindrome")
