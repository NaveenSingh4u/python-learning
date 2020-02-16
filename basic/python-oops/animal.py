class Animal:
    leg = 4

    @classmethod
    def walk(cls, name):
        print('{} walk with {} legs'.format(name, cls.leg))


Animal.walk('Dog')
Animal.walk('Cow')
