"""Number of 1 bits."""


class Solution:
    # Function to count the number of '1' bits in the binary representation of the input integer
    def hammingWeight(self, n: int) -> int:
        ans: int = 0  # Initialize the count of '1' bits to 0
        while n:  # Continue the loop until n becomes 0
            ans += n & 1  # Increment the count if the least significant bit of n is '1'
            n >>= 1  # Right shift n by 1 bit to check the next bit
        return ans  # Return the total count of '1' bits


# Main function to test the hammingWeight function
if __name__ == "__main__":
    n: int = 11  # Example input integer
    solution: Solution = Solution()  # Create an instance of the Solution class
    print(
        solution.hammingWeight(n=n)
    )  # Print the count of '1' bits in the binary representation of n
