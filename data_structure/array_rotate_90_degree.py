"""Rotate array elements in 90 degree."""

class Solution:
    def __init__(self, arr: list[list[int]]) -> None:
        self.arr = arr

    def rotate_array_brute_force(self)->list[list[int]]:
        n = len(self.arr) # get the length of n*n matrix
        # create a 2d array filled with zero
        ans = [[0 for col in range(n)] for row in range(n)]
        for row in range(n):
            for col in range(n):
                ans[col][n-row-1] = self.arr[row][col]
        return ans

    def rotate_array_optimal(self)->None:
        # modify the original array
        # Step 1  make the transpose of the matrix row = col, col=row
        n = len(self.arr)
        for i in range(n-1):
            for j in range(i+1, n):
                self.arr[i][j],self.arr[j][i] = self.arr[j][i],self.arr[i][j]
        # Now reverse every row
        for row in range(n):
            # self.arr[row] = list(reversed(self.arr[row]))
            # self.arr[row] = self.arr[row][::-1]
            self.arr[row].reverse()

    def print_arr(self):
        n = len(self.arr)
        for row in range(n):
            print(self.arr[row], sep=" ", end="\n")
        print()


if __name__ == "__main__":
    arr = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16],
    ]
    solution = Solution(arr)
    solution.print_arr()
    arr = solution.rotate_array_brute_force()
    solution.rotate_array_optimal()
    solution.print_arr()
