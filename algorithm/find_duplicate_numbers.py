def find_duplicates(numbers: list[int]):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                print(numbers[i], "is a duplicate")
                break


def find_duplicates_optimized(numbers: list[int]):
    new_nums = set(numbers)
    print(len(numbers))
    print(len(new_nums))


numbers: list[int] = [3, 6, 2, 4, 3, 6, 8, 9]

find_duplicates(numbers=numbers)

find_duplicates_optimized(numbers=numbers)
