"""Power Exponentiation."""


class Solution:
    def __f(self, n: int, p: int) -> int:
        ans: int = 1
        while p:
            ans *= n
            p -= 1
        return ans

    def __power(self, n: int, p: int) -> int:
        """
        Calculate the power of a number using an optimized approach.

        Args:
            n (int): The base number.
            p (int): The exponent.

        Returns:
            int: The result of the power operation (n^p).
        """
        ans: int = 1
        while p > 0:
            if p % 2 == 1:
                # If the exponent is odd, multiply ans by n, and reduce power by one
                ans *= n
                p -= 1
            else:
                # If the exponent is even, square n and halve p
                n *= n
                p //= 2
        return ans

    def power(self, num: int, p: int) -> int:
        # return self.__f(n=num, p=p)
        return self.__power(n=num, p=p)


if __name__ == "__main__":
    num: int = 2
    p: int = 21
    solution: Solution = Solution()
    print(solution.power(num=num, p=p))
