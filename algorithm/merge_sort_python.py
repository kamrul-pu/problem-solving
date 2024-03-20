"""Merge Sort Implementation in Python."""

from typing import List


class MergeSort:
    def __init__(self, arr: List[int]) -> None:
        """
        Initialize the MergeSort object with an array to be sorted.
        """
        self.arr: List[int] = arr

    def __merge(self, low: int, mid: int, high: int) -> None:
        """
        Merge two sorted subarrays into a single sorted array.

        Parameters:
            low (int): Starting index of the first subarray.
            mid (int): Ending index of the first subarray and starting index of the second subarray.
            high (int): Ending index of the second subarray.
        """
        temp: List[int] = []  # Temporary array to store merged elements.
        left: int = low  # Pointer for the left subarray.
        right: int = mid + 1  # Pointer for the right subarray.

        # Compare elements from both subarrays and merge them into the temporary array.
        while left <= mid and right <= high:
            if self.arr[left] < self.arr[right]:
                temp.append(self.arr[left])
                left += 1
            else:
                temp.append(self.arr[right])
                right += 1

        # Copy remaining elements from the left subarray, if any.
        while left <= mid:
            temp.append(self.arr[left])
            left += 1

        # Copy remaining elements from the right subarray, if any.
        while right <= high:
            temp.append(self.arr[right])
            right += 1

        # Copy the sorted elements from the temporary array back to the original array.
        for i in range(low, high + 1):
            self.arr[i] = temp[i - low]

    def __mergeSort(self, low: int, high: int) -> None:
        """
        Recursive function to divide the array into subarrays and merge them.

        Parameters:
            low (int): Starting index of the subarray to be sorted.
            high (int): Ending index of the subarray to be sorted.
        """
        if low < high:
            mid: int = (low + high) // 2  # Calculate the middle index.
            # Recursively sort the left and right subarrays.
            self.__mergeSort(low=low, high=mid)
            self.__mergeSort(low=mid + 1, high=high)
            # Merge the sorted subarrays.
            self.__merge(low=low, mid=mid, high=high)

    def sort_util(self) -> None:
        """
        Utility function to start the merge sort process.
        """
        low: int = 0  # Starting index of the array.
        high: int = len(self.arr) - 1  # Ending index of the array.
        # Call the recursive merge sort function.
        self.__mergeSort(low=low, high=high)


if __name__ == "__main__":
    arr = [40, 25, 19, 12, 13, 33]
    print("Original Array:", arr)
    ms: MergeSort = MergeSort(arr=arr)
    ms.sort_util()
    print("Sorted Array:", arr)
