from SortingAlgorithm import SortingAlgorithm


class QuickSort(SortingAlgorithm):
    def Sort(self, list_to_sort):
        self.Quick_Sort(list_to_sort, 0, len(list_to_sort) - 1)
    
    def Quick_Sort(self, list_to_sort, low_idx, high_idx):
        if low_idx < high_idx:
            partition = self.Partition(list_to_sort, low_idx, high_idx)
            self.Quick_Sort(list_to_sort, low_idx, partition - 1)
            self.Quick_Sort(list_to_sort, partition + 1, high_idx)
    
    
    def Partition(self, list_to_sort, low_idx, high_idx):
        pivot_idx = self.get_pivot(list_to_sort, low_idx, high_idx)
        pivot_val = list_to_sort[pivot_idx]
        list_to_sort[pivot_idx], list_to_sort[low_idx] = list_to_sort[low_idx], list_to_sort[pivot_idx]
        swap_idx = low_idx
    
        for compare_idx in range(low_idx, high_idx + 1):
            if list_to_sort[compare_idx] < pivot_val:
                swap_idx += 1
                list_to_sort[compare_idx], list_to_sort[swap_idx] = list_to_sort[swap_idx], list_to_sort[compare_idx]
        list_to_sort[low_idx], list_to_sort[swap_idx] = list_to_sort[swap_idx], list_to_sort[low_idx]
    
        return swap_idx
    
    
    def get_pivot(self, list_to_search, low_idx, high_idx):
        mid_idx = (high_idx + low_idx) // 2
        sorted_pivots = sorted([list_to_search[low_idx], list_to_search[mid_idx], list_to_search[high_idx]])
        if sorted_pivots[1] == list_to_search[low_idx]:
            return low_idx
        elif sorted_pivots[1] == list_to_search[mid_idx]:
            return mid_idx
        return high_idx


test_sort_algo = QuickSort()
test_sort_algo.Plot_Sort_Performance()
