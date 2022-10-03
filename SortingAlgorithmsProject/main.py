from InsertionSort import Insertion_Sort
from MergeSort import Recursive_Merge_Sort
from BinarySearchTree import Binary_Search
from BinarySearchTree import Binary_Search_NonRec
from BinarySearchTree import sorted_book
import time
import random
import matplotlib.pyplot as plt

scenario_list = ["good", "base", "worse"]
color_list = ["green", "blue", "red"]
lengths_to_run = list(range(1, 5000, 100))


def Run_Sort(list_, scenario):
    if scenario == "good":
        pass
    elif scenario == "base":
        random.shuffle(list_)
    elif scenario == "worse":
        list_.reverse()

    time_begin = time.time()
    Insertion_Sort(list_to_sort=list_)
    time_end = time.time()
    time_elapsed = time_end - time_begin

    return time_elapsed


def Plot_Insertion_Sort_Performance():
    list_results = []
    for current_scenario, scenario_color in zip(scenario_list, color_list):
        for lengths in lengths_to_run:
            list_to_be_sorted = list(range(1, lengths))
            time_elapsed = Run_Sort(list_=list_to_be_sorted, scenario=current_scenario)
            list_results.append(time_elapsed)
        print("scenario:", current_scenario)
        print(list_results)
        plt.plot(lengths_to_run, list_results, color=scenario_color, label=current_scenario)
        list_results.clear()
    plt.legend()
    plt.show()


def Run_Specific_Sort(list_, scenario, sorting_algo):
    if scenario == "good":
        pass
    elif scenario == "base":
        random.shuffle(list_)
    elif scenario == "worse":
        list_.reverse()

    time_begin = time.time()

    match sorting_algo:
        case "Insert":
            Insertion_Sort(list_to_sort=list_)
        case "Merge":
            Recursive_Merge_Sort(list_to_sort=list_)

    time_end = time.time()
    time_elapsed = time_end - time_begin

    return time_elapsed


def Plot_Specific_Sort_Performance(sorting_algo):
    list_results = []
    for current_scenario, scenario_color in zip(scenario_list, color_list):
        for lengths in lengths_to_run:
            list_to_be_sorted = list(range(1, lengths))
            time_elapsed = Run_Specific_Sort(
                list_=list_to_be_sorted,
                scenario=current_scenario,
                sorting_algo=sorting_algo)
            list_results.append(time_elapsed)
        plt.figure(sorting_algo)
        plt.plot(lengths_to_run, list_results, color=scenario_color, label=current_scenario)
        list_results.clear()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    temp_list = [8, 7, 6, 5, 4, 3, 2, 1]
    # Recursive_Merge_Sort(temp_list)
    # Plot_Insertion_Sort_Performance()
    #Plot_Specific_Sort_Performance("Insert")
    Plot_Specific_Sort_Performance("Merge")