# Import threading module
import threading


# Function definition
def task():

    print("Task Started")


# Create threads
t1 = threading.Thread(target=task)

t2 = threading.Thread(target=task)


# Start threads
t1.start()

t2.start()


"""

Thread 1
   ↓
Acquire GIL
   ↓
Execute Python Code
   ↓
Release GIL
   ↓
Thread 2 Acquires GIL

"""

"""

Thread 1
↓
Calling API
↓
Waiting
↓
Releases GIL

"""