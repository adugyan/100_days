def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

#print(add(1,2,5))

def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    sum: int = 0
    product: int = 0
    n += kwargs['add']
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs['make']
        self.model = kwargs.get("model") # This retrieves the dictionary key's value. If there is none it returns none
        # used to handle when users don't put a keyword in
        self.print_car_info()

    def print_car_info(self):
        print(self.make, self.model)

my_car= Car(make = 'Nissan', model='Sentra')

