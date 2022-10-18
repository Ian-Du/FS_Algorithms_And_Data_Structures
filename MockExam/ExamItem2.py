# Note:
#   O((n^3)/2) not sure about the /2 part.
#   Assumes that a single letter or empty string is considered a palindrome
# Step 1:
#   Consider pivot_idx as the middle/pivot point of comparison to be used as we traverse the entire input_string.
#   Starting with the first index 0
# Step 2:
#   Take pivot_idx and set it as the left_idx and right_idx this is to search for odd length palindromes.
# Step 3:
#   If values in left_idx and right_idx are the same then store the substring bounded by left and right indexes
# Step 4:
#   Decrement left_idx by 1 and increment right_idx by 1.
# Step 5:
#   Repeat step 2 and 3 as long as left_idx or right_idx do not exceed the allowed index of input_string and condition
#   on step 3 is true.
# Step 6:
#   take pivot_idx and set it as the left_idx and pivot_idx + 1 as the right_idx. This is to search for even length
#   palindromes. Do step 3, 4 and 5 using new starting values of left_idx and right_idx
# Step 7:
#   increase pivot_idx by 1 and repeat all steps starting at 2 as long as pivot_idx is smaller than the length of the
#   string.

def Palindrome_SubString(input_string, left_idx, right_idx):
    palindrome_list = set() #using a set to prevent duplicates

    #Given the starting points of comparison for the string
    #Store the all substring based on the left and right indexes
    while (left_idx >= 0 and
           right_idx < len(input_string) and
           input_string[left_idx] == input_string[right_idx]):

        palindrome_list.add(input_string[left_idx: right_idx + 1])

        # Expand in both directions
        left_idx -= 1
        right_idx += + 1

    return palindrome_list


def Get_All_Palindrome(input_string):
    palindrome_list = set() #using a set to prevent duplicates
    pivot_idx = 0

    while pivot_idx < len(input_string)-1:
        # find all odd length palindrome with character starting at pivot_idx as a midpoint (e.g.: mom)
        palindrome_list.update(Palindrome_SubString(input_string, pivot_idx, pivot_idx))

        # find all even length palindrome with characters starting at pivot_idx and pivot_idx + 1
        # as its midpoints (e.g.: anna)
        palindrome_list.update(Palindrome_SubString(input_string, pivot_idx, pivot_idx+1))

        pivot_idx += 1

    return palindrome_list


print(Get_All_Palindrome("abbccc mom"))