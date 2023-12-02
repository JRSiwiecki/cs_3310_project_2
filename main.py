import algorithms.merge_sort
import utilities.utils

# Parameters for random array generation
array_length = 1000
min_value = 0
max_value = 100

# Generate a random array
random_array = utilities.utils.generate_random_array(array_length, [min_value, max_value])

# Number of times to test each algorithm with each random array
iterations = 5

# Test for k
k = 0

# Switch to true to see intermediary unsorted -> sorted arrays
display_output = False

set_results = {"array_length": array_length, "results": []}

# List of algorithms to test
algorithm_list = [
    algorithms.merge_sort.merge_sort
]

# Test each algorithm on a given number of iterations while tracking time for execution
for algorithm in algorithm_list:
    print(f"----- {algorithm.__name__.upper()} for array_length = {array_length}, k = {k}  -----")

    if display_output:
        # Display the unsorted array
        print("Given Array:", random_array)
    
    execution_times = []

    for _ in range(iterations):
        _, execution_time = utilities.utils.time_algorithm(utilities.utils.kth_smallest_element, 
                                                           algorithm, random_array, k)
        execution_times.append(execution_time)

        if display_output:
            # Display the sorted array
            sorted_result, _ = utilities.utils.time_algorithm(utilities.utils.kth_smallest_element, 
                                                              algorithm, random_array, k)
            print("Sorted Array:", sorted_result)

    avg_execution_time = sum(execution_times) / iterations
    set_results["results"].append({"algorithm": algorithm.__name__, 
                                   "avg_execution_time": avg_execution_time})
    print(f"Average Execution Time: {avg_execution_time:.6f} seconds")
    print("-------------------------------------------\n")
