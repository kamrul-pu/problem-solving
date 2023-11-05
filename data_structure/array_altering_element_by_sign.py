"""Rearrange array element by signed when positives == negetives."""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def rearrnage_array1(self) -> None:
        """TC = O(2n) Space O(n)"""
        # Store the positve and negetive value to separate array
        positives = []
        negetives = []
        for x in self.arr:
            if x < 0:
                negetives.append(x)
            else:
                positives.append(x)

        # Copy back to the original array
        for i in range(len(self.arr) // 2):
            self.arr[2 * i] = positives[i]  # store positives in positive index 0, 2, 4
            self.arr[2 * i + 1] = negetives[i]  # negetives in negetive index 1, 3, 5

    def rearrange_array2(self):
        """TC O(n) Space O(n)"""
        temp: list[int] = [0] * len(self.arr)
        positive_index = 0
        negetive_index = 1
        for x in self.arr:
            if x > 0:
                temp[positive_index] = x
                positive_index += 2
            else:
                temp[negetive_index] = x
                negetive_index += 2

        self.arr = temp

    def print_arr(self):
        print(self.arr)


if __name__ == "__main__":
    arr = [3, 1, -2, -5, 2, -4]
    solution = Solution(arr)
    solution.print_arr()
    solution.rearrange_array2()
    solution.print_arr()
