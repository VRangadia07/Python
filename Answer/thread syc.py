# Lock 
# Ensures that only one thread can access a critical section of code at a time.

# a threading lock has two states: locked and unlocked. 
# When a thread acquires a lock, the lock enters the locked state. 
# The thread can have exclusive access to the shared resource.

# A lock is acquired using acquire() and released using release(). 
# Using the with statement automatically handles acquiring and releasing the lock.


from threading import Thread, Lock
from time import sleep


counter = 0


def increase(by, lock):
    global counter

    lock.acquire()

    local_counter = counter
    local_counter += by

    sleep(0.1)

    counter = local_counter
    print(f'counter={counter}')

    lock.release()


lock = Lock()

# create threads
t1 = Thread(target=increase, args=(10, lock))
t2 = Thread(target=increase, args=(20, lock))

# start the threads
t1.start()
t2.start()


# wait for the threads to complete
t1.join()
t2.join()


print(f'The final counter is {counter}')



# Event
# Allows one thread to signal one or more threads to proceed.
# The Event class offers a simple but effective way to coordinate between threads: 
# one thread signals an event while other threads wait for it.

from threading import Thread, Event
from time import sleep

def task(event: Event, id: int) -> None:
    print(f'Thread {id} started. Waiting for the signal....')
    event.wait()
    print(f'Received signal. The thread {id} was completed.')

def main() -> None:
    event = Event()

    t1 = Thread(target=task, args=(event,1))
    t2 = Thread(target=task, args=(event,2))

    t1.start()
    t2.start()

    print('Blocking the main thread for 3 seconds...')
    sleep(3) 
    event.set()



if __name__ == '__main__':
    main()
    
# all the wait() method of the event object, 
# both t1 and t2 threads will wait for the event to be set before continuing.
# calling the set() method from the main thread

# Use the Event object to stop a child thread.
# Use the set() method to set an internal flag of an Event object to True.
# Use the is_set() method to check if the internal flag of an Event object was set.

# Semaphore
# Controls access to a resource pool with a fixed number of available slots.

# A Python semaphore is a synchronization primitive that 
# allows you to control access to a shared resource.

# Each acquire() call decrements the semaphore's counter, and each release() call increments it. 
# If the counter reaches zero, subsequent acquire() calls block until another thread releases the semaphore.

import threading
import time

# Create a semaphore with a maximum of 2 threads allowed
semaphore = threading.Semaphore(2)

def access_resource(thread_id):
    with semaphore:
        print(f"Thread-{thread_id} is accessing the resource")
        time.sleep(2)
        print(f"Thread-{thread_id} has finished using the resource")

# Create and start 5 threads
threads = []
for i in range(5):
    thread = threading.Thread(target=access_resource, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# The with statement ensures that the semaphore is properly 
# released even if an exception occurs within the block.
# Each thread attempts to acquire the semaphore before accessing the resource. 
# If the semaphore's value is greater than zero, the thread acquires it and decrements the value.
# After accessing the resource, the thread releases the semaphore, incrementing its value, 
# allowing other threads to acquire it.
















































































# from threading import Thread
# from time import sleep

# def my_function_1(arg):
#    for i in range(arg):
#       print("Child Thread 1 running", i)
#       sleep(0.5)

# def my_function_2(arg):
#    for i in range(arg):
#       print("Child Thread 2 running", i)
#       sleep(0.1)

# # Create thread objects
# thread1 = Thread(target=my_function_1, args=(5,))
# thread2 = Thread(target=my_function_2, args=(3,))

# # Start the first thread and wait for 0.2 seconds
# thread1.start()
# thread1.join(timeout=0.2)

# # Start the second thread and wait for it to complete
# thread2.start()
# thread2.join()

# print("Main thread finished...exiting")

