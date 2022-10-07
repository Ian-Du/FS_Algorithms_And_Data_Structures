import math
from SortingAlgorithm import SortingAlgorithm


class MergeSort(SortingAlgorithm):

    def Sort(self, list_to_sort):

        if len(list_to_sort) <= 1:
            return list_to_sort

        mid_index = math.floor(len(list_to_sort) / 2)

        left_list = self.Sort(list_to_sort[:mid_index])
        right_list = self.Sort(list_to_sort[mid_index:])

        list_to_sort = self.Merge_List(left_list, right_list)
        return list_to_sort

    def Merge_List(self, left_list, right_list):
        left_list_length = len(left_list)
        right_list_length = len(right_list)
        merged_list = []
        left_index = 0
        right_index = 0

        while left_index < left_list_length and right_index < right_list_length:
            if left_list[left_index] <= right_list[right_index]:
                merged_list.append(left_list[left_index])
                left_index += 1
            else:
                merged_list.append(right_list[right_index])
                right_index += 1

        if left_index < left_list_length:
            merged_list.extend(left_list[left_index:])

        if right_index < right_list_length:
            merged_list.extend(right_list[right_index:])

        return merged_list


test_sort_algo = MergeSort()
test_sort_algo.Plot_Sort_Performance()
