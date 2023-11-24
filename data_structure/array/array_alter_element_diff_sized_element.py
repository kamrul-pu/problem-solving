"""Rearrange array element by signed when positives != negetives."""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def rearrnage_array(self) -> None:
        """TC = O(2n) Space O(n)"""
        # Store the positve and negetive value to separate array
        positives = []
        negetives = []
        for x in self.arr:
            if x < 0:
                negetives.append(x)
            else:
                positives.append(x)

        if len(positives) > len(negetives):
            for i in range(len(negetives)):
                self.arr[2 * i] = positives[i]
                self.arr[2 * i + 1] = negetives[i]

            # copy back the existing element
            index = len(negetives) * 2
            for i in range(len(negetives), len(positives)):
                self.arr[index] = positives[i]
                index += 1
        else:
            for i in range(len(positives)):
                self.arr[2 * i] = positives[i]
                self.arr[2 * i + 1] = negetives[i]

            # copy remaining elements
            index = len(positives) * 2
            for i in range(len(positives), len(negetives)):
                self.arr[index] = negetives[i]
                index += 1

    def print_arr(self):
        print(self.arr)


if __name__ == "__main__":
    arr = [-1, 2, 3, 4, -3, 1]
    arr1 = arr.copy()
    solution = Solution(arr)
    solution.print_arr()
    solution.rearrnage_array()
    solution.print_arr()
    # alter all elementes
    arr1 = [x * -1 for x in arr1]
    solution1 = Solution(arr1)
    solution1.print_arr()
    solution1.rearrnage_array()
    solution1.print_arr()
