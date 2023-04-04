    #Задание 1
'''
string = input("Введи слово - ")
reverse = str(string[::-1])
print(reverse)
if string == reverse:
  print("cлово палиндром")
else:
  print("не палиндром")
'''

    #Задание 2
'''
string = input("Введи число - ")
reverse = string[::-1]
print(reverse)
if string == reverse:
  print("число палиндром")
else:
  print("не палиндром")
'''

    #Задание 3
'''
string_1 = input("Введи текст = ") #fg45h3f@fg%
cifri = 0
bukvi = 0
znaki = 0
for i in range(0,len(string_1)):
    if string_1[i].isdigit():
        cifri += 1
    elif string_1[i].isalpha():
        bukvi += 1
    else:
        znaki += 1
print(cifri,bukvi,znaki)
'''

    #Задание 4
'''
string_1 = input("Введи текст = ") #apple#34%
znaki = 0
for i in string_1:
    if ord(i)>32 and ord(i)<48:
        znaki += 1
    if ord(i) > 57 and ord(i) < 65:
        znaki += 1
print("Всего знаков = ", znaki)
'''
