from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encode a list of strings into a single delimited string
        if strs == [""] or strs == []:
            # If input list is empty or contains only an empty string, return it as is
            return strs

        # Join the list of strings into a single string delimited by ";"
        encoded: str = ";".join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        # Decode a delimited string back into a list of strings
        if s == []:
            # If input string is empty list, return an empty list
            return []
        if s == [""]:
            # If input string is a list containing an empty string, return a list with one empty string
            return [""]
        if s == "":
            # If input string is empty, return an empty list
            return []

        # Split the input string by ";" to extract individual strings
        decoded: List[str] = s.split(";")
        return decoded


if __name__ == "__main__":
    # Example usage:
    strs = ["neet", "code", "love", "you"]  # Input list of strings
    solution: Solution = Solution()

    # Encode the list of strings into a delimited string
    encoded: str = solution.encode(strs=strs)
    print(encoded)  # Output the encoded string

    # Decode the delimited string back into a list of strings
    decoded: List[str] = solution.decode(s=encoded)
    print(decoded)  # Output the decoded list of strings
