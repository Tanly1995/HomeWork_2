'''class student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.progress = 0

    def print_info(self):
        return self.name, self.age

    def study(self,subject,study):
        if study:
            self.progress += 1
            print(f"You study {subject} and progress = {self.progress}")
        else:
            self.progress -= 1
            print(f"Progress decreased by 1. Overall progress = {self.progress}")

student = student("Rashad", 24)
student.study("Programming", True)'''

'''def food(a, b = "Pizza"):
    class MyClass:

        def my_method(self, a, b=None):
            if b:
                print(a, b)
            else:
                print(a)'''

class human:
    def __init__(self, name,age,city,phone):
        self.name = name
        self.age = age
        self.city = city
        self.phone = phone

    def info(self):
        print(self.name, self.age, self.city, self.phone)

human = human(input("Vvedi imya ="), input("Vvedi vozrast ="), input("Vvedi gorod ="), input("Vvedi telefon ="))
human.info()
