from tkinter import *
from tkinter.messagebox import *
import tkinter as tk
import PIL
from random import *

class PinPage(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Money Terminal")
        #        self.master.iconbitmap(default='favicon.ico')
        self.master.config(bg='#faf2d5')
        self.master.geometry('220x100')
        self.master.resizable(False, False)
        self.widgets()

    def Next(self):
        next = self.pin_code.get()
        if next == '1234':
            self.master.withdraw()
            self.new_MainPage = Toplevel(self.master)
            self.mainpage = Viselnik(self.new_MainPage)
        else:
            showinfo(title="Wrong Data", message="Incorrect PIN")

    def Exit(self):
        self.master.withdraw()

    def widgets(self):
        welcome = Label(self.master, text='Enter pin code', font=("Open Sans", 12)).grid(row=1, column=2)

        self.pin_code = Entry(self.master, justify=CENTER, bd=4)
        self.pin_code.grid(row=2, column=2)

        self.btn_next = Button(self.master, text='Next', command=self.Next, font=("Open Sans", 12))
        self.btn_next.grid(row=3, column=1, sticky=W)
        self.btn_exit = Button(self.master, text="Exit", command=self.Exit, font=("Open Sans", 12))
        self.btn_exit.grid(row=3,column=3, sticky=E)

class Viselnik(Frame):

    # Список слов для угадывания
    words = ['python', 'programming', 'computer', 'code', 'algorithm', 'debugging']
    # Количество попыток
    tries = 5
    # Выбор случайного слова
    word = choice(words)
    # Список угаданных букв
    guessed_letters = []

    def __init__(self,master = None):
        super().__init__(master)
        self.master1 = master
        self.master1.title('Виселица')
        self.master1.geometry('800x700')
        self.master1.resizable(False, False)
        self.master1['bg'] = '#DCDCDC'
        self.create_widgets()


    def create_widgets(self):

        self.label_word = Label(self.master1, text=self.get_word_display(), font=('Arial', 20))
        self.label_word.pack()

        self.label_tries = Label(self.master1, text=f'Количество оставшихся попыток: {self.tries}')
        self.label_tries.pack()

        self.label_result = Label(self.master1, text='')
        self.label_result.pack()

        for letter in 'abcdefghijklmnopqrstuvwxyz':
            self.button = Button(self.master1, text=letter,command=lambda alphabet=letter: self.button_click(alphabet))
            self.button.pack(side=LEFT, padx=5, pady=5)

    def get_word_display(self):
        display_word = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                display_word += letter
            else:
                display_word += '_ '
        return display_word

    def button_click(self,letter):
        if letter in self.word:
            self.guessed_letters.append(letter)
            self.label_word.config(text=self.get_word_display())
            if set(self.guessed_letters) == set(self.word):
                self.label_result.config(text='Вы победили!')
        else:
            self.tries -= 1
            self.label_tries.config(text=f'Количество оставшихся попыток: {self.tries}')
            if self.tries == 0:
                self.label_result.config(text=f'Вы проиграли! Загаданное слово: {self.word}')

root = tk.Tk()
pinpage = PinPage(root)
pinpage.mainloop()