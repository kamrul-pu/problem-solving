"""
pattern
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
"""


class Solution:
    def print_pattern(self, n: int) -> None:
        # Calculate the value of 2n
        _2n: int = n * 2

        # Iterate over the rows
        for i in range(_2n - 1):
            # Iterate over the columns
            for j in range(_2n - 1):
                # Calculate the distance to the nearest boundary in each direction
                top: int = i
                left: int = j
                right: int = _2n - 2 - j
                bottom: int = _2n - 2 - i

                # Determine the minimum distance to the nearest boundary
                distance: int = n - min(top, left, right, bottom)

                # Print the distance value with a space separator
                print(distance, end=" ")

            # Move to the next line after printing each row
            print()


if __name__ == "__main__":
    n: int = 4
    solution: Solution = Solution()
    solution.print_pattern(n=n)
