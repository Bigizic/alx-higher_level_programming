#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    """Documentation:
    This function divides elements in list1 by elements in list2
    both lists can contain any type
    list_length can be longer than the length of both lists
    if 2 elements can't be divided the result will be 0
    if an element is not an int type or float it will print "wrong type"
    if the division can't be done i.e element1 / 0 it prints "division by 0"
    if list1 or list2 is too short it prints "out of range"
    """

    new_list = []  # Decleares a new list

    div = False  # Handles error message for dision by 0

    max_range = False  # handles error message for out of range

    wrong_type = False  # handles error message for wrong type

    double_max_range = False  # handles error message when a list too short

    try:
        """Iteration through list1
        this method gets the index and the elements in list1
        """

        for index, element in enumerate(my_list_1):
            """Elment type check
            a condition that checks if an element is not an int
            or float type and if true it gets the index of that element
            using the index in the enumerate for loop and updates the
            element to 0
            """

            if not isinstance(element, (int, float)):
                my_list_1[index] = 0

                """Wrong type error
                sets wrong type to "True" to indicate an encountered
                wrong type of element
                """
                wrong_type = True
        for i, e in enumerate(my_list_2):
            if not isinstance(e, (int, float)):
                my_list_2[i] = 0
                wrong_type = True

                """List too short"
                sets out of range error if a list length is zero
                """
        if len(my_list_2) == 0:
            double_max_range = True

            """List_length
            iterate through the newly list1 and list2 and use a range of
            list_length to iterate through every element in the list
            """
        for x in range(list_length):

            """Out of range error
            if list_length is greater than the length of both list
            then out of range error is True and result is set to 0
            to append it to the remaining length of the list, where
            list_length is 7 and both list length are neither 7 the
            remaining elements to complete 7 elements in the list would
            ZEROS
            """
            if x >= len(my_list_1) or x >= len(my_list_2):
                result = 0
                max_range = True

                """Extra check
                if any element in list1 is 0 and if wrong_type
                for either elements is true it append 0 to the
                new list
                """
            elif my_list_1[x] == 0 and wrong_type:
                result = 0

                """Division by 0 error
                if any element in my list2 is zero then append 0
                to new list and set the divsion by zero error to true
                """
            elif my_list_2[x] == 0:
                result = 0
                div = True
            else:
                result = my_list_1[x] / my_list_2[x]

            new_list.append(result)
    except nothing:
        pass
    finally:
        if div:
            print("division by 0")
        if wrong_type:
            print("wrong type")
        if max_range:
            print("out of range")
        if double_max_range:
            print("out of range")
        return new_list
