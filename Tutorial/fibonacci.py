# Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonacci sequence is a sequence of numbers where the next number in the sequence is the sum of the
# previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def fibonacci(nth_time):

    # nth_time = int(input("Enter the number of sequence to be generated: "))
    n0 = 1
    n1 = 2
    count = 0
    new_list = []

    if nth_time <= 0:
        print("\nNumber must be a positive integer: ")
    elif nth_time == 1:
        new_list.append(nth_time)
        print(f"\nFibonacci sequence: {new_list}")
    else:
        while count < nth_time:
            new_list.append(n0)
            nth = n0 + n1
            n0 = n1
            n1 = nth
            count += 1
            new_list.append(nth)
        return f"\nFibonacci sequence:{new_list}"


nth_time = int(input("Enter the number of sequence to be generated: "))
result = fibonacci(nth_time)
print(result)
