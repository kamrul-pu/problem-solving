"""Lock in multi processing."""

import time
import multiprocessing


def deposit(balance, lock):
    for i in range(100):
        # lock the balance varibale
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        # release the lock
        lock.release()


def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        # release the lock
        lock.release()


if __name__ == "__main__":
    # Declare initial balance value
    balance = multiprocessing.Value("i", 200)
    # create a lock
    lock = multiprocessing.Lock()
    # Declare two process deposit and withdraw
    d = multiprocessing.Process(target=deposit, args=(balance, lock))
    w = multiprocessing.Process(target=withdraw, args=(balance, lock))

    # Start two process
    d.start()
    w.start()
    # Join the two process to main process
    d.join()
    w.join()

    print("final Balance:", balance.value)
