import utilities.utils

# Returns kth_smallest value in input array (which is just the kth index) using quick sort partioning
def kth_smallest_quick_sort(array, k):
    # Uses standard quick sort to sort input array
    def quick_sort_standard(array, low, high, k):
        if low <= high:
            pivot_index = utilities.utils.partition(array, low, high)

            # If pivot position == kth element
            if pivot_index == k:
                return array[pivot_index]
            
            # If pivot position > k, search left sub-array
            elif pivot_index > k:
                return quick_sort_standard(array, low, pivot_index - 1, k)
            
            # If pivot position < k, search right sub-array
            else:
                return quick_sort_standard(array, pivot_index + 1, high, k)
    
    return quick_sort_standard(array, 0, len(array) - 1, k)