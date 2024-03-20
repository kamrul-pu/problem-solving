"""
Allocate Books among n students.
"""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr: list[int] = arr
        self.n = len(self.arr)

    def number_of_student(self, pages: int) -> int:
        student: int = 1
        pages_student: int = 0
        for i in range(self.n):
            if pages_student + self.arr[i] <= pages:
                pages_student += self.arr[i]
            else:
                student += 1
                pages_student = self.arr[i]

        return student

    def allocate_books(self, students: int) -> int:
        if students > self.n:
            return -1
        low: int = max(self.arr)
        high: int = sum(self.arr)
        for pages in range(low, high + 1):
            ct_student = self.number_of_student(pages)
            if ct_student == students:
                return pages

    def allocate_books_bs(self, students: int) -> int:
        if students > self.n:
            return -1
        low: int = max(self.arr)
        high: int = sum(self.arr)
        while low <= high:
            mid: int = (low + high) // 2
            ct_student = self.number_of_student(pages=mid)
            if ct_student > students:
                low = mid + 1
            else:
                high = mid - 1

        return low

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    arr = [25, 46, 28, 49, 24]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.allocate_books(4))
    print(solution.allocate_books_bs(4))
