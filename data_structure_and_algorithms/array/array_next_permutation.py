"""Rearrange array element by signed when positives != negetives."""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def next_permutation(self) -> None:
        ind: int = -1  # break point
        n: int = len(self.arr)  # Size of the array
        for i in range(n - 2, -1, -1):
            if self.arr[i] < self.arr[i + 1]:
                ind = i
                break
        # if i is still -1 then just reverse the element
        if ind == -1:
            # Reverse the whole array
            self.arr.reverse()
            return
        # step 2: find the next greater element
        #          and swap it with arr[ind]
        for i in range(n - 1, ind, -1):
            if self.arr[i] > self.arr[ind]:
                self.arr[i], self.arr[ind] = self.arr[ind], self.arr[i]
                break

        # Step 3: reverse the right half
        self.arr[ind + 1 :] = reversed(self.arr[ind + 1 :])

    def print_arr(self):
        print(self.arr)


if __name__ == "__main__":
    arr = [3, 2, 1]
    solution = Solution(arr)
    solution.print_arr()
    solution.next_permutation()
    solution.print_arr()
