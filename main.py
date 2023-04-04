from pickle import dump, load
#car = "Tesla"
#year = 2016
#with open(r"C:\Users\salmanov_o\PycharmProjects\39-40 lesson\test.doc", "wb") as fileHandler:
#    dump(car, fileHandler)
#    dump(year, fileHandler)
#
#with open(r"C:\Users\salmanov_o\PycharmProjects\39-40 lesson\test.doc", "rb") as fileHandler:
#    print(load(fileHandler))
#    second = load(fileHandler)
#    print(f"{type(second)} this type has value = {second}")


#doc_file = r"C:\Users\salmanov_o\PycharmProjects\39-40 lesson\test.doc"
'''
car = ["BMW", "Rolls Royce", "Porshe", "Bugatti"]
cars_info = [["BMW", "m5", 2022, 2.8],
             ["Rolls-Royce","GHOST", 2020, 4.5],
             ["Porshe", "Taycan", 2019, 2.7],
             ['Bugatti',"Chiron", 2018, 2.1]]

with open(doc_file, "wb") as fileHandler:
    for i in cars_info:
        dump(i, fileHandler)

with open(doc_file, "rb") as fileHandler:
    for i in range(len(cars_info)-1):
        print(load(fileHandler))
        for j in cars_info[i]:
            print(load(fileHandler))'''

#1. Поиск и замена слов списка в содержимом бинарного файла
#2. Подсчет количества слов и чисел(по отдельности) в содержимом бинарного файла
#3. Вывести слова спрятанные за ключами в словае в содержимом бинарном файле

spisok = ["car", "meal", "animal"]
with open(r"C:\Users\salmanov_o\PycharmProjects\39-40 lesson\samost.doc", "wb") as fileHandler:
    dump(spisok, fileHandler)

with open(r"C:\Users\salmanov_o\PycharmProjects\39-40 lesson\samost.doc", "rb") as fileHandler:
    print(load(fileHandler))

zamena_slovo = input("какое слово заменить: ")
zamena = input("на что заменить: ")

with open(r"C:\Users\salmanov_o\PycharmProjects\39-40 lesson\samost.doc", "wb") as fileHandler:
    for i in spisok:
        if i == zamena_slovo:
            spisok[spisok.index(i)] = zamena

with open(r"C:\Users\salmanov_o\PycharmProjects\39-40 lesson\samost.doc", "rb") as file:
     print(load(file))

#-----------------------------------
