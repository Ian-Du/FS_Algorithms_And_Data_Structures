import math

def Recursive_Merge_Sort(list_to_sort):
    """
    This function is where we apply recursion as a means to break down the
    list (divide-and-conquer). Once a list has been broken down to its singular
    components the mering and sorting then happens. Note that the split always
    happens left first. The "list" mentioned can be the original list, left list
    or right list depending on what point of the recursion you are looking at.
    :param list_to_sort: contains the list to be sorted
    :return: sorted list
    """
    if len(list_to_sort) <= 1:
        #print("Returning smallest list of 1: ", list_to_sort)
        return list_to_sort #breaks the recursion as the list can no longer be split

    mid_index = math.floor(len(list_to_sort)/2) #gets the half of the length rounded down
    left_list = list_to_sort[:mid_index]
    right_list = list_to_sort[mid_index:]
    #print("Unsorted: ", list_to_sort)
    #print("L: ", left_list, "          R: ", right_list)
    left_list = Recursive_Merge_Sort(left_list) #pass on left list to be split even further
    right_list = Recursive_Merge_Sort(right_list) #pass on right list to be split even further

    """
    The code stops here while it does the recursion. It will keep starting over
    until the recursion ends for a list (meaning its down to 1 element).
    """

    list_to_sort = Merge_List(left_list, right_list)
    #print("Sorted: ", list_to_sort)
    return list_to_sort

def Merge_List(left_list, right_list):
    """
    :param left_list: contains the left half of the list to be merged
    :param right_list: contains the right half of the list to be merged
    :return: merged and sorted list from the left and right list
    """
    #print("MERGE L:", left_list, "     R:", right_list)
    left_list_length = len(left_list)
    right_list_length = len(right_list)
    merged_list = []
    left_index = 0
    right_index = 0

    """
    This while loop will compare the left list and the right list to get 
    the lower value and add it to the merged list. It will keep doing this
    until either left or right list have been fully compared. 
    """
    while left_index < left_list_length and right_index < right_list_length:
        #print("Comparing L-Index:", left_index, "     R-Index", right_index, end="     ")
        if left_list[left_index] <= right_list[right_index]:
            merged_list.append(left_list[left_index])
            left_index += 1
        else:
            merged_list.append(right_list[right_index])
            right_index += 1
        #print("Merged List after compare: ", merged_list)

    """
    Insert the remaining values in the left and/or right lists that have not been 
    added to the merged list. With the left list being added first since the left 
    values will always be less than the right values
    """
    if left_index < left_list_length:
        #print("Appending remaining values from left list: ", left_list[left_index:])
        merged_list.extend(left_list[left_index:])

    if right_index < right_list_length:
        #print("Appending remaining values from right list: ", right_list[right_index:])
        merged_list.extend(right_list[right_index:])

    return merged_list