"""Leaders mean the all right most element should be smaller."""


class Solution:
    def longest_consequtive_seqence(self, arr: list[int]) -> int:
        # sort the array
        n: int = len(arr)
        arr.sort()
        longest: int = 1
        last_smaller: int = -12435436
        count: int = 0
        for i in range(n):
            if arr[i] - 1 == last_smaller:
                count += 1
                last_smaller = arr[i]
            elif arr[i] != last_smaller:
                count = 1
                last_smaller = arr[i]
            longest = max(longest, count)

        return longest

    def longest_consequtive_sequence1(self, arr: list[int]) -> int:
        n: int = len(arr)
        if n == 0:
            return 0
        longest: int = 1
        # insert the unique element in the set
        st = set(arr)
        for val in st:
            # if current - 1 not in the set then it is the start point
            if val - 1 not in st:
                x: int = val
                ct: int = 1
                while (x + 1) in st:
                    x += 1
                    ct += 1

                longest = max(longest, ct)

        return longest

    def print_arr(self, arr) -> None:
        print(arr)


if __name__ == "__main__":
    arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
    solution = Solution()
    solution.print_arr(arr)
    print(solution.longest_consequtive_seqence(arr))
    print(solution.longest_consequtive_sequence1(arr))
