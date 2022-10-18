# Note:
#   Complexity of O(N) as it has to iterate through the entire list
#   n starts at index 0
# Step 1:
#   Check if value of index n > value of index n+1 then
#       - Display that the list is not ascending
#       - End loop and function
# Step 2:
#   increment index n by 1
# Step 3:
#   Repeat to step 1 and 2 until index n < the length of the list minus 1
# Step 4:
#   If at no point was the loop broken and the whole list was checked then
#       - Display that the list is ascending

def Is_List_Ascending(list_to_check):
    index = 0
    while len(list_to_check)-1 > index:
        if list_to_check[index] >= list_to_check[index+1]:
            print("Not Ascending")
            return
        index += 1
    print("Ascending")
    return

Is_List_Ascending([1,2,3,5,6,7,11])
Is_List_Ascending([1,2,3,9,6,7,11])