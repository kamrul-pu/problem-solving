"""Insertion SOrt.
Space complexity O(1)
Time Complexity O(n^2) worst.
Best case O(n)
"""


def insertion_sort(elements: list):
    count = 0
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            count += 1
            j -= 1

        elements[j + 1] = anchor

    print(count)


if __name__ == "__main__":
    numbers = [38, 9, 29, 7, 2, 15, 28]
    # numbers = [2, 7, 9, 15, 28, 29, 38]
    # numbers = list(range(1, 1000))
    # Sort the list
    insertion_sort(numbers)
    print("after sort: ", numbers)
