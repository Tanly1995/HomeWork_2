                                            #Lesson 17
'''
string = "hello world"
c0 = string[-1]
print(c0)
'''
'''
string = "hello"
string_1 = "hello"
string[-1] = "R"
print(string)
'''
'''
string = "infinity" 
print(string[:3])      #Начинается от 0 до 3 буквы
print(string[2:6])     #Начинается от 2 до 6 буквы   
print(string[0:8:2])   #Начинается от 0 до 8, каждые 2 буквы
'''
'''
stroka = input()
print(len(stroka))  #Показывает длину строки
'''
'''
print("zero"+"infiniy")     # Соеденяет 2 слова слитно
print("zero"*4)             # Напечатает слово 4 раза
'''
'''
string_1 = "ZaB"
string_2 = "zAb"
print(string_1>string_2)
'''
'''
string = "first item"
a = "t"
print(a in string)  # Проверка буквы в строке
'''
'''
string = input("Введи слово = ")
a = "g"
count = 0
print(a in string)
for i in string:
    if i == a:
        count += 1
print(count)
'''
'''
string = input("Введи слово = ")
for i in range(0, len(string)):
    print(string[i], end='')
'''

string = input("Введи слово = ") #Hello
#1 Variant
#print(string[::-1])
#2 Variant
for i in range(1, len(string)+1):
    print(string[-i], end = '')
#3 Variant
#for i in range(len(string)-1, -1, -1):
    #print(string[i], end = '')

                                            #Lesson 18
'''
\n - перенос всего слова после меня на новую строку
\t - табуляция
\b - удалить предыдущий символ
\' - 
\" - 
\\ - 
'''
'''
print("Hello '\n' World")
print("Hello '\t' World")
print("Hello '\b' World")
string = '\"Карты на столе\"'
print("string")
'''

'''
string = 'Hello'
string_1 = 'hello'
string_2 = 'ACADEMY'
string_3 = 'pelmeni vkusniye ua yaaa'
string_4 = '      pelmeni vkusniye ua yaaa'

print(str.lower(string))
print(str.capitalize(string_1))
print(str.upper(string_1))
print(str.casefold(string_2))
print(str.title(string_3))
print(str.swapcase(string_3))
print(str.ord("R"))
print(str.strip(string_4))
print(str.replace(string_1,string_4))

text = 'borsh'
print(text.replace('borsh', 'hinkali'))

print(str.split(string_3))
print(string.find('o',0 ,5))
'''

