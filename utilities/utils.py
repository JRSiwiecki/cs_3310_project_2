import random
import time

# Returns kth_smallest value in input array (which is just the kth index)
def kth_smallest_element(algorithm, array, k):
    # Sort array first using given algorithm
    sorted_array = algorithm(array)

    # Return number at index k
    return sorted_array[k], sorted_array

# Generates random array of specified size with values within given number range
def generate_random_array(array_size, number_range):
    MIN_VALUE, MAX_VALUE = number_range

    random_array = []

    for i in range(array_size):
        random_array.append(random.randint(MIN_VALUE, MAX_VALUE))
    
    return random_array

# Times a given algorithm and returns the algorithm result and its execution time
def time_algorithm(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Merges two subarrays together, appending values by which is smaller, first
def merge(left_subarray, right_subarray):
    
    # Empty merged array to hold final sorted array
    merged_array = []
    
    # Pointers to track current number for each subarray
    left_pointer = 0
    right_pointer = 0

    # Go through value in each subarray until none left in at least one subarray
    while left_pointer < len(left_subarray) and right_pointer < len(right_subarray):
        
        # Compare current value in each subarray to determine which is smaller
        if left_subarray[left_pointer] < right_subarray[right_pointer]:
            merged_array.append(left_subarray[left_pointer])
            left_pointer += 1
        
        else:
            merged_array.append(right_subarray[right_pointer])
            right_pointer += 1
    
    # Append any leftovers of either array to the merged sorted array
    merged_array.extend(left_subarray[left_pointer:])
    merged_array.extend(right_subarray[right_pointer:])

    return merged_array

# Partition array into subarrays
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1