"""Accounts Merge using DSU."""


class DSU:
    def __init__(self, n: int) -> None:
        # Initialize the data structure with size and parent pointers.
        self.size: list[int] = [1] * (n)
        self.parent: list[int] = [0] * (n)
        for i in range(n):
            self.parent[i] = i

    def find_parent(self, node: int) -> int:
        # Find the parent of the node using path compression.
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u: int, v: int) -> None:
        # Union two nodes by size, ensuring the smaller tree is attached to the larger one.
        u_parent: int = self.find_parent(node=u)
        v_parent: int = self.find_parent(node=v)

        if u_parent == v_parent:
            return

        if self.size[u_parent] < self.size[v_parent]:
            self.parent[u_parent] = v_parent
            self.size[v_parent] += self.size[u_parent]
        elif self.size[u_parent] > self.size[v_parent]:
            self.parent[v_parent] = u_parent
            self.size[u_parent] += self.size[v_parent]
        else:
            self.parent[u_parent] = v_parent
            self.size[v_parent] += self.size[u_parent]


def merge_details(accounts: list[list[str]]) -> list[list[str]]:
    n: int = len(accounts)
    merged_mails: list[list[str]] = [[] for i in range(n)]
    map_mail_node: dict = dict()
    ds: DSU = DSU(n=n)

    # Traverse through accounts to build the DSU structure based on common emails.
    for i in range(n):
        for j in range(1, len(accounts[i])):
            mail: str = accounts[i][j]
            if mail not in map_mail_node:
                map_mail_node[mail] = i
            else:
                ds.union_by_size(i, map_mail_node[mail])

    # Map each mail to its corresponding parent node after merging.
    for mail, node in map_mail_node.items():
        parent: int = ds.find_parent(node=node)
        merged_mails[parent].append(mail)

    ans: list[list[str]] = []

    # Construct the final merged details list.
    for i in range(n):
        if len(merged_mails[i]) == 0:
            continue
        merged_mails[i].sort()
        temp: list[str] = [accounts[i][0]]
        temp += merged_mails[i]
        ans.append(temp)

    return ans


if __name__ == "__main__":
    accounts: list[list[str]] = [
        ["John", "j1@com", "j2@com", "j3@com"],
        ["John", "j4@com"],
        ["Raj", "r1@com", "r2@com"],
        ["John", "j1@com", "j5@com"],
        ["Raj", "r2@com", "r3@com"],
        ["Mary", "m1@com"],
    ]
    details: list[list[str]] = merge_details(accounts=accounts)
    print(details)
