"""Multi processing in python."""

import time
import multiprocessing


def calc_square(numbers: list[int], q):
    for number in numbers:
        time.sleep(0.2)
        q.put(number * number)


if __name__ == "__main__":
    arr = [2, 4, 5, 8, 9]
    # Make a queue for share data using array
    q = multiprocessing.Queue()
    # Declare process
    p = multiprocessing.Process(
        target=calc_square,
        args=(arr, q),
    )
    # start the process
    p.start()
    # Join the two process, two the main process otherwise print will print first
    p.join()
    while q.empty() is False:
        print(q.get())

    print("Done!!!")
