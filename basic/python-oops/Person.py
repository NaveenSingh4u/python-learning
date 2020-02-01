class Person:
    def __init__(self):
        self.name = 'Durga'
        self.dob = self.DOB()

    def display(self):
        print("Name : ", self.name)
        self.dob.display()

    class DOB:
        def __init__(self):
            self.dd = 10
            self.mm = 11
            self.yyyy = 1995

        def display(self):
            print('DOB = {}/{}/{}'.format(self.dd, self.mm, self.yyyy))

p = Person()
p.display()