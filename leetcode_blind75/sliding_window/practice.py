class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls = s.strip(" ").split(" ")
        print(ls)
        return len(ls[-1])


if __name__ == "__main__":
    s: str = "   fly me   to   the moon  "
    solution: Solution = Solution()
    print(solution.lengthOfLastWord(s=s))
