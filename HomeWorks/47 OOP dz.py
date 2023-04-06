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

    def add_grades(self):
        self.add_grades()


student = Student(10)
print(student.get_grades())'''

#4 zadanie
