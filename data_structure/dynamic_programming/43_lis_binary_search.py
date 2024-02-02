from typing import List


# Function to find the lower bound using binary search
def lower_bound(arr: List[int], n: int, target: int) -> int:
    ans = n
    low: int = 0
    high: int = n - 1

    # Binary search to find the lower bound index
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


# Function to find the Longest Increasing Subsequence using binary search
def lis_using_binary_search(arr: List[int], n: int) -> int:
    temp: List[int] = [arr[0]]

    # Iterate through the array to build the LIS
    for i in range(1, n):
        if arr[i] > temp[-1]:
            temp.append(arr[i])
        else:
            # Find the lower bound index and replace the element
            ind: int = lower_bound(temp, len(temp), arr[i])
            temp[ind] = arr[i]

    return len(temp)


# Function to get the Longest Increasing Subsequence of an array
def get_lis(arr: List[int]) -> int:
    n: int = len(arr)
    return lis_using_binary_search(arr, n)


# Example usage
if __name__ == "__main__":
    arr: List[int] = [1, 7, 8, 4, 5, 6, -1, 9]
    print(get_lis(arr))
