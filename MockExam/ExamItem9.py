
def Get_List(list_to_search, given_val):
    ret_list = []
    while len(list_to_search) > 1:
        comp_val = list_to_search.pop()
        if (given_val - comp_val) in list_to_search:
            ret_list.append([comp_val, given_val - comp_val])
    return ret_list


print(Get_List([3, 4, 1, 7, 9, 17, 5], 8))
print(Get_List([3, 4, 1, 7, 9, 17], 10))
print(Get_List([3, 4, 1, 7, 9, 4, 17, 12], 21))
