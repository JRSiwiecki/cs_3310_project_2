from random import randint

def generate_random_arrays(array_size, number_range):
    MIN_VALUE, MAX_VALUE = number_range

    random_array = []

    for i in range(array_size):
        random_array.append(randint(MIN_VALUE, MAX_VALUE))
    
    return random_array

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