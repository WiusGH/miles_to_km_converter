def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(5, 5, 5, 6))


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw['model']

car = Car(model='Lancer Evo IX')
print(car.make)
