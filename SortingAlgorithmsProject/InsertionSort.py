def Insertion_Sort(list_to_sort):
    deck_length = len(list_to_sort)
    index = 1
    while(index < deck_length):
        current_value = list_to_sort[index]
        compare_index = index - 1

        while(current_value < list_to_sort[compare_index]) and (compare_index >= 0):
            list_to_sort[compare_index + 1] = list_to_sort[compare_index]
            compare_index -= 1

        list_to_sort[compare_index + 1] = current_value
        index += 1