"""
Design a time-based key-value data structure that can store multiple values for the
same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
"""

from typing import List, Dict


class TimeMap:

    def __init__(self):
        # Initialize a dictionary to store key-value pairs with associated timestamps
        self.t_map: Dict[str, List[List[str, int]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Store the key-value pair along with the timestamp in the dictionary
        if key not in self.t_map:
            self.t_map[key] = []  # Create an empty list for the key if it doesn't exist
        self.t_map[key].append(
            [value, timestamp]
        )  # Append [value, timestamp] to the list

    def get(self, key: str, timestamp: int) -> str:
        res = ""  # Initialize result to an empty string
        values = self.t_map.get(
            key, []
        )  # Get the list of [value, timestamp] pairs for the given key

        # Binary search to find the largest timestamp_prev <= timestamp
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2

            if values[mid][1] <= timestamp:
                # If current value's timestamp is <= the desired timestamp, update the result and search to the right
                res = values[mid][0]
                l = mid + 1
            else:
                # If current value's timestamp is > the desired timestamp, search to the left
                r = mid - 1

        return res  # Return the result (value associated with the largest timestamp_prev <= timestamp)


if __name__ == "__main__":
    time_map: TimeMap = TimeMap()
    time_map.set("foo", "bar", 1)
    print(time_map.get("foo", 1))  # Output: "bar" (value associated with timestamp 1)
    print(
        time_map.get("foo", 3)
    )  # Output: "bar" (value associated with the largest timestamp_prev <= 3)
    time_map.set("foo", "bar2", 4)
    print(time_map.get("foo", 4))  # Output: "bar2" (value associated with timestamp 4)
    print(
        time_map.get("foo", 5)
    )  # Output: "bar2" (value associated with the largest timestamp_prev <= 5)
