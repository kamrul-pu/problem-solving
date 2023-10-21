import time
import threading


def calc_square(numbers: list[int]):
    print("calculate square numbers")

    for n in numbers:
        time.sleep(0.2)
        print("square:", n * n)


def calc_cube(numbers: list[int]):
    print("Calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("cube: ", n * n * n)


arr = [2, 3, 8, 9]
# Test using single thread
# t = time.time()
# calc_square(arr)

# calc_cube(arr)

# print("done in : ", time.time() - t)
# print("hah... I am done with all my work now!")

# Test using multi threading

t1 = time.time()

# Create thread to do some staffs
th1 = threading.Thread(target=calc_square, args=(arr,))
th2 = threading.Thread(target=calc_cube, args=(arr,))

# Start the thread
th1.start()
th2.start()

# Join the thread means wait until th1 is done. i mean calc_squarei
# if we do not join then it will execute last print statement before completing the calc functions
# By joining it is joining back to the main thread, after finishing threads
th1.join()
th2.join()


print("done in : ", time.time() - t1)
print("hah... I am done with all my work now!")
