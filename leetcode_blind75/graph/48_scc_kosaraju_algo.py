"""
Strongly connected component using Kosaraju's algorithm (only in directed graph).
Step 1: Perform a Depth-First Search (DFS) in the forward pass: Start a DFS from each unvisited vertex,
traversing the graph in a depth-first manner. Maintain a stack to keep track of the order in which
vertices are visited.
Step 2: Reverse the graph: Reverse the direction of all edges in the graph, creating a new graph.
Step 3: Perform a Depth-First Search (DFS) in the backward pass: Pop vertices from the stack obtained in
the forward pass and start a DFS from each unvisited vertex in the reversed graph. The SCCs are identified
during this pass.
Step 4: Output the SCCs: Each completed DFS traversal in the backward pass represents an SCC. Collect the
vertices visited in each traversal and output them as separate SCCs.
"""

from typing import List


class Solution:
    def __dfs(
        self, node: int, adj_list: List[List[int]], visited: List[bool], st: List[int]
    ) -> None:
        # Depth First Search (DFS) function
        # Marks the current node as visited
        visited[node] = True
        # Explore all neighbors of the current node
        for neighbor in adj_list[node]:
            # If neighbor is not visited, recursively call DFS on it
            if not visited[neighbor]:
                self.__dfs(neighbor, adj_list, visited, st)
        # After exploring all neighbors, push the current node onto the stack
        st.append(node)

    def __kosaraju(self, v: int, adj_list: List[List[int]]) -> int:
        # Kosaraju's algorithm function
        visited: List[bool] = [False] * v  # Mark all vertices as not visited
        st: List[int] = []  # Stack to keep track of the order of visited vertices

        # Step 1: Perform DFS in the forward pass
        # Start DFS from each unvisited vertex
        for node in range(v):
            if not visited[node]:
                self.__dfs(node=node, adj_list=adj_list, visited=visited, st=st)

        # Step 2: Reverse the graph
        # Create a new graph with reversed edges
        adj_list_rev: List[List[int]] = [[] for _ in range(v)]
        for node in range(v):
            visited[node] = False  # Reset visited array
            # Reverse the edges of the original graph
            for neighbor in adj_list[node]:
                adj_list_rev[neighbor].append(node)

        ans: List[List[int]] = []  # List to store Strongly Connected Components (SCCs)
        total_scc: int = 0  # Total number of SCCs

        # Step 3: Perform DFS in the backward pass
        # Pop vertices from the stack obtained in the forward pass
        while st:
            node: int = st.pop()
            scc_list: List[int] = []  # List to store vertices of current SCC
            if not visited[node]:
                total_scc += 1  # Increment the count of SCCs
                # Start DFS from each unvisited vertex in the reversed graph
                self.__dfs(
                    node=node, adj_list=adj_list_rev, visited=visited, st=scc_list
                )
                ans.append(scc_list)  # Add vertices of SCC to the list of SCCs

        print(ans)  # Print the list of SCCs
        return total_scc  # Return the total number of SCCs

    def scc(self, adj_list: List[List[int]]) -> int:
        v: int = len(adj_list)  # Number of vertices in the graph
        return self.__kosaraju(v=v, adj_list=adj_list)  # Call Kosaraju's algorithm


if __name__ == "__main__":
    # Example adjacency list representing the graph
    adj_list: List[List[int]] = [[1], [2], [0, 3], [4], [5, 7], [6], [4, 7], []]
    solution: Solution = Solution()
    scc: int = solution.scc(adj_list=adj_list)  # Find SCCs using Kosaraju's algorithm
    print(scc)  # Print the total number of SCCs
