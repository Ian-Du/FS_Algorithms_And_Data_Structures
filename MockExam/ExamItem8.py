# Note:
#
# Step 1:
#   create a temporary dictionary. this will house the word as key and frequency as value
# Step 2:
#   iterate through each word in the list and check if it already exists as a key in the
#   dictionary if it does increase the frequency by 1 if not addd it in the dictionary.
# Step 2:
#   return dictionary once finished checking the entire list
import tabulate

def Display_Frequency(list_to_check):
    ret_dict = Get_Frequency(list_to_check=list_to_check)

    for dict_key in ret_dict:
        print(dict_key, " ", ret_dict[dict_key])
    print(ret_dict)

def Get_Frequency(list_to_check):
    ret_dict = {}
    for word in list_to_check:
        if word in ret_dict:
            ret_dict[word] += 1
        else:
            ret_dict[word] = 1

    return ret_dict


list_of_words = ["hi", "I", "am", "Alexa", "I", "would", "just", "like", "to", "say", "hi"]
Display_Frequency(list_to_check=list_of_words)

list_of_words = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "brown", "dog", "over", "and", "over", "again"]
Display_Frequency(list_to_check=list_of_words)





