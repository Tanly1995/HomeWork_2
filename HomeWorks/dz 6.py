        #Задание 1
'''
# 1)Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы
a = input() #i love 5 lol! yasuo 3 is 1 broken. yo9ne!
numbers = 0
znaki_prepinania = 0
vosklic = 0
print(a.title())
    # 2)Посчитайте сколько раз цифры встречаются в тексте
for i in a:
    if ord(i)>=48 and ord(i)<=57:
        numbers += 1
    # 3)Посчитайте сколько раз знаки препинания встречаются в тексте
    if (ord(i)>=33 and ord(i)<=47) or (ord(i)>=58 and ord(i)<=64):
        znaki_prepinania += 1
    # 4)Посчитайте количество восклицательных знаков в тексте
    if ord(i)==33:
        vosklic += 1

print("Всего чисел =", numbers)
print("Всего знаков препинания =", znaki_prepinania)
print("Всего восклицательных знаков =", vosklic)
'''

        #Задание 2
'''
virajenie = input("Введите выражение = ")
new_virajenie = virajenie.split(' ')
print(new_virajenie)
if new_virajenie[1] == '+':
    print(f'Ответ = {float(new_virajenie[0]) + float(new_virajenie[2])}')
elif new_virajenie[1] == '-':
    print(f'Ответ = {float(new_virajenie[0]) - float(new_virajenie[2])}')
elif new_virajenie[1] == '/':
    print(f'Ответ = {float(new_virajenie[0]) / float(new_virajenie[2])}')
elif new_virajenie[1] == '*':
    print(f'Ответ = {float(new_virajenie[0]) * float(new_virajenie[2])}')
'''

        #Задание 3
'''for i in range(0,6):
    for j in range(0,6):
        print('*', end = '')
    print(' ')
print("\n")
for i in range(0,6):
    for j in range(0, 6):
        if j==0 or j==5 or i==0 or i==5:
            print("*", end = '')
        else:
            print(" ", end='')
    print(' ')'''