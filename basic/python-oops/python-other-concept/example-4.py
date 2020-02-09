from threading import *

mt = current_thread()
# isDaemon() and daemon method is used for checking is deamon thread.
print(mt.isDaemon())
print(mt.daemon)

def job():
    print("Executed by t1")
    t2 = Thread(target=job2())
    print("t2 is Deamon : ", t2.isDaemon())

def job2():
    print("Executed by t2")

t1 = Thread(target=job())
t1.setDaemon(True)
print('t1 is Deamon: ', t1.isDaemon())
t1.start()

# Note: Once Thread started we cannot change its Deamon nature.
# mt.setDaemon(True);
# print(mt.isDaemon())

# Note : When last non-deamon thread termiated then automatically all the non deamon thread will terminate.

# Real life example of deamon thread and non- deamon thread.
# 1. Car game
# Cars --> non deamon
# background scenario --> deamon
#
# 2. Cinema shooting
# Hero, Heroine ---> Non- Deamon
# Make up --> Deamon