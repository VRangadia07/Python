#  run code in parallel using the Python multiprocessing module.
# Multiprocessing allows two or more processors to simultaneously process two or more different parts of a program.


# multiprocessing module to implement multiprocessing.

import time
import multiprocessing

def task() -> int:
    result = 0
    for _ in range(10**8):
        result += 1
    return result

if __name__ == '__main__':
    start = time.perf_counter()

    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()
    print(f'It took {finish-start:.2f} second(s) to finish')
    


# Process() constructor returns a new Process object.
# call the start() method of the Process objects to start the process.
#  wait for the processes to complete by calling the join() method.



# ProcessPoolExecutor
# manage the processes more efficiently, you can use a process pool
#  a process pool is a pattern for managing processes automatically.
# ProcessPoolExecutor class from the concurrent.futures module allows you to create and manage a process pool.
# submit() – dispatch a function to be executed by the process and return a Future object.
#  map() – call a function to an iterable of elements.

import concurrent.futures
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = [114587963, 25478582705942171, 325280095190773, 425397848077099]

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(is_prime, numbers)

for number, result in zip(numbers, results):
    print(f"{number} is prime: {result}")




# The is_prime function checks if a number is prime.

# A list of large numbers is provided.

# ProcessPoolExecutor is used to apply the is_prime function to each number in parallel.

# The map method blocks until all results are available and returns them in the same order as the input.
# zip() function takes two or more iterables and returns an iterator of tuples.