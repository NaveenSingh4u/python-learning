import sys
import time


class Test:
    def __init__(self):
        print('Object initilization..')

    def __del__(self):
        print('Performing cleaning activity..')


# Here init method will be called followed by del.
# Here we're creating 3 object and assigning in list so
# when list will None..All 3 Test object(reference variable) will go for GC.
list = [Test(), Test(), Test()]
time.sleep(5)
list = None
time.sleep(5)

t1 = Test()
t2 = t1
t3 = t2
t4 = t3

# Total no of reference variable = 5(t1,t2,t3,t4 and __init__ of t1)
# Each will have 5 ref as we are assigning.
print(sys.getrefcount(t1))
print(sys.getrefcount(t2))
print(sys.getrefcount(t3))
print(sys.getrefcount(t4))

del t3
del t4
# Now no of reference variable should be 3.
print(sys.getrefcount(t1))
print(sys.getrefcount(t2))


print('\nEnd of Application..')
