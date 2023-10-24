"""
Quick Sort Algorithm.
# Complexicity Space O(1)
# Complexicity Time AVG O(nlogn) Worst O(n^2)
"""

count = 0


def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def partition(elements, start, end):
    global count
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
            count += 1

        while elements[end] > pivot:
            end -= 1
            count += 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)
    return end


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        # Left Partition
        quick_sort(elements, start, pi - 1)
        # Right Partition
        quick_sort(elements, pi + 1, end)


if __name__ == "__main__":
    numbers = [38, 9, 29, 7, 2, 15, 28]
    # numbers = [2, 7, 9, 15, 28, 29, 38]
    # numbers = range(1, 1000)
    # Sort the list
    quick_sort(numbers, 0, len(numbers) - 1)
    print("after sort: ", numbers)
    print(count)
