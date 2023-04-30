
from random import *
from tkinter import *
from PIL import ImageTk, Image

class MainMenu(Frame):

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

        # Load the image of the hangman
        self.hangman_image = ImageTk.PhotoImage(Image.open("hangman.png").resize((200, 200)))
        self.label_hangman = Label(self.master1, image=self.hangman_image)
        self.label_hangman.pack()

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

    def button_click(self, letter):
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
                # Update the hangman image
                self.hangman_image = ImageTk.PhotoImage(Image.open(f"hangman_{6 - self.tries}.png").resize((200, 200)))
                self.label_hangman.config(image=self.hangman_image)
            else:
                # Update the hangman image
                self.hangman_image = ImageTk.PhotoImage(Image.open(f"hangman_{6 - self.tries}.png").resize((200, 200)))
                self.label_hangman.config(image=self.hangman_image)

root = Tk()
mainmenu = MainMenu(root)

mainmenu.mainloop()