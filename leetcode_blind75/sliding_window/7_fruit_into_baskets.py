"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer
array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right.
The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

"""

from collections import defaultdict
from typing import DefaultDict, List, Set


class Solution:
    def __brute(self, fruits: List[int]) -> int:
        # Initialize the maximum length variable
        max_len = 0
        # Get the length of the fruits list
        n: int = len(fruits)
        # Iterate over each tree as a potential starting point
        for i in range(n):
            # Initialize a set to store the types of fruits encountered
            st: Set = set()
            # Iterate over the fruits starting from the current tree
            for j in range(i, n):
                # Add the fruit type to the set
                st.add(fruits[j])
                # If the set contains two or fewer types of fruits, update the maximum length
                if len(st) <= 2:
                    max_len = max(max_len, j - i + 1)
                # If more than two types of fruits are encountered, break out of the loop
                else:
                    break
        return max_len

    def __better(self, fruits: List[int]) -> int:
        # Initialize variables
        n: int = len(fruits)
        max_len = l = r = 0
        mp: DefaultDict = defaultdict(int)
        # Iterate over the fruit trees
        while r < n:
            # Add the current fruit to the frequency map
            mp[fruits[r]] += 1
            # If there are more than two types of fruits in the map
            if len(mp) > 2:
                # Adjust the left pointer until there are only two types of fruits in the map
                while len(mp) > 2:
                    # Decrease the count of the fruit type at the left pointer
                    mp[fruits[l]] -= 1
                    # If the count becomes 0, remove the fruit type from the map
                    if mp[fruits[l]] == 0:
                        mp.pop(fruits[l])
                    # Move the left pointer to the right
                    l += 1
            # Update the maximum length
            max_len = max(max_len, r - l + 1)
            # Move the right pointer to the right
            r += 1
        return max_len

    def __optimal(self, fruits: List[int]) -> int:
        # Initialize variables
        n: int = len(fruits)
        max_len = l = r = 0
        mp: DefaultDict = defaultdict(int)
        # Iterate over the fruit trees
        while r < n:
            # Add the current fruit to the frequency map
            mp[fruits[r]] += 1
            # If there are more than two types of fruits in the map
            if len(mp) > 2:
                # Decrease the count of the fruit type at the left pointer
                mp[fruits[l]] -= 1
                # If the count becomes 0, remove the fruit type from the map
                if mp[fruits[l]] == 0:
                    mp.pop(fruits[l])
                # Move the left pointer to the right
                l += 1
            # Update the maximum length
            max_len = max(max_len, r - l + 1)
            # Move the right pointer to the right
            r += 1
        return max_len

    def totalFruit(self, fruits: List[int]) -> int:
        # return self.__brute(fruits=fruits)
        # return self.__better(fruits=fruits)
        return self.__optimal(fruits=fruits)


if __name__ == "__main__":
    fruits: List[int] = [1, 2, 3, 2, 2]
    solution: Solution = Solution()
    print(solution.totalFruit(fruits=fruits))
