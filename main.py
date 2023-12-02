from algorithms.merge_sort import kth_smallest_merge_sort

test = [4, 3, 6, 1, 9, 10, 2, 5]
low = 0
high = len(test)

kth_smallest_merge_sort(low, high, test)

print(test)