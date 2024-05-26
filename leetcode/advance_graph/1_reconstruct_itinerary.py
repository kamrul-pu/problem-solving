"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure
and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK".
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical
order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
"""

from typing import DefaultDict, List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create an adjacency list to store destinations for each source airport
        adj_list: DefaultDict[str, List[str]] = defaultdict(list)

        # Sort the tickets in reverse order to pop from the end for efficiency
        tickets.sort(reverse=True)

        # Populate the adjacency list
        for src, dst in tickets:
            adj_list[src].append(dst)

        # Initialize an empty list to store the itinerary
        result: List[str] = []

        # Depth-first search (DFS) function to construct the itinerary
        def dfs(node: str) -> None:
            # While there are destinations available from the current airport
            while adj_list[node]:
                # Recursively call DFS on the next destination
                dfs(adj_list[node].pop())
            # Add the current airport to the itinerary
            result.append(node)

        # Start DFS from the initial airport "JFK"
        dfs("JFK")

        # Reverse the result because we appended in reverse order during DFS
        return result[::-1]


if __name__ == "__main__":
    # Example usage
    tickets: List[List[str]] = [
        ["JFK", "SFO"],
        ["JFK", "ATL"],
        ["SFO", "ATL"],
        ["ATL", "JFK"],
        ["ATL", "SFO"],
    ]
    solution: Solution = Solution()
    result: List[str] = solution.findItinerary(tickets=tickets)
    print(result)
