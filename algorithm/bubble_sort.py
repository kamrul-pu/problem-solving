"""
Bubble Sort Algorithm.
# Complexicity Space O(1)
# Complexicity Time O(n^2)
"""


def bubble_sort(numbers: list[int]):
    n = len(numbers)
    count = 0
    for i in range(n - 1):
        swaped = False
        for j in range(n - i - 1):
            count += 1
            if numbers[j] > numbers[j + 1]:
                # Swap the numbers.
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swaped = True
        if not swaped:
            break

    print(count)


if __name__ == "__main__":
    numbers = [38, 9, 29, 7, 2, 15, 28]
    # numbers = [2, 7, 9, 15, 28, 29, 38]
    # numbers = range(1, 1000000)
    # Sort the list
    bubble_sort(numbers)
    print("after sort: ", numbers)
