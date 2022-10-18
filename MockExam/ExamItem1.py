# Note:
#   Complexity of O(N/2) as it has to iterate through the entire word on
#   both ends thus effectively splitting the time/number of iteration it takes
#   to complete the task
#   Assumes that a single letter or empty string is considered a palindrome
# Step 1:
#   Get the left most and right most character of the word and check
#   if not equal then return false and break loop
# Step 2:
#   increment index of left by 1 and decrement the index of right by 1
# Step 3:
#   check if these new values have gone past/reached their center values
#   (i.e. left is now greater than right for even length words or
#   left is equal to right for odd length words) then break loop since we
#   have checked the whole word
# Step 4:
#   repeat step one with the new left most and right most characters.

def Is_Pal_Rec(val_to_check, left_most_idx, right_most_idx):
    # If there is only one character or
    # left and right have gone past each other, then return true
    if (left_most_idx == right_most_idx or
            left_most_idx > right_most_idx):
        return True

    # If left most and right most characters do not match return false
    if val_to_check[left_most_idx] != val_to_check[right_most_idx]:
        return False

    # Keep recursion going until the word is checked as a palindrome(TRUE) or
    # not a palindrome (FALSE)
    return Is_Pal_Rec(val_to_check, left_most_idx + 1, right_most_idx - 1)


def Is_Palindrome(val_to_check):
    val_length = len(val_to_check)
    val_to_check = val_to_check.lower()

    # An empty string is
    # considered as palindrome
    if val_length == 0:
        return True

    return Is_Pal_Rec(val_to_check, 0, val_length - 1)


print(Is_Palindrome("Anna"))
print(Is_Palindrome("test"))
print(Is_Palindrome("mom"))
