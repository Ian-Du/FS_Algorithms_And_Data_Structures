def Sort(list_to_sort):
    Quick_Sort(list_to_sort, 0, len(list_to_sort) - 1)

def Quick_Sort(list_to_sort, low_idx, high_idx):
    if low_idx < high_idx:
        partition = Partition(list_to_sort, low_idx, high_idx)
        Quick_Sort(list_to_sort, low_idx, partition - 1)
        Quick_Sort(list_to_sort, partition + 1, high_idx)


def Partition(list_to_sort, low_idx, high_idx):
    pivot_idx = get_pivot(list_to_sort, low_idx, high_idx)
    pivot_val = list_to_sort[pivot_idx]
    list_to_sort[pivot_idx], list_to_sort[low_idx] = list_to_sort[low_idx], list_to_sort[pivot_idx]
    #print("put pivot :",list_to_sort)
    swap_indx = low_idx
    #print (f"low: {low_idx}, high: {high_idx}, pivot val:{pivot_val}")
    for compare_idx in range(low_idx, high_idx + 1):
        #print(f"Index: {compare_idx}, Val: {list_to_sort[compare_idx]}, swap index: {swap_indx}")
        if list_to_sort[compare_idx] < pivot_val:
            #print("swap")
            swap_indx += 1
            list_to_sort[compare_idx], list_to_sort[swap_indx] = list_to_sort[swap_indx], list_to_sort[compare_idx]
    list_to_sort[low_idx], list_to_sort[swap_indx] = list_to_sort[swap_indx], list_to_sort[low_idx]

    #print(list_to_sort)
    return swap_indx


def get_pivot(list_to_search, low_idx, high_idx):
    mid_idx = (high_idx + low_idx) // 2
    sorted_pivots = sorted([list_to_search[low_idx], list_to_search[mid_idx], list_to_search[high_idx]])
    if sorted_pivots[1] == list_to_search[low_idx]:
        return low_idx
    elif sorted_pivots[1] == list_to_search[mid_idx]:
        return mid_idx
    return high_idx

def trysort(list_to_sort):
    if len(list_to_sort) <= 1:
        #print("Returning smallest list of 1: ", list_to_sort)
        return list_to_sort

    pivot_idx = get_pivot(list_to_sort, 0, len(list_to_sort) - 1)
    pivot_val = list_to_sort[pivot_idx]




#temp_list = [9, 7, 3, 2, 8, 1]
#print(temp_list)
#Sort(temp_list)
