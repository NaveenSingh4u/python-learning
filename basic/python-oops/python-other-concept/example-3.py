from threading import *

# Setting and getting name in Thread

print(current_thread().getName())
current_thread().setName('Nargis Faqri')
print(current_thread().getName())
current_thread().name = 'Durga'
print(current_thread().getName())


def test():
    print('Child thread')


t = Thread(target=test)
t.start()

print('Main Thread identification number ', current_thread().ident)
print('Child Thread identification number ', t.ident)
