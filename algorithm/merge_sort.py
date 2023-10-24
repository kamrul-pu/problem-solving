"""
Merge SOrt in Python.
Work in devide and conquer approach.
Complexity
Time O(nlogn)
Space O(nlogn)
"""
INT_MAX = 1e5 + 10


def merge_two_sorted_list(a, b):
    sorted_list = []
    i = j = 0
    # Append a dummy value to avaoid another two loop for last value
    a.append(INT_MAX)
    b.append(INT_MAX)
    len_a = len(a)
    len_b = len(b)

    while i < len_a and j < len_b:
        if a[i] < b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    # ignore the last value which is int max
    return sorted_list[:-1]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # merge left array
    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_list(left, right)


if __name__ == "__main__":
    numbers = [38, 9, 29, 7, 2, 15, 28]
    print(merge_sort(numbers))
