# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.


def prime_number(num):

    # num = int(input("Enter a number: "))

    if num > 1:
        # check for factors
        for i in range(2, num):
            if num % i == 0:
                print(f"\n{num}, is not a prime number")
                print(f"\n{i} X {num // i} is {num}")
                break
        else:
            print(f"\n{num}, is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        return f"\n{num}, is not a prime number"


number = int(input("Enter a number: "))
result = prime_number(number)
print(result)
