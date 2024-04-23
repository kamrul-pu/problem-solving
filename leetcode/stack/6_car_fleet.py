"""
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the
ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed.
The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored
(i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.
"""

from typing import List, Tuple


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a list of tuples (position, speed) for each car
        pair: List[Tuple[int, int]] = [(p, s) for p, s in zip(position, speed)]

        # Initialize a stack to keep track of the time it takes for each car to reach the target
        stack: List[int] = []

        # Sort the cars by their starting position in descending order (farthest car first)
        for p, s in sorted(pair)[::-1]:
            # Calculate the time needed for the current car to reach the target
            time_to_reach_target: float = (target - p) / s

            # Add the calculated time to the stack
            stack.append(time_to_reach_target)

            # If there are at least two cars in the stack and the latest car takes longer or equal time to reach than the previous one,
            # it means this car will form a fleet with the previous car
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # Remove the previous car's time (merge into a fleet)

        # The length of the stack will represent the number of car fleets that will arrive at the destination
        return len(stack)


if __name__ == "__main__":
    target: int = 12
    position: List[int] = [10, 8, 0, 5, 3]
    speed: List[int] = [2, 4, 1, 1, 3]
    solution: Solution = Solution()
    print(solution.carFleet(target=target, position=position, speed=speed))
