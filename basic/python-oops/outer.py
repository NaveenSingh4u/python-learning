class Outer:

    def __init__(self):
        print('Outer class object creation')

    def m2(self):
        print('Outer class method')

    class Inner:

        def __init__(self):
            print('Inner class object creation')

        def m1(self):
            print('Inner class method')

# 1st way
o = Outer()
i = o.Inner()
i.m1()

#2nd way
i = Outer().Inner().m1()

#3rd way
Outer().Inner().m1()

# We can't call outer method from inner class object
# i.m2() --> Not possible

o.m2()