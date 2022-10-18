# Note:
#   Complexity of O(N) as it has to iterate through the entire list
#   n starts at index 0
# Step 1:
#   Set n as first index of list.
#   Increment the current sequence by 1
# Step 2:
#   Check if value of index n > value of index n+1 then
#       - check if the current sequence is the longest then set it as the
#         longest sequence and reset current sequence counter
# Step 3:
#   increment index n by 1
# Step 4:
#   Repeat to step 1 and 2 until index n < the length of the list minus 1
# Step 5:
#   return longest sequence value

def Is_List_Ascending(list_to_check):
    index = 0
    long_seq = []
    current_seq = []
    while len(list_to_check)-1 > index:
        current_seq.append(list_to_check[index])
        if list_to_check[index] > list_to_check[index+1]:
            if len(current_seq) > len(long_seq):
                long_seq.clear()
                long_seq = current_seq
            current_seq.clear()
        index += 1

    # This is due to using len(list_to_check)-1 > index in the while loop
    # we end up looping shorter than the actual length of the list and lose
    # the last index
    current_seq.append(list_to_check[index])
    # This is for when we encounter a list that is ascending meaning the
    # whole list is the longest sequence or the sequence was the last
    # sequence stored.
    if len(current_seq) > len(long_seq):
        long_seq = current_seq
    return long_seq


print(Is_List_Ascending([1,2,3,0,6,3,11])) #3
print(Is_List_Ascending([1,2,3,4,5,6,7])) #7
print(Is_List_Ascending([1,2,3,0,9,6,7,9,11,0,1,2,3,4,5,6,7,8,9])) #4