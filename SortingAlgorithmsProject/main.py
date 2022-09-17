def InsertSort(deck):
    deck_length = len(deck)
    index = 1
    while(index < deck_length):
        current_value = deck[index]
        compare_index = index - 1

        while(current_value < deck[compare_index]) and (compare_index >= 0):
            deck[compare_index + 1] = deck[compare_index]
            compare_index -= 1

        deck[compare_index +1] = current_value
        index += 1

if __name__ == '__main__':
    deck = [5, 2, 7, 9, 3, 8]
    InsertSort(deck)
    print(deck)