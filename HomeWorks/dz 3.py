#Задача 1
'''
for i in range(int(input("Введи первое число: ")), int(input("Введи второе число: "))): #1-10
    delitel = 2
    povtor = 0
    while delitel < i:
        if i % delitel == 0:
            povtor += 1
        delitel += 1
    if povtor == 0:
        print(i)
'''

#Задача 2
'''
for i in range(1, 10):
    for j in range(1, 11):
        print(i*j, end='\t')
        if j == 10:
            print(end='\n')
'''

#Задача 3
'''
num_1 = int(input("Введи число начала умножения: "))
num_2 = int(input("Введи число конца умножения: "))
for i in range(num_1, num_2+1):
    for j in range(1, 11):
        print(i*j, end='\t')
        if j == 10:
            print(end='\n')
'''