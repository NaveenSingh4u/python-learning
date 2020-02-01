# class
class Student:
    cname = 'DURGASOFT'

    def setName(self, name):
        self.name = name

    def setMarks(self, marks):
        self.marks = marks

    def getName(self):
        return self.name

    def getMarks(self):
        # Validation stuff
        return self.marks

    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

    # when we will call this method marks field will be added in that calling object
    def info(self):
        self.marks = 60

    def talk(self):
        print("hello my name is " + self.name)
        print("hello my roll number is " + str(self.rollno))

    # For defining class level method use @classmethod decorator
    # cls : class level data
    @classmethod
    def getCollegeName(cls):
        print('College name', cls.cname)

    # use static method for creating utility.
    @staticmethod
    def findAverage(x,y):
        print('Average',(x+y)/2)

s1 = Student(100, 'Ram lal')
print(s1.rollno)
print(s1.name)
s1.talk()
s1.getCollegeName()
s1.info()
print(s1.__dict__)

s2 = Student(101, 'Ram manohar')
s2.talk()
s2.findAverage(20,60)
# We can add attribute in instance
s2.wife = 'Renuka'
print(s2.__dict__)

# if method is decorator by @staticmethod..Call method directly by class
Student.findAverage(20,60)

n = int(input("Enter the number of students:"))
for i in range(n):
    name = input('Enter the Student name')
    marks = int(input('Enter Student marks'))
    s = Student()
    s.setName(name)
    s.setMarks(marks)