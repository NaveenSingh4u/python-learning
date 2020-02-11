# Generators are useful in
# 1. To implement countdown
# 2. To generate first n number
# 3. To generate fibonacci series
import random
import time


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for n in fib():
    if n > 1000:
        break
    print(n)

names = ['sunny', 'bunny', 'chinmayee', 'vinny']
subjects = ['Python', 'Java', 'Blockchain']


def people_list(num):
    results = []
    for i in range(num):
        person = {
            'id': i,
            'name': random.choice(names),
            'subject': random.choice(subjects)
        }
        results.append(person)
    return results


def generate_people_list(num):
    for i in range(num):
        person = {
            'id': i,
            'name': random.choice(names),
            'subject': random.choice(subjects)
        }
        yield person

# See the performance difference between both approach.

t1 = time.clock()
people = people_list(10000)
t2 = time.clock()
print('Time taken : ', t2 - t1)

t1 = time.clock()
people = generate_people_list(10000)
t2 = time.clock()
print('Time taken : ', t2 - t1)
