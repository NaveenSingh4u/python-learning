from threading import *


# Predefined method run. We're only overriding it.
class MyThread(Thread):
    def run(self):
        for i in range(10):
            print('Child Thread ', current_thread().getName())


t = MyThread()
t.start()
# Note above method will called by Child thread.

for i in range(5):
    print('Main Thread ', current_thread().getName())
# Note above method will called by Main thread.
