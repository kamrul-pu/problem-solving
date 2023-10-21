"""Multi threading. run two function in two thread."""
import time
import threading


def calc_square(numbers: list[int]):
    for number in numbers:
        time.sleep(0.2)
        print(f"square of {number} =", number * number)


def calc_cube(numbers: list[int]):
    for number in numbers:
        time.sleep(0.2)
        print(f"cube of {number} =", number * number * number)


# list of numbers
arr = [2, 3, 8, 9]
# get start time
t = time.time()
# Declare two thread
t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

# start thread
t1.start()
t2.start()

# Join the t1 and t2 thread to main thread
t1.join()
t1.join()

print("done in", time.time() - t)
print("Hah... I am done with all my work now")
