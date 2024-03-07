"""Longest common prefix."""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans: str = ""
        strs.sort()
        first: str = strs[0]
        last: str = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]

        return ans


if __name__ == "__main__":
    strs: List[str] = ["flower", "flow", "flight"]
    solution: Solution = Solution()
    print(solution.longestCommonPrefix(strs=strs))
