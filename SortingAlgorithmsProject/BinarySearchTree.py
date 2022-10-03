import math

# A SORTED list of dictionaries with the keys: 'number' and 'name'
sorted_book = [
    {"number": 1, "name": "A"},
    {"number": 2, "name": "B"},
    {"number": 3, "name": "C"},
    {"number": 4, "name": "D"},
    {"number": 5, "name": "E"},
    {"number": 6, "name": "F"},
    {"number": 7, "name": "G"},
    {"number": 8, "name": "H"}
]


def Binary_Search(original_list, query_number):
    """
    Binary search function using recursion.
    :param original_list: contains the list that we want to search
    :param query_number: contains the 'number' that we are searching for
    """
    mid_index = math.floor(len(original_list) / 2)  # gets the middle index

    # This is the "not found" exit conditions  for the recursion
    if mid_index == 0 and original_list[mid_index]["number"] != query_number:
        return "Not Found"
    # This is the "number found" exit conditions  for the recursion
    elif original_list[mid_index]["number"] == query_number:
        matching_dictionary = original_list[mid_index]
    # The remaining 2 are for triggering the recursion on either the left list or right list. The recursion will pass
    # on only the right or left list and will keep doing so until it achieves any of the recursion exit condition.
    # We did a +1 for the right list as we already know that the middle index is not what we're looking for we can
    # disregard it.
    # We try catch the output of Binary_Search with matching_dictionary so that the result is passed
    # back up the beginning of the recursion.
    elif original_list[mid_index]["number"] > query_number:
        matching_dictionary = Binary_Search(original_list[:mid_index], query_number)
    elif original_list[mid_index]["number"] < query_number:
        matching_dictionary = Binary_Search(original_list[mid_index + 1:], query_number)

    # Exit/End of the function.
    return matching_dictionary


def Binary_Search_NonRec(original_list, query_number):
    """
    Binary search function not using recursion.
    :param original_list: contains the list that we want to search
    :param query_number: contains the 'number' that we are searching for
    """
    mid_index = 0
    is_found = False
    # The conditions for exiting the while loop is when the number is found or when
    # the list size is 0 due to the query_number not found.
    while (not is_found) and (len(original_list) > 1):
        mid_index = math.floor(len(original_list) / 2)

        # Depending on the compare results we will CUT the list to either the right
        # or left and do the process of comparing then cutting the list again until
        # the while condition is met.
        if original_list[mid_index]["number"] > query_number:
            original_list = original_list[:mid_index]
        elif original_list[mid_index]["number"] < query_number:
            original_list = original_list[mid_index:]
        else:
            is_found = True

    #if the list has been cut all the way to 0 then the query_number was not found.
    if is_found:
        return original_list[mid_index]
    else:
        return "Not found"


print(Binary_Search(sorted_book, 9))
print(Binary_Search(sorted_book, 2))

print(Binary_Search_NonRec(sorted_book, 0))
print(Binary_Search_NonRec(sorted_book, 8))
