# Note:
#   Complexity of O(N) as it has to iterate through both strings
# Step 1:
#   Check if both strings have same length if not then return FALSE
# Step 2:
#   Make a dictionary of both string containing a count of each unique
#   letter.
# Step 3:
#   Compare the dictionaries and see if the values/counts of each letter
#   are the same. If same then return TRUE otherwise FALSE


def Is_Anagram(string1, string2):
    if len(string1) != len(string2):
        return False

    string1 = string1.lower()
    string2 = string2.lower()

    dict1 = Assemble_Dictionary(string1)
    dict2 = Assemble_Dictionary(string2)

    for char_dict in dict1:
        if (char_dict not in dict2 or
                dict1[char_dict] is not dict2[char_dict]):
            return False

    return True


def Assemble_Dictionary(string_to_sort):
    ret_dict = {}
    for character in string_to_sort:
        if character in ret_dict:
            ret_dict[character] += 1
        else:
            ret_dict[character] = 1

    return ret_dict


print(Is_Anagram("test", "sett"))
print(Is_Anagram("test", "bett"))
print(Is_Anagram("anna", "nana"))