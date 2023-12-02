import algorithms.merge_sort
import algorithms.quick_sort_standard
import algorithms.quick_sort_medians
import utilities.utils

# Parameters for random array generation
# ARRAY_LENGTH is being tested for 2^n until we reach some hardware limit
ARRAY_LENGTH = 16
MIN_VALUE = 0
MAX_VALUE = ARRAY_LENGTH * 2

# Generate a random array
random_array = utilities.utils.generate_random_array(ARRAY_LENGTH, [MIN_VALUE, MAX_VALUE])

# Number of times to test each algorithm with each random array
ITERATIONS = 10

# Test for k
K = ARRAY_LENGTH // 2

# Switch to true to see intermediary unsorted -> sorted arrays
display_output = False

set_results = {"array_length": ARRAY_LENGTH, "results": []}

# List of algorithms to test
algorithm_list = [
    algorithms.merge_sort.kth_smallest_merge_sort,
    algorithms.quick_sort_standard.kth_smallest_quick_sort,
    algorithms.quick_sort_medians.kth_smallest_median_of_medians
]

# Test each algorithm on a given number of iterations while tracking time for execution
for algorithm in algorithm_list:
    print(f"----- {algorithm.__name__.upper()} for array_length = {ARRAY_LENGTH}, k = {K}  -----")

    if display_output:
        # Display the unsorted array
        print("Given Array:", random_array)
        
        # Use throwaway array to not sort a given array
        throwaway_array = random_array.copy()
        print("Sorted Array:", sorted(throwaway_array))
    
    execution_times = []

    for _ in range(ITERATIONS):   
        _, execution_time = utilities.utils.time_algorithm(algorithm, random_array.copy(), K)
        execution_times.append(execution_time)

        if display_output:
            # Display the sorted array
            sorted_result, _ = utilities.utils.time_algorithm(algorithm, random_array.copy(), K)
            print(f"Kth ({K}) Smallest Element:", sorted_result)

    avg_execution_time = sum(execution_times) / ITERATIONS
    set_results["results"].append({"algorithm": algorithm.__name__, 
                                   "avg_execution_time": avg_execution_time})
    print(f"Average Execution Time: {avg_execution_time:.6f} seconds")
    print("-------------------------------------------\n")
