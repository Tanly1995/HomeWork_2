                            # Задание 1
'''
x = int(input("Введи первое число= "))
#1
y = int(input("Введи второе число= "))
#6

for i in range (x, y+1): #1,2,3,4,5,6
  count = 1
  otvet = 1
  while count <= y: #1<6
    otvet *= i
    count += 1
  print(otvet)
'''

                            # Задание 2
'''
import random

print("Добро пожаловать в угадай число! начать игру?" '\n' "1) Да" '\n' "2) Нет")
igra = int(input("Выбор = "))

while igra == 1:
    num = random.randint(1, 500)
    print(num)
    x = int(input("Игра началась!!" '\n' "Угадай число от 1 до 500. Ответ = "))
    counter = 0

    while x != num:
        if x < num:
            print("Число выше")
        elif x > num:
            print("Число ниже")
        counter += 1
        x = int(input("Попробуй снова = "))

    print("Молодец! Ты угадал!")
    print("Общее число попыток = ", counter)
    igra = 0
    print("Хотите поиграть снова?" '\n' "1) Да" '\n' "2) Нет")
    igra = int(input("Выбор = "))
else:
    print("Игра окончена")
'''