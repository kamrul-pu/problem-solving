"""Pascal Triangle problem."""


class Solution:
    def find_nCr(self, n: int, r: int):
        ans: int = 1
        for i in range(r):
            ans *= n - i
            ans //= i + 1
        return ans

    def find_pascal_value_at(self, row: int, col: int):
        return self.find_nCr(row - 1, col - 1)

    def find_pascal_row(self, row: int) -> None:
        for c in range(1, row + 1):
            print(self.find_nCr(row - 1, c - 1), end=" ")
        print()

    def find_pascal_row_1(self, row: int) -> None:
        ans: int = 1
        print(ans, end=" ")
        for i in range(1, row):
            ans *= row - i
            ans //= i
            print(ans, end=" ")
        print()

    def print_pascal_triangle(self, n: int) -> None:
        for i in range(1, n + 1):
            self.find_pascal_row_1(i)


if __name__ == "__main__":
    solution = Solution()
    print(solution.find_nCr(4, 2))
    print(solution.find_pascal_value_at(5, 3))
    solution.find_pascal_row(6)
    solution.find_pascal_row_1(6)
    solution.print_pascal_triangle(6)
