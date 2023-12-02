from utilities.utils import merge

def kth_smallest_merge_sort(k, array):
    # Sort array first
    sorted_array = merge_sort(array)

    # Return number at index k
    return sorted_array[k]


def merge_sort(array):
    # Find midpoint/splitpoint
    midpoint = len(array) // 2

    # Divide array into two somewhat equal subarrays
    left_subarray = array[:midpoint]
    right_subarray = array[midpoint:]

    # Recursively merge sort subarrays until only one value left in subarray
    if len(left_subarray) > 1:
        left_subarray = merge_sort(left_subarray)
    if len(right_subarray) > 1:
        right_subarray = merge_sort(right_subarray)
    
    # Merge sorted subarrays
    return merge(left_subarray, right_subarray)