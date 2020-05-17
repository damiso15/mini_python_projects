# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

import random

ran_number = random.randint(1, 9)
count = 0
game = True

while game:

    user_number = int(input("\nGuess the number 😀: "))

    count += 1

    if user_number < ran_number:
        print("""
Sorry! Your guess is too low 😟.
Try again 😁.    
        """)
    elif user_number > ran_number:
        print("""
Sorry! Your guess is too high 😢.
Try again 😁.    
        """)
    else:
        print("🥳🍾 Correct 🎉🎊")

    again = input("\nDo you want to play again 🙃? Yes ☺️ or No 😒: ").upper()
    if again == 'YES':
        game = True

    else:
        user = False
        print("\nThank you for playing 😛🤪😜")
        print(f"\nIt took you {count} trials 🤭😊☺️")
        break
