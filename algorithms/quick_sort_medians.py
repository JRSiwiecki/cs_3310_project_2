import utilities.utils

# Returns kth_smallest value in input array (which is just the kth index) using quick sort median of medians
def kth_smallest_median_of_medians(array, k):
    # Divide array into sub-arrays of size 5
    sub_arrays = [sorted(array[i: i + 5]) for i in range(0, len(array), 5)]

    # Find median of each subarray
    medians = [sub_array[len(sub_array) // 2] for sub_array in sub_arrays]

    # Find pivot index using median of medians
    if len(medians) <= 5:
        pivot_index = sorted(medians)[len(medians) // 2]
    else:
        pivot_index = kth_smallest_median_of_medians(medians, len(medians) // 2)
    
    # Partition array around pivot_index
    left = [x for x in array if x < pivot_index]
    right = [x for x in array if x > pivot_index]
    middle = [x for x in array if x == pivot_index]

    # Recursively search in correct sub_array
    if k < len(left):
        return kth_smallest_median_of_medians(left, k)
    elif k < len(left) + len(middle):
        return pivot_index
    else:
        return kth_smallest_median_of_medians(right, k - len(left) - len(middle))
