#1 zadanie
'''class Cars:
    def __init__(self, model, year, city, engine, color, cost):
        self.model = model
        self.year = year
        self.city = city
        self.engine = engine
        self.color = color
        self.cost = cost
    def info(self):
        print(self.model, self.year, self.city, self.engine, self.color, self.cost)

cars = Cars(input("model: "), input("year: "), input("city :"), float(input("engine: ")), input("color: "), input("cost: "))
cars.info()'''

#2 zadanie ne polucilos
'''class Shape:
    def __init__(self,width, heigh, radius):
        self.__width = width
        self.__heigh = heigh
        self.__radius = radius

class Square:
    def square(self, width):
        print(width)

class Rectangle(Shape):
    def rectangle(self, width, heigh):
        print(width, heigh)

class Circle(Shape):
    def circle(self, radius):
        print(radius)

shape = Shape(14, 17, 9)
squ = Square(14)
rec = Rectangle()
circ = Circle'''

#3 zadanie
'''class Flat:
    def __init__(self, plosad, cena):
        self.plosad = plosad
        self.cena = cena

class Flat_2:
    def __init__(self, plosad_2, cena_2):
        self.plosad_2 = plosad_2
        self.cena_2 = cena_2

flat_1 = Flat(32, 3000)
flat_2 = Flat_2(28, 2700)
print(flat_2.plosad_2 == flat_1.plosad)
print(flat_1.plosad != flat_2.plosad_2)
print(flat_1.cena > flat_2.cena_2)
print(flat_1.cena < flat_2.cena_2)'''

#4 zadanie
'''class Passport:
    def __init__(self, name, age, nationality):
        self.__name = name
        self.__age = age
        self.__nationality = nationality
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age
    def get_age(self):
        return self.__age

    def set_nationality(self, nationality):
        self.__nationality = nationality
    def get_nationality(self):
        return self.__nationality

class ForeignPassport(Passport):
    def __init__(self, name, age, nationality, visa, number):
        super(). __init__(name, age, nationality)
        self.__visa = visa
        self.__number = number
    def set_visa(self, value):
        self.__visa = value
    def set_number(self, value):
        self.__number = value
    def get_visa(self):
        return self.__visa
    def get_number(self):
        return self.__number

passport = Passport("John", 32, "Mexican")
print(f'Человека зовут {passport.get_name()}, его возраст {passport.get_age()}, национальность {passport.get_nationality()}')
foreign = ForeignPassport("John", 32, "Mexican", 0, 0)
foreign.set_number(34534)
foreign.set_visa('AZE14141')
print(f'Серийный номер заграна {foreign.get_number()}, его VISA {foreign.get_visa()}')'''

#5 zadnie неохота было делать