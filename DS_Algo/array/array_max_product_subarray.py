""" Maximum product of a subarray."""


class Solution:
    def __init__(self, arr: list[int] = []) -> None:
        self.arr = arr
        self.INT_MIN = -123456789

    def max_subarray_product(self) -> int:
        cnt: int = 0
        max_product = self.INT_MIN
        n = len(self.arr)
        for i in range(n):
            product: int = 1
            for j in range(i, n):
                product *= self.arr[j]
                max_product = max(max_product, product)
                cnt += 1
        print(f"loop rans: {cnt} times")
        return max_product

    def max_subarray_product_optimal(self) -> int:
        max_product = self.INT_MIN
        n = len(self.arr)
        prefix: int = 1
        suffix: int = 1
        for i in range(n):
            prefix *= self.arr[i]
            suffix *= self.arr[n - i - 1]
            max_product = max(max_product, prefix, suffix)
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

        return max_product

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    arr = [2, 3, -2, 4]
    soltuion = Solution(arr)
    soltuion.print_arr()
    print(soltuion.max_subarray_product())
    print(soltuion.max_subarray_product_optimal())
