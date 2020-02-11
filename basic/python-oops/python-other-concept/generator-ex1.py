# input function --> [ Decorator Function] --> output function
# [ Generator function] --> To generate sequence of values.

def mygen():
    yield 'A'
    yield 'B'
    yield 'C'

g = mygen()

# Following is also a way for storing variable but it will take memory.
l = ['A', 'B', 'C']

# printing type of g variable
print(type(g))

# printing sequence of value
print(next(g))
print(next(g))
print(next(g))

# this will throw error(Stop iteration) as only 3 value defined.
print(next(g))