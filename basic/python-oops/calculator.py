class Calculator:
# Note: 1. staticmethod is used for creating utility
# 2. Do not pass self param in static method
    @staticmethod
    def add(x, y):
        return x + y;

    @staticmethod
    def sub(x, y):
        return x - y;

    @staticmethod
    def mul(x, y):
        return x * y;

    @staticmethod
    def div(x, y):
        return x / y;

    @staticmethod
    def avg(x, y):
        return (x + y) / 2;


print(Calculator.add(120, 39))
print(Calculator.sub(20, 38))
print(Calculator.mul(20, 10))
print(Calculator.div(20, 10))
print(Calculator.avg(10, 20))
