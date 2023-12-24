def dfs(
    node: int, adj_list: list[list[int]], visited: list[int], ans: list[int]
) -> None:
    visited[node] = node
    ans.append(node)
    for item in adj_list[node]:
        if not visited[item]:
            dfs(node=item, adj_list=adj_list, visited=visited, ans=ans)


def number_of_proviences(adj_list: list[int], n: int) -> int:
    visited: list[int] = [0 for _ in range(n + 1)]
    cnt: int = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(node=i, adj_list=adj_list, visited=visited, ans=ans)
            cnt += 1

    return cnt


if __name__ == "__main__":
    n: int = 8  # number of node
    adj_list = [
        [],
        [2],
        [1, 3],
        [2],
        [5],
        [4, 6],
        [5],
        [8],
        [7],
    ]
    print(adj_list)
    visited: list[int] = [0 for _ in range(n + 1)]
    ans: list[int] = []
    dfs(node=1, adj_list=adj_list, visited=visited, ans=ans)
    print(ans)
    print(number_of_proviences(adj_list=adj_list, n=n))
