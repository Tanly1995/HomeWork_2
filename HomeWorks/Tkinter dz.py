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

button = Button(text="Apply", width=10, height=1, font=("Chivo Mono", 12))
button.pack(anchor=CENTER, padx=0, pady=250)

name_info = Label(text ="name: ")
name_info.config(font = ('Chivo Mono', 15))
name_info.pack()
name_info.place(x=20, y=500)
surname_info = Label(text="surname: ")
surname_info.config(font = ('Chivo Mono', 15))
surname_info.pack()
surname_info.place(x=20, y=530)
birth_info = Label(text ="birth: ")
birth_info.config(font = ('Chivo Mono', 15))
birth_info.pack()
birth_info.place(x=20, y=560)
telefon_info = Label(text ="telefon: ")
telefon_info.config(font = ('Chivo Mono', 15))
telefon_info.pack()
telefon_info.place(x=20, y=590)

root.mainloop()