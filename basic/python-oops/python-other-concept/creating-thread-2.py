from threading import *


# Predefined method run. We're only overriding it.
class Test:
    def m1(self):
        for i in range(10):
            print('Child Thread - 1 ', current_thread().getName())


obj = Test()
t = Thread(target=obj.m1)
t.start()
# Note above method(m1) will called by Child thread.

for i in range(5):
    print('Main Thread ', current_thread().getName())
# Note above method will called by Main thread.
