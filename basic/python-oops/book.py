class Book:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return 'The number of pages: ' + str(self.pages)

    def __add__(self, other):
        total = self.pages + other.pages
        b = Book(total)
        return b

    def __sub__(self, other):
        total = self.pages - other.pages
        b = Book(total)
        return b

    def __mul__(self, other):
        total = self.pages * other.pages
        b = Book(total)
        return b


b1 = Book(100)
b2 = Book(200)
b3 = Book(700)
print('Add')
print(b1 + b2)
print(b1 + b3)

print('Sub')
print(b1 - b2)

print('Mul')
print(b1 * b2)

# Note : 1.whenever we are calling + operator then __add__() method will be called.
# 2. Whenever we're printing Book object reference then __str__() method will be called.

print("Printing multiple add ..")
print(b1 + b2 + b3)
print(" add with multiple")
print(b1 * b2 + b2 * b3)
