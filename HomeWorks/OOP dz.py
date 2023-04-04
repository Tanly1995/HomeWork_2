#Zadanae 1
'''class City:
    def __init__(self, country, city, people_count, post_index, telephone_code):
        self.strana = country
        self.gorod = city
        self.naselenie = people_count
        self.indeks = post_index
        self.telefon = telephone_code

    def city_info(self):
        print(self.strana, self.gorod, self.naselenie, self.indeks, self.telefon)


a = City(input("Введи страну: "), input("Введи город: "), input("Население: "), input("Индекс города: "), input("Телефонный код: "))
a.city_info()'''

#Zadanie 2
'''class Drob:
    def __init__(self, chislitel, znamenatel):
        self.chislitel = chislitel
        self.znamenatel = znamenatel

    def plus(self):
        otvet_plus = print(self.chislitel + self.znamenatel)
    def minus(self):
        otvet_minus = print(self.chislitel - self.znamenatel)
    def delit(self):
        otvet_delit = print(self.chislitel / self.znamenatel)
    def umnojit(self):
        otvet_umnojit = print(self.chislitel * self.znamenatel)

a = Drob(int(input("Vvedi chislo: ")), int(input("Vvedi 2 chislo: ")))
a.delit()
a.plus()
a.minus()
a.umnojit()'''

#Zadanie 3
'''class Podscet:
    def __init__(self, first_element, second_element, third_element, fourth_element):
        self.first = first_element
        self.second = second_element
        self.third = third_element
        self.fourth = fourth_element
    def max(self):
        spisok = print(max(self.first, self.second, self.third, self.fourth))
    def min(self):
        spisok = print(min(self.first, self.second, self.third, self.fourth))
    def arifm(self):
        spisok = print((self.first +self.second + self.third + self.fourth)/4)

a = Podscet(int(input("pervoe chislo: ")),int(input("vtoroe chislo: ")),int(input("trete chislo: ")),int(input("chetvertoe chislo: ")))
a.max()
a.min()
a.arifm()'''

#Zadanie 4
'''class Formule:
    def __init__(self, first_value,second_value,third_value,fourth_value):
        self.first = first_value
        self.second = second_value
        self.third = third_value
        self.visota = fourth_value
    def square(self):
        otvet = print(self.first*4)
    def rectangle(self):
        otvet = print((self.first + self.second) * 2)
    def triangle(self):
        otvet = print("1 formula",0.5*self.first*self.second)
        otvet = print("2 formula",0.5*self.visota*self.first)
    #Formuli neoxota pisat vse

a = Formule(int(input("Vvedi 1 chislo: ")),int(input("Vvedi 2 chislo: ")),int(input("Vvedi 3 chislo: ")),int(input("Vvedi visotu: ")))
a.square()
a.rectangle()
a.triangle()'''