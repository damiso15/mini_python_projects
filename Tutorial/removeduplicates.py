# Write a program (function!) that takes a list and returns a new list that contains all the elements of the
# first list minus all the duplicates.

# init_list = list(input("Enter the all the elements: "))
# translation = {39: None}
# print(str(init_list).translate(translation))


def remove_duplicate(init_list):

    # init_list = list(input("Enter the all the elements: "))
    # Using Translation Method will return a List without any apostrophe.
    translation = {39: None}
    new_list = []

    for item in init_list:
        if item not in new_list:
            new_list.append(item)
    return str(new_list).translate(translation)


init_list = list(input("Enter the all the elements: "))
result = remove_duplicate(init_list)
print(result)
