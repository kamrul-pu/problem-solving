"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element
accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there
is some common email to both accounts. Note that even if two accounts have the same name, they may belong
to different people as people could have the same name. A person can have any number of accounts initially,
but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is
the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
"""

from typing import List, Dict


class DSU:
    def __init__(self, node: int) -> None:
        # Initialize DSU with parent array and size array
        self.parent: List[int] = [i for i in range(node + 1)]  # Initialize parent array
        self.__size: List[int] = [1] * (node + 1)  # Initialize size array

    def find_parent(self, node: int) -> int:
        # Find the parent of the set containing 'node' (with path compression)
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find_parent(node=self.parent[node])  # Path Compression
        return self.parent[node]

    def union(self, u: int, v: int) -> None:
        # Union operation to merge two sets
        u_parent: int = self.find_parent(node=u)
        v_parent: int = self.find_parent(node=v)
        if u_parent == v_parent:
            return None
        if self.__size[u_parent] < self.__size[v_parent]:
            self.parent[u_parent] = v_parent
            self.__size[v_parent] += self.__size[u_parent]
        elif self.__size[u_parent] > self.__size[v_parent]:
            self.parent[v_parent] = u_parent
            self.__size[u_parent] += self.__size[v_parent]
        else:
            self.parent[u_parent] = v_parent
            self.__size[v_parent] += self.__size[u_parent]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n: int = len(accounts)
        ds: DSU = DSU(node=n)
        mail_node: Dict = dict()  # Mapping of emails to their corresponding node index
        # Iterate over each account
        for i in range(n):
            # Iterate over emails in the account starting from the second element
            for j in range(1, len(accounts[i])):
                mail: str = accounts[i][j]
                if mail in mail_node:
                    # If the email is already present in mail_node, union the nodes
                    ds.union(u=i, v=mail_node[mail])
                else:
                    # Otherwise, create a new entry in mail_node
                    mail_node[mail] = i
        merged_mail: List[List[str]] = [
            [] for _ in range(n)
        ]  # List to store merged emails
        # Iterate over mail_node to group emails based on their parent node
        for mail, node in mail_node.items():
            parent: int = ds.find_parent(node=node)
            merged_mail[parent].append(mail)
        ans: List[List[str]] = []  # Final merged accounts
        # Iterate over merged_mail to construct the final answer
        for i in range(n):
            if len(merged_mail[i]) == 0:
                continue
            merged_mail[i].sort()  # Sort emails in alphabetical order
            temp: List[str] = [accounts[i][0]]  # First element is the name
            temp += merged_mail[i]  # Append sorted emails
            ans.append(temp)  # Append the account to the final answer
        return ans


if __name__ == "__main__":
    accounts: List[List[str]] = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    solution: Solution = Solution()
    print(solution.accountsMerge(accounts=accounts))
