from tkinter import *
from tkinter.messagebox import *
import tkinter as tk
from random import *
from PIL import Image, ImageTk

class PinPage(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Poveseniy - The Game")
        self.master.config(bg='#977016')
        self.master.geometry('220x100')
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
        welcome = Label(self.master, text='Enter pin code',bg='#977016' ,font=("Open Sans", 12, "bold")).grid(row=1, column=2)

        self.pin_code = Entry(self.master, justify=CENTER, bd=4)
        self.pin_code.grid(row=2, column=2)

        self.btn_next = Button(self.master, text='Next', command=self.Next, font=("Open Sans", 12))
        self.btn_next.grid(row=3, column=3, sticky=E)
        self.btn_exit = Button(self.master, text="Exit", command=self.Exit, font=("Open Sans", 12))
        self.btn_exit.grid(row=3,column=1, sticky=W)

        root.iconbitmap(default=r"D:\Python works\Lessons\hanged_ico.ico")

class Viselnik(Frame):

    # Список слов для угадывания
    list_words = ['python', 'car', 'computer', 'teacher', 'step', 'helicopter']
    # Количество попыток
    tries = 5
    # Выбор случайного слова
    word = choice(list_words)
    # Список угаданных букв
    guessed_letters = []
    # Количество картинок
    images = [r'D:\Python works\Lessons\ves.png',
              r'D:\Python works\Lessons\ves1.png',
              r'D:\Python works\Lessons\ves2.png',
              r'D:\Python works\Lessons\ves3.png',
              r'D:\Python works\Lessons\ves4.png',
              r'D:\Python works\Lessons\ves5.jpg']

    def __init__(self,master = None):
        super().__init__(master)
        self.master1 = master
        self.master1.title('Poveseniy - The Game')
        self.master1.geometry('800x400')
        self.master1.resizable(False, False)
        self.master1['bg'] = '#977016'
        self.create_widgets()


    def create_widgets(self):

        # Load the image of the hangman
        self.hangman_image = ImageTk.PhotoImage(Image.open(r'D:\Python works\Lessons\ves.png').resize((200, 200)))
        self.label_hangman = Label(self.master1, image=self.hangman_image)
        self.label_hangman.pack()

        self.label_word = Label(self.master1, text=self.get_word_display(),bg='#977016', font=('Open Sans', 20))
        self.label_word.pack()

        self.label_tries = Label(self.master1, text=f'Осталось {self.tries} попыток', bg='#977016')
        self.label_tries.pack()

        self.label_result = Label(self.master1, text='', bg='#977016')
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

    def button_click(self, letter):
        if letter in self.word:
            self.guessed_letters.append(letter)
            self.label_word.config(text=self.get_word_display())
            if set(self.guessed_letters) == set(self.word):
                self.label_result.config(text='Вы победили!', bg='#977016', font=("Open Sans", 12, 'bold'))
        else:
            self.tries -= 1
            self.label_tries.config(text=f'Осталось {self.tries} попыток',font=("Open Sans", 12, 'bold'), bg='#977016' )
            if self.tries == 0:
                self.label_result.config(text=f'Вы проиграли! Слово: {self.word}', font=("Open Sans", 12, 'bold'),bg='#977016')
                # Update the hangman image
                self.hangman_image = ImageTk.PhotoImage(Image.open(self.images[-1]).resize((200, 200)))
                self.label_hangman.config(image=self.hangman_image)
            elif self.tries < 0:
                self.label_tries.config(text=f'Прекрати тыкать',font=("Open Sans", 12, 'bold'))
            else:
                misses = 5 - self.tries
                self.hangman_image = ImageTk.PhotoImage(Image.open(self.images[misses]).resize((200, 200)))
                self.label_hangman.config(image=self.hangman_image)

root = Tk()
mainmenu = PinPage(root)

mainmenu.mainloop()