import time


def countdown(num):
    print('Count down starting....')
    while num > 0:
        yield num
        num = num - 1


values = countdown(10)
for x in values:
    print(x)
    time.sleep(1)


# To generate first n number
def firstnNumber(num):
    n = 1
    while n <= num:
        yield n
        n = n + 1


for x in firstnNumber(10):
    print(x)