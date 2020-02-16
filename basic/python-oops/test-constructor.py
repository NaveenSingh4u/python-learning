class Test:
    count = 0
    def __init__(self):
        Test.count = Test.count + 1

    @classmethod
    def getNoOfobject(cls):
        print('The number of object created', cls.count)

t1 = Test()
t2 = Test()
t3 = Test()
t3.getNoOfobject()


t4 = Test()
t5 = Test()
t5.getNoOfobject()