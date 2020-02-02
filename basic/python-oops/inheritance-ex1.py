class A:
    def m1(self):
        print('A class method')


class B(A):
    def m1(self):
        print('B class method')


class C(A):
    def m1(self):
        print('C class method')


class D(B, C):
    def m1(self):
        print('D class method')


d = D()
d.m1()
