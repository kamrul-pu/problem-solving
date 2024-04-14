class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        count = 0
        while i < 32:
            count += (n >> i) & 1
            i += 1
        return count

    def hammingWeight2(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n - 1)
            res += 1

        return res

    def hammingWeight3(self, n: int) -> int:
        # most optimized solution
        # Initialize with count zero
        count = 0
        # run the loop till n not 0
        while n:
            # bitwise and operation with n and 1
            count += n & 1
            # right shift the number to one position
            n >>= 1

        # return the number of set bit in the number
        return count


if __name__ == "__main__":
    solution = Solution()
    n = 11
    print(solution.hammingWeight3(n))
