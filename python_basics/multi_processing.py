"""Multi processing in python."""

import time
import multiprocessing

square_result = []


def calc_square(numbers: list[int]):
    global square_result
    for number in numbers:
        time.sleep(0.2)
        print(f"square of {number} =", number * number)
        square_result.append(number * number)

    print("result within square function", square_result)


def calc_cube(numbers: list[int]):
    for number in numbers:
        time.sleep(0.2)
        print(f"cube of {number} =", number * number * number)


if __name__ == "__main__":
    arr = [2, 4, 5, 8, 9]
    # Declare process
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))
    # start the process
    p1.start()
    p2.start()
    # Join the two process, two the main process otherwise print will print first
    p1.join()
    p2.join()
    # main process will wait for p1 and p2
    print("result", square_result)
    print("Done!!!")
