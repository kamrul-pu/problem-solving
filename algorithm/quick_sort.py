"""
Quick Sort Algorithm.
Complexity Space: O(1)
Complexity Time: AVG O(nlogn), Worst O(n^2)
"""

from typing import List


class QuickSort:
    def __init__(self, arr: List[int]) -> None:
        """
        Initialize the QuickSort object with an array to be sorted.

        Parameters:
            arr (List[int]): The array to be sorted.
        """
        self.arr: List[int] = arr

    def __partition(self, low: int, high: int) -> int:
        """
        Partition the array around a pivot element and return the index of the pivot.

        Parameters:
            low (int): Starting index of the partition.
            high (int): Ending index of the partition.

        Returns:
            int: Index of the pivot element after partitioning.
        """
        # Choose the first element as the pivot
        pivot: int = self.arr[low]
        i: int = low  # Initialize pointer for the left subarray
        j: int = high  # Initialize pointer for the right subarray

        # Loop until the pointers cross each other
        while i < j:
            # Move 'i' to the right until it finds an element greater than the pivot
            while i <= high and self.arr[i] <= pivot:
                i += 1
            # Move 'j' to the left until it finds an element less than or equal to the pivot
            while j >= low and self.arr[j] > pivot:
                j -= 1

            # If 'i' is still less than 'j', swap the elements at indices 'i' and 'j'
            if i < j:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        # Swap the pivot element with the element at index 'j'
        self.arr[low], self.arr[j] = self.arr[j], self.arr[low]
        # Return the index of the pivot element after partitioning
        return j

    def __quickSort(self, low: int, high: int) -> None:
        """
        Recursive function to perform quick sort.

        Parameters:
            low (int): Starting index of the subarray to be sorted.
            high (int): Ending index of the subarray to be sorted.
        """
        # Check if there are more than one element in the subarray
        if low < high:
            # Partition the array and get the index of the pivot element
            partition_index: int = self.__partition(low=low, high=high)
            # Recursively sort the left subarray (elements less than the pivot)
            self.__quickSort(low=low, high=partition_index - 1)
            # Recursively sort the right subarray (elements greater than the pivot)
            self.__quickSort(low=partition_index + 1, high=high)

    def sort_arr(self) -> None:
        """
        Utility function to start the quick sort process.
        """
        low: int = 0  # Starting index of the array.
        high: int = len(self.arr) - 1  # Ending index of the array.
        self.__quickSort(low=low, high=high)


if __name__ == "__main__":
    numbers: List[int] = [38, 9, 29, 7, 2, 15, 28]
    print("Before sort: ", numbers)
    # Sort the list
    qs: QuickSort = QuickSort(arr=numbers)
    qs.sort_arr()
    print("After sort: ", numbers)
