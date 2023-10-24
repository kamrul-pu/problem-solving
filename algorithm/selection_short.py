"""Selecttion SHort in python."""


def selection_short(elements: list):
    for i in range(len(elements)):
        min_index = i
        for j in range(i + 1, len(elements)):
            if elements[j] < elements[min_index]:
                min_index = j

        elements[i], elements[min_index] = elements[min_index], elements[i]


if __name__ == "__main__":
    numbers = [38, 9, 29, 7, 2, 15, 28]
    # numbers = list(range(10, 0, -1))
    selection_short(numbers)
    print(numbers)
