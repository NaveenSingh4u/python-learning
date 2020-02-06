# There are three ways for creating Thread in Python
# 1. Creating Thread without using any class.
# 2. Creating Thread by extending Thread class.
# 3. Creating Thread without extending Thread class.

# Difference between importing thread in python
# Call with module
import threading

threading.current_thread()

# Call without module
from threading import *

current_thread()


def display():
    for i in range(10):
        print('Child Thread')

def displayThread():
    print(current_thread().getName())

# t = Thread(target=display) # creation of Thread object to execute display
t = Thread(target=displayThread)
t.start()

for i in range(10):
    print('Main Thread', current_thread().getName())

#Note: We can't predict exact output. It may vary run to run.
# Because they are runnning in parallel.