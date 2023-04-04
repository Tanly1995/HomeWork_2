                                #Задание 1
                        #1.1 с уже готовыми значениями
'''
bilet_vzrosliy = 3
bilet_deti = 5
vsego = bilet_vzrosliy + bilet_deti
cena_vzroslogo = 10
#10 - 100%
#x - 60%
cena_deti = int((10*60)/100)
summa = cena_vzroslogo + cena_deti
print("Всего билетов:", vsego)
print("Сумма:", summa, "AZN")
'''

                        #1.2 где сам вводишь данные
'''
print("Добро пожаловать Рафаель. Сколько билетов вы хотели бы купить? Цена для взрослых - 10 azn, для детей по скидке в 40% составляет - 6 azn")
bilet_vzrosliy = int(input("Введите кол-во билетов взрослых: "))
bilet_deti = int(input("Введите кол-во билетов детей: "))
vsego = int(bilet_vzrosliy + bilet_deti)
cena_vzroslogo = int(bilet_vzrosliy * 10)
#10 - 100%
#x - 60%
#cena_deti = int((10*60)/100) = 6 AZN
cena_deti = int(bilet_deti * 6)
summa = int(cena_vzroslogo + cena_deti)
print("Всего билетов куплено: ", vsego)
print("Общая цена: ", summa, "AZN")
'''
                                 #Задание 2
'''
cena_bloknota = int(input("Введи цену блокнота: "))
kolvo_bloknotov = int(input("Введи количество блокнотов: "))
skidka = int(input("Введи скидку от 0-100: "))
#допустим 3 манат блокнот, взял 5 штук, скидка 20, тогда 5*3=15 это 100%, тогда (15*20)/100  3 манат это скидка, тогда 15 блокнотов будут стоить 12 манат
if cena_bloknota or kolvo_bloknotov or skidka <= 0:
    print("ERROR 404")
else:
    summa = float(cena_bloknota * kolvo_bloknotov - (((cena_bloknota * kolvo_bloknotov) * skidka) / 100))
    print("Общая цена: ", summa)
'''

                                #Задание 3
'''
num_1 = int(input("Введите первое число - "))
num_2 = int(input("Введите второе число - "))
num_3 = int(input("Введите третье число - "))
if num_1 > num_2 and num_1 > num_3:
    print("1st: True")
else:
    print("1st: False")

if num_2 > num_3 and num_2 < num_1:
    print("2nd: True")
else:
    print("2nd: False")

if num_3 > 0 and num_3 < num_1 and num_3 < num_2:
    print("3rd: True")
else:
    print("3rd: False")
'''

                            #Задание 4
#Не смог сделать
'''
num_1 = int(input("Vvedi pervoe chislo ejji - "))
num_2 = int(input("Vvedi vtoroe chislo ejji - "))
num_3 = int(input("Vvedi tretye chislo ejji - "))
num_4 = int(input("Vvedi chetvertoe chislo ejji - "))
num_5 = int(input("Vvedi patyoe chislo ejji - "))

summa = num_1 + num_2 +num_3 + num_4 + num_5
obsee = ((num_1 * 10000) + (num_2 * 1000) + (num_3 * 100) +(num_4 * 10) + num_5)
if obsee:
    float(num_1 % 2) or float(num_1 % 3)
    float(num_2 % 2) or float(num_2 % 3)
    float(num_3 % 2) or float(num_3 % 3)
    float(num_4 % 2) or float(num_4 % 3)
    float(num_5 % 2) or float(num_5 % 3)
    print("Не все числа простые")
else:
    num_1 / 1 and num_1 / num_1
    num_2 / 1 and num_2 / num_2
    num_3 / 1 and num_3 / num_3
    num_4 / 1 and num_4 / num_4
    num_5 / 1 and num_5 / num_5
    print(summa)
'''












