#1 zadanie
'''class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, dobavit):
        self.__balance += dobavit
        print(self.__balance)
    def withdraw(self, snat):
        self.__balance -= snat
        print(self.__balance)
dobavit = int(input("Skolko dobavit: "))
snat = int(input("Skolko snat: "))
a = BankAccount(3000)
a.deposit(dobavit)  #Почему в скобках написали добавить?
a.withdraw(snat)'''

#2 zadnie
'''class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def set_salary(self, value):
        self.__salary = value

    def get_salary(self):
        return self.__salary

employee = Employee(1300)
print(employee.get_salary())'''

#3 zadanie
'''class Student:
    def __init__(self, grades):
        self.__grades = grades

    def get_grades(self):
        return self.__grades

    def add_grades(self, new_grade):
        self.__grades = new_grade


student = Student(10)
student.add_grades(7) #Введи новое число
print(student.get_grades())'''

#4 zadanie
'''class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year

    def get_car_info(self):
        print(self.__brand, self.__model, self.__year)

car = Car("BMW", "M3 GTR", 2002)
car.get_car_info()'''

#5 zadanie
'''class Game:
    def __init__(self, score):
        self.__score = score

    def update_score(self, value):
        self.__score = value

    def get_score(self):
        return self.__score

game = Game(2100)
game.update_score(3400)
print(game.get_score())'''
