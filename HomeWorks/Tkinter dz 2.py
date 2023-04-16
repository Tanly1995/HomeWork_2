from tkinter import *
from tkinter import ttk

root = Tk()
root.resizable(False, False)
root.title("Registration form")
root.config(background='#D2AC81')
root.geometry('570x500')

registr = Label(text="Registration")
registr.config(font=('Chivo Mono', 23, 'bold'), background='#D2AC81')
registr.place(x=220, y=10)

name_entre = Entry(bd=3)
mail_entre = Entry(bd=3)
age_entre = Entry(bd=3)
name_entre.place(x=240, y=100)
mail_entre.place(x=240, y=150)
age_entre.place(x=240, y=255)

name = Label(text="Full Name")
name.config(font=('Chivo Mono', 14), background='#D2AC81')
name.place(x=100, y=100)

mail = Label(text="Email")
mail.config(font=('Chivo Mono', 14), background='#D2AC81')
mail.place(x=100, y=150)

gender = Label(text="Gender")
gender.config(font=('Chivo Mono', 14), background='#D2AC81')
gender.place(x=100, y=200)

check_2 = Checkbutton(text="Male")
check_2.config(font=('Times new roman', 17), background='#D2AC81')
check_2.place(x=240 ,y=195)

check = Checkbutton(text="Female")
check.config(font=('Times new roman', 17), background='#D2AC81')
check.place(x=330, y=195)

age = Label(text="Age")
age.config(font=('Chivo Mono', 14), background='#D2AC81')
age.place(x=100, y=250)

submit = Button(text="submit")
submit.pack()
submit.config(font=('Times new roman', 17), background='#831A1A', width=20)
submit.place(x= 170, y=340)

root.mainloop()