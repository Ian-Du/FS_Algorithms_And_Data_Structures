import math

def Recursive_Merge_Sort(list_to_sort):

    if len(list_to_sort) <= 1:
        #print("Returning smallest list of 1: ", list_to_sort)
        return list_to_sort

    mid_index = math.floor(len(list_to_sort)/2)

    left_list = Recursive_Merge_Sort(list_to_sort[:mid_index])
    right_list = Recursive_Merge_Sort(list_to_sort[mid_index:])

    list_to_sort = Merge_List(left_list, right_list)
    #print("Sorted: ", list_to_sort)
    return list_to_sort

def Merge_List(left_list, right_list):
    #print("MERGE L:", left_list, "     R:", right_list)
    left_list_length = len(left_list)
    right_list_length = len(right_list)
    merged_list = []
    left_index = 0
    right_index = 0

    while left_index < left_list_length and right_index < right_list_length:
        #print("Comparing L-Index:", left_index, "     R-Index", right_index, end="     ")
        if left_list[left_index] <= right_list[right_index]:
            merged_list.append(left_list[left_index])
            left_index += 1
        else:
            merged_list.append(right_list[right_index])
            right_index += 1
        #print("Merged List after compare: ", merged_list)

    if left_index < left_list_length:
        #print("Appending remaining values from left list: ", left_list[left_index:])
        merged_list.extend(left_list[left_index:])

    if right_index < right_list_length:
        #print("Appending remaining values from right list: ", right_list[right_index:])
        merged_list.extend(right_list[right_index:])

    return merged_list