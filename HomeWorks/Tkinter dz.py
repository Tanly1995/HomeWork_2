from tkinter import *

root = Tk()
'''root.minsize(600,700)
root.maxsize(600,700)'''
root.resizable(False, False)
root.title("Anketa")
root.geometry('600x700')
anketa = Label(text = "Anketa")
anketa.config(font = ('Chivo Mono', 35, 'bold'))
anketa.pack()
name = Label(text = "Name")
name.config(font = ('Chivo Mono', 17, 'bold'))
name.pack()
name.place(x=60, y=100)
surname = Label(text = "Surname")
surname.config(font = ('Chivo Mono', 17, 'bold'))
surname.pack()
surname.place(x=420, y=100)
birth = Label(text = "Birth Date")
birth.config(font = ('Chivo Mono', 17, 'bold'))
birth.pack()
birth.place(x=60, y=200)
telefon = Label(text = "Telephone Number")
telefon.config(font = ('Chivo Mono', 17, 'bold'))
telefon.pack()
telefon.place(x=340, y=200)
name_entry = Entry(bd=2)
name_entry.place(relx=0.07, rely=0.2)
surname_entry = Entry(bd=2)
surname_entry.place(relx=0.07, rely=0.35)
birth = Entry(bd=2)
birth.place(relx=0.7, rely=0.2)
telefon = Entry(bd=2)
telefon.place(relx=0.65, rely=0.35)


root.mainloop()