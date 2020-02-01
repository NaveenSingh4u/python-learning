class Employee:
    # use can write doc string by using '''
    '''class for handling employee data'''

    # self is a reference variable which always refer to current object.
    # For defining constructor method name should always __init(self)
    # while creating the object this method will be automatically called.
    def __init__(self, empno, empname, empsal, empaddr):
        self.empno = empno
        self.empname = empname
        self.empsal = empsal
        self.empaddr = empaddr

    def info(self):
        print('*'*20)
        print("Employee number :"+str(self.empno))
        print("Employee name :" + self.empname)
        print("Employee salary :" + str(self.empsal))
        print("Employee address :" + self.empaddr)
        print('*'*20)

naveen = Employee(428,"Naveen", 260000.00,"Pune")
naveen.info()

# we use __doc__ for getting class information
print(Employee.__doc__)

# for getting data of employee class (information)
help(Employee)