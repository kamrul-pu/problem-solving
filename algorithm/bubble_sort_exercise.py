"""
Bubble Sort Algorithm.
# Complexicity Space O(1)
# Complexicity Time O(n^2)
"""


def bubble_sort(elements, key: str):
    n = len(elements)
    count = 0
    for i in range(n - 1):
        swaped = False
        for j in range(n - i - 1):
            count += 1
            if elements[j][key] > elements[j + 1][key]:
                # Swap the elements.
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                swaped = True
        if not swaped:
            break

    print(count)


if __name__ == "__main__":
    elements = [
        {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
        {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
        {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
        {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
    ]
    # Sort the list
    bubble_sort(elements, "transaction_amount")
    print("after sort: ", elements)
