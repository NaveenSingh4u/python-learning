import gc
import time


class GarbageCollector:
    def __init__(self):
        print('Object initilization.....')

    def __del__(self):
        print('Fulfilling last wish and cleaning up the activity..')

    def showDemo(self):
        # By default gc always enabled.
        print(gc.isenabled())
        gc.disable()
        print(gc.isenabled())
        gc.enable()
        print(gc.isenabled())

        # following method called by GC automatically for cleanup activity.
        # GC invoked by PVM (Python virtual machine)
        # __del__(self): ===> Destructor
        # close db connection
        # close network connection

# Even if GC is disabled then also __del__ method will be called by class
gc.disable()

t1 = GarbageCollector()
# when this method will called __del__ method will be automtically called by GC.
t1 = None
print(t1)

t2 = t1
t3 = t2
t4 = t3
del  t1
time.sleep(5)
print('After deleting t1 object not destroyed..')
del t2
del t3
time.sleep(5)
print('still object is not eligible for gc')
time.sleep(5)
del t4
print('Endof Appn.......')


time.sleep(10)
print('End of Application..')
