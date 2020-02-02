class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # n no of properties

    def display(self, name, age):
        print('Name : ', self.name)
        print('Age : ', self.age)


class Student(Person):
    def __init__(self, name, age, rollno, marks):
        # self.name = name
        # self.age = age
        # The above both line can be replaced by following line
        super().__init__(name, age)
        # n no of properties
        self.rollno = rollno
        self.marks = marks

    def display(self):
        # print('Name : ', self.name)
        # print('Age : ', self.age)
        super().display(self.name, self.age)
        print('Roll no : ', self.rollno)
        print('Marks : ', self.marks)


class Teacher(Person):
    def __init__(self, name, age, salary, subject):
        # self.name = name
        # self.age = age
        # The above both line can be replaced by following line
        super().__init__(name, age)
        self.salary = salary
        self.subject = subject

    def display(self):
        # print('Name : ', self.name)
        # print('Age : ', self.age)
        super().display(self.name, self.age)
        print('Salary : ', self.salary)
        print('Subject : ', self.subject)


s = Student('Ravi', 23, 101, 90)
p = Teacher('Durga', 62, 10000, 'Python')
s.display()
p.display()
