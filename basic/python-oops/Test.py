# instance variable vs static variable
# instance: For every object a separate copy
# static: For all object a single copy maintained at class level

class Test:
    f = 60
    # constructor overloading
    def __init__(self):
        print("zero argument")
        self.a = 10
        self.b = 20
        self.c = 30

    def m1(self):
        # this variable can be accessed from anywhere in class
        global x
        self.d = 40

    def m2(self):
        x = 500
        print(x)
        self.e = 50

    # del is used for deleting
    def delete(self):
        del self.a
        del self.b

t1 = Test()
t1.m1()


t2 = Test()

# assigning value and accessing that.
Test.h = 80
print(Test.h)

t2.m2()
t2.s = 200
t2.y = 300

print(t1.__dict__)
print(t2.__dict__)
t1.delete()
print("After deleting\n")
print(t1.__dict__)
