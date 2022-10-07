import time
import random
import matplotlib.pyplot as plt


class SortingAlgorithm:
    def __init__(self):
        self.scenario_list = ["good", "base", "worse"]
        self.color_list = ["green", "blue", "red"]
        self.lengths_to_run = list(range(1, 1000, 10))
        self.average_counter = 3

    def Sort(self, list_to_sort):
        print("If you see this, you didnt override")

    def Run_Sort(self, list_to_sort, scenario):
        if scenario == "good":
            pass
        elif scenario == "base":
            random.shuffle(list_to_sort)
        elif scenario == "worse":
            list_to_sort.reverse()

        time_begin = time.time()
        self.Sort(list_to_sort=list_to_sort)
        time_end = time.time()
        time_elapsed = time_end - time_begin

        return time_elapsed

    def Plot_Sort_Performance(self):
        list_results = []
        total_time = 0
        for current_scenario, scenario_color in zip(self.scenario_list, self.color_list):
            for lengths in self.lengths_to_run:
                for iterate in range(self.average_counter):
                    initial_list = list(range(1, lengths))
                    time_elapsed = self.Run_Sort(
                        list_to_sort=initial_list,
                        scenario=current_scenario)
                    total_time += time_elapsed

                list_results.append(total_time / self.average_counter)
            plt.plot(self.lengths_to_run, list_results, color=scenario_color, label=current_scenario)
            list_results.clear()
        plt.legend()
        plt.show()
