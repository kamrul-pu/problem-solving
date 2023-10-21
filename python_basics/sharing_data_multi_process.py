"""Sharring data within multiprocessing."""

import multiprocessing


def calc_square(numbers: list[int], result, v):
    v.value = 5.67
    for idx, number in enumerate(numbers):
        print(f"square of {number} =", number * number)
        result[idx] = number * number

    print("result within square function", result[:])


if __name__ == "__main__":
    arr = [2, 4, 5, 8, 9]
    # Share result in main and cal_square process
    result = multiprocessing.Array("i", len(arr))  # i meand integer d means double
    # Share value its a single value
    v = multiprocessing.Value("d", 0.0)
    # Declare process
    p1 = multiprocessing.Process(target=calc_square, args=(arr, result, v))
    # start the process
    p1.start()
    # Join the two process, two the main process otherwise print will print first
    p1.join()
    # main process will wait for p1 and p2
    print("outside process result", result[:])
    print("Value: ", v.value)
    print("Done!!!")
