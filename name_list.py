def name_list():
    """
    Create a dictionary of names based on user's input.

    The dictionary's keys will be integers representing the number of letters in a name,
    and the values will be lists that contain names of that length.

    :precondition: user input name must be a string
    :postcondition: create a dictionary with names user inputted
    :return:a dictionary, the dictionary's keys will be integers representing the number of letters in a name,
            and the values will be lists that contain names of that length.
    """
    name_dict = {}
    while True:
        user_input_name = input('Enter a name, enter "quit" when you finish:')

        if user_input_name != 'quit':
            break

        name_length = len(user_input_name)
        if name_length in name_dict:
            name_dict[name_length].append(user_input_name)
        else:
            name_dict[name_length] = [user_input_name]

    return name_dict


def main():
    print(name_list())


if __name__ == "__main__":
    main()