# in mt is allow to run mytitask in same time at same process .
# Multithreading allows a program to perform multiple tasks at the same time within a single process. Each task is handled by a separate thread, 
# which is like a mini-program running inside your main program.
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, 5, self.counter)
      print ("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
print ("Exiting Main Thread")

from time import sleep, perf_counter
from threading import Thread


def task():
    print('Starting a task...')
    sleep(1)
    print('done')


start_time = perf_counter()

# create two new threads
t1 = Thread(target=task)
t2 = Thread(target=task)

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

# When the program executes, it’ll have three threads: the main thread and two other child threads.



# ThreadPoolExecutor
# A thread pool is a pattern for managing multiple threads efficiently.
#  manually managing threads is not efficient because creating and destroying many threads frequently
# are very expensive in terms of computational costs.
# A thread pool is a pattern for achieving concurrency of execution in a program. A thread pool 
# allows you to automatically manage a pool of threads efficiently
# The ThreadPoolExecutor class extends the Executor class and returns a Future object.

from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor

def task(id):
    print(f'Starting the task {id}...')
    sleep(1)
    return f'Done with task {id}'

start = perf_counter()

with ThreadPoolExecutor() as executor:
    f1 = executor.submit(task, 1)
    f2 = executor.submit(task, 2)

    print(f1.result())
    print(f2.result())    

finish = perf_counter()

print(f"It took {finish-start} second(s) to finish.")

# submit() – dispatch a function to be executed and return a Future object. The submit() method 
# takes a function and executes it asynchronously.
# we have two Future objects f1 and f2. To get the result from the Future object, we called its result() method.


# map() method
# execute a function asynchronously for each element in an iterable.
from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor


def task(id):
    print(f'Starting the task {id}...')
    sleep(1)
    return f'Done with task {id}'

start = perf_counter()

with ThreadPoolExecutor() as executor:
    results = executor.map(task, [1,2])
    for result in results:
        print(result)

finish = perf_counter()

print(f"It took {finish-start} second(s) to finish.")

# First, call the map() method of the executor object to run the 
# task function for each id in the list [1,2]. The map() method re
# turns an iterator that contains the result of the function calls.
# iterate over the results and print them out



from concurrent.futures import ThreadPoolExecutor
from time import sleep

def calculate_square(number):
    sleep(1)
    return number ** 2

def calculate_cube(number):
    sleep(1)
    return number ** 3

def main():
    numbers = [1, 2, 3, 4, 5]
    with ThreadPoolExecutor(max_workers=3) as executor:
        squares = executor.map(calculate_square, numbers)
        cubes = executor.map(calculate_cube, numbers)
    
    print("Squares:", list(squares))
    print("Cubes:", list(cubes))

if __name__ == "__main__":
    main()


# Call the submit() method of the ThreadPoolExecutor to submit 
# a task to the thread pool for execution. The submit() method 
# returns a Future object.
# Call the map() method of the ThreadPoolExecutor class to 
# execute a function in a thread pool with each element in a list.