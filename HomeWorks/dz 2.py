#Так и не смог найти ошибку в коде
'''
range_1 = int(input("Please, Enter the Range Value: ")) #10
povtorenia = int(input("Please, Enter the Range Value: "))#10
number = 2
number_2 = 1
counter=0
print("The Простые числа в диапазоне: ")
while number<=range_1:# 2<10
  print(number)
  number += 1 # 3
  continue
  while number_2<=povtorenia: #1 - 10
    if number%number_2==0:
        counter+=1
        continue
    number_2+=1
  if counter>=0:
    print(counter)
'''
                            #Задание 1
#Его условие совпадает с заданием 2.3, не вижу смысла тоже самое писать и тут


                            #Задание 2
#2.1
'''
nacalo = int(input("Nacalo diapazona: ")) #8
konec = int(input("Konec  diapazona: ")) #14
num = nacalo
print("Числа в диапазоне", nacalo, "до", konec)
while nacalo <= num and num <= konec:
  print(num)
  num +=1
'''
#2.2
'''
nacalo = int(input("Nacalo diapazona: ")) #8
konec = int(input("Konec  diapazona: ")) #14
num = konec
print("Числа в диапазоне", konec, "до", nacalo)
while konec >= num and num >= nacalo:
  print(num)
  num -=1
'''
#2.3
'''
nacalo = int(input("Nacalo diapazona: ")) #6
konec = int(input("Konec  diapazona: ")) #30
num = nacalo
print("Числа в диапазоне", nacalo, "до", konec, "кратные 7 таковы: ")
while nacalo <= num and num <= konec:
  if num % 7 == 0:
    print(num)
    num +=1
  else:
    num +=1
print("Vse")
'''
#2.4
'''
nacalo = int(input("Nacalo diapazona: ")) #4
konec = int(input("Konec  diapazona: ")) #33
num = nacalo
count = 0
print("Числа в диапазоне", nacalo, "до", konec, "кратные 5 таковы: ")
while nacalo <= num and num <= konec:
  if num % 5 == 0:
    print(num)
    num +=1
    count += 1
  else:
    num +=1
print("Количество кратных чисел = ", count)
'''

                                #Задание 3
'''
nacalo = int(input("Nacalo diapazona: ")) #1
konec = int(input("Konec  diapazona: ")) #20
num = nacalo
print("Числа в диапазоне", nacalo, "до", konec)
while nacalo <= num and num <= konec:
  if num % 5 == 0 and num % 3 == 0:
    print(num, "Fizz Buzz")
    num += 1
  elif num % 3 == 0:
    print (num, "Fizz")
    num += 1
  elif num % 5 == 0:
    print (num, "Buzz")
    num += 1
  else:
    print(num)
    num += 1
'''