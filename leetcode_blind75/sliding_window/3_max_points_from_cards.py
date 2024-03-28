"""
The goal is to find the maximum sum of points that can be obtained by selecting exactly k cards from either the beginning or end of the row of cards.

Approach:
- Initialize variables to keep track of the left sum, right sum, and the maximum sum obtained.
- Calculate the initial left sum by summing the first k elements of the cardPoints array.
- Initialize the right sum to 0.
- Iterate over the range from k - 1 to 0 (inclusive) to simulate selecting cards from the end of the row.
- In each iteration, update the left sum by subtracting the value of the card at the current index.
- Update the right sum by adding the value of the card at the corresponding index from the end of the array.
- Calculate the total sum of points by adding the left and right sums.
- Update the maximum sum obtained so far.
- Return the maximum sum.

Explanation:
- Initially, the left sum is calculated by summing the first k elements of the cardPoints array.
- Then, we iterate over the indices from k - 1 to 0 (inclusive) to simulate selecting cards from the end of the row.
- In each iteration, we update the left sum by subtracting the value of the card at the current index and update the right sum by adding the value of the card at the corresponding index from the end of the array.
- We calculate the total sum of points obtained by adding the left and right sums.
- We update the maximum sum obtained so far if the current sum is greater.
- Finally, we return the maximum sum.

Time Complexity Analysis:
- The algorithm has a time complexity of O(k), where k is the number of cards to select.
- This is because we iterate over the array twice, once to calculate the initial left sum and then again to update the left and right sums.
"""

from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Get the length of the cardPoints array
        n: int = len(cardPoints)
        # Initialize the left sum with the sum of the first k elements
        left_sum: int = sum(cardPoints[0:k])
        # Initialize the right sum with 0
        right_sum: int = 0
        # Initialize the maximum sum with the left sum
        max_sum: int = left_sum
        # Initialize the index for accessing elements from the right end of the array
        right_index: int = n - 1

        # Iterate over the indices from k - 1 to 0 (inclusive)
        for i in range(k - 1, -1, -1):
            # Update the left sum by subtracting the value of the card at the current index
            left_sum = left_sum - cardPoints[i]
            # Update the right sum by adding the value of the card at the corresponding index from the end of the array
            right_sum = right_sum + cardPoints[right_index]
            # Decrement the right index to move towards the beginning of the array
            right_index -= 1
            # Calculate the total sum of points by adding the left and right sums
            total_sum: int = left_sum + right_sum
            # Update the maximum sum obtained so far
            max_sum = max(max_sum, total_sum)

        # Return the maximum sum
        return max_sum


if __name__ == "__main__":
    # Test the maxScore function
    card_points: List[int] = [1, 2, 3, 4, 5, 6, 1]
    k: int = 3
    solution: Solution = Solution()
    print(solution.maxScore(cardPoints=card_points, k=k))
