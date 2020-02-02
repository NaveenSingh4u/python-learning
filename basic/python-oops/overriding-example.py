class Test:
    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            print('The sum of 3 numbers :', a + b + c)
        elif a != None and b != None:
            print('Some of 2 numbers: ', a + b)
        else:
            print('Please provide 2 or 3 arguments')

    # For adding
    def add(self, *a):
        total = 0
        for x in a:
            total = total + x
            print('The add', total)

    def addString(self, *s):
        total = ''
        for x in s:
            total = total + x
            print('The add ', total)

    def __init__(self, *a):
        print('Constructor with any number of argument..')

# Note: *args = same type of argument(any number of argument)

t = Test()
t.sum(10, 20, 30)
t.sum(10, 20)
t.sum(10)
print('***********************************************')

t.add()
print('---------------------')
t.add(10)
print('---------------------')
t.add(10, 20)
print('---------------------')
t.add(10, 20, 30)
print('---------------------')
t.add(10, 20, 30, 40)
print('---------------------')
t.add(10, 20, 30, 40, 50)
print('---------------------')

print('*************************************************')
t.addString('De', 'Dana', 'Dan')
