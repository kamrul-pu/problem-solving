"""
You are playing a game with integers. You start with the integer 1 and you want to reach the integer target.

In one move, you can either:

Increment the current integer by one (i.e., x = x + 1).
Double the current integer (i.e., x = 2 * x).
You can use the increment operation any number of times, however, you can only use the double operation at most maxDoubles times.

Given the two integers target and maxDoubles, return the minimum number of moves needed to reach target starting with 1.
"""


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        c: int = 0  # Initialize the count of moves to zero

        # Continue until we have maxDoubles left or target is reduced to 1
        while maxDoubles and target > 1:
            # If the target is even and we still have doubles left
            if target % 2 == 0:
                maxDoubles -= 1  # Use up one of the allowed double operations
                target //= (
                    2  # Double the current integer, which means we halve the target
                )
            else:
                # If the target is odd, we need to decrement the target by 1
                target -= 1  # Perform increment operation (in this case, decrement to make it even)
            c += 1  # Increment move count for the decrement operation

        # After exhausting double operations or reducing target to 1, we might still need to decrement
        # the target to 1 using only increments
        if target > 1:
            # Add the remaining increments needed to reach 1 from the target
            c += target - 1

        return c  # Return the total number of moves required


# Example usage
if __name__ == "__main__":
    target: int = 19  # Example target value
    maxDoubles: int = 2  # Example maximum number of doubles allowed
    solution: Solution = Solution()
    print(
        solution.minMoves(target, maxDoubles)
    )  # Output the result of the minMoves function
