"""Valid parentheses."""


class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        parenthesis = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                st.append(ch)
            else:
                if len(st) == 0:
                    return False
                top = st.pop()
                if top != parenthesis[ch]:
                    return False

        return len(st) == 0


if __name__ == "__main__":
    s: str = "()[]{}"
    solution: Solution = Solution()
    print(solution.isValid(s=s))
