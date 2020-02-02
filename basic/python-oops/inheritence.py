# Types of Inheritance
#  Single Inheritance
#  Hierarchical Inheritance
#  Multiple Inheritance
#  Cyclic Inheritance
#  Hybrid Inheritance(Combined of the all above)
#  MRO Algorithm (Method resolution operator)

class P:
    def property(self):
        print('cash+land+gold+power')

    def marry(self):
        print('Subbalaxmi')


class C(P):
    def marry(self):
        print('Katrina')


c = C()
c.property()
c.marry()
