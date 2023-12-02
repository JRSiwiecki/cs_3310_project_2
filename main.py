import algorithms.merge_sort
import algorithms.quick_sort_standard
import utilities.utils

# Parameters for random array generation
ARRAY_LENGTH = 10
MIN_VALUE = 0
MAX_VALUE = ARRAY_LENGTH + 1

# Generate a random array
random_array = utilities.utils.generate_random_array(ARRAY_LENGTH, [MIN_VALUE, MAX_VALUE])

# Number of times to test each algorithm with each random array
ITERATIONS = 5

# Test for k
K = 5

# Switch to true to see intermediary unsorted -> sorted arrays
display_output = True

set_results = {"array_length": ARRAY_LENGTH, "results": []}

# List of algorithms to test
algorithm_list = [
    algorithms.merge_sort.kth_smallest_merge_sort,
    algorithms.quick_sort_standard.kth_smallest_quick_sort
]

# Test each algorithm on a given number of iterations while tracking time for execution
for algorithm in algorithm_list:
    print(f"----- {algorithm.__name__.upper()} for array_length = {ARRAY_LENGTH}, k = {K}  -----")

    if display_output:
        # Display the unsorted array
        print("Given Array:", random_array)
    
    execution_times = []

    for _ in range(ITERATIONS):   
        _, execution_time = utilities.utils.time_algorithm(algorithm, random_array, K)
        execution_times.append(execution_time)

        if display_output:
            # Display the sorted array
            sorted_result, _ = utilities.utils.time_algorithm(algorithm, random_array, K)
            print("Sorted Array:", sorted_result)

    avg_execution_time = sum(execution_times) / ITERATIONS
    set_results["results"].append({"algorithm": algorithm.__name__, 
                                   "avg_execution_time": avg_execution_time})
    print(f"Average Execution Time: {avg_execution_time:.6f} seconds")
    print("-------------------------------------------\n")
