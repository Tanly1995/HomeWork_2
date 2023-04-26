from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *


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
            self.mainpage = MainPage(self.new_MainPage)
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


class MainPage(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Choose Option")
        self.master.iconbitmap()
        self.master.geometry('400x400')
        self.master.config(bg='#faf2d5')

    def wigit(self):
        lbl = Label(self.master, text="Chose option", font="Open Sans")
        lbl.grid(row=0, column=0)


if __name__ == "__main__":
    root = Tk()
    app = PinPage(root)
    app.mainloop()