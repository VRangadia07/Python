# queue module allows you to exchange data safely between multiple threads. 
# The Queue class in the queue module implements all required locking semantics.

import time
from queue import Empty, Queue
from threading import Thread


def producer(queue):
    for i in range(1, 6):
        print(f'Inserting item {i} into the queue')
        time.sleep(1)
        queue.put(i)


def consumer(queue):
    while True:
        try:
            item = queue.get()
        except Empty:
            continue
        else:
            print(f'Processing item {item}')
            time.sleep(2)
            queue.task_done()


def main():
    queue = Queue()

    # create a producer thread and start it
    producer_thread = Thread(
        target=producer,
        args=(queue,)
    )
    producer_thread.start()

    # create a consumer thread and start it
    consumer_thread = Thread(
        target=consumer,
        args=(queue,),
        daemon=True
    )
    consumer_thread.start()

    # wait for all tasks to be added to the queue
    producer_thread.join()

    # wait for all tasks on the queue to be completed
    queue.join()


if __name__ == '__main__':
    main()
    
# To add an item to the queue, you use the put() method 
# To get an item from the queue, you can use the get() method

# producer() function that adds numbers from 1 to 11 to the queue. 
# It delays one second in each iteration

# consumer() function that gets an item from the queue and processes it. 
# It delays two seconds after processing each item on the queue

# task_done() indicates that the function has processed the item on the queue.

# main() function that creates two threads, 
# one thread adds a number to the queue every second 
# while another thread processes an item on the queue every two seconds

# Wait for all the tasks on the queue to be completed by calling the join() method of the queue.