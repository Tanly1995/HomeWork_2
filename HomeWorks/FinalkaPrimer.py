from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from PIL import Image, ImageTk

class LoginWindow(Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.master.title('Login Window')
        self.master.iconbitmap(default='favicon.ico')
        self.master.config(bg = '#faf2d5')
        self.master.resizable(False,False)
        self.create_widgets()


    def create_widgets(self):
        lbl_login = Label(self.master,text= 'Login: ').grid(row= 0)
        lbl_password = Label(self.master,text= 'Password: ').grid(row=1)

        self.user_login = Entry(self.master,bd = 3)
        self.user_login.grid(row = 0, column= 1)
        self.user_password = Entry(self.master,bd = 3,show = '*')
        self.user_password.grid(row=1, column=1)

        self.btn_login = ttk.Button(self.master,text='Login',command= self.login)
        self.btn_login.grid(row = 2, column=2, columnspan= 3)

        self.exit_btn = Button(self.master, text ='Exit',command = self.exit)
        self.exit_btn.grid(row = 2, column=0,sticky=NW)


    def exit(self):
        self.master.withdraw()

    def login(self):
        login = self.user_login.get()
        password = self.user_password.get()

        if login == 'Lego' and password == '12345':
            self.master.withdraw()
            self.new_InfoWindow = Toplevel(self.master)
            self.info_window = InfoWindow(self.new_InfoWindow)
        else:
            showinfo(title = 'Wrong Data', message = 'Wrong password or login')

class InfoWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Info Window')
        self.master.geometry('400x200')
        self.master.resizable(False, False)
        self.create_widgit()

    def create_widgit(self):
        img = Image.open('')
        self.resized_img = img.resize((300, 100))
        self.new_img = ImageTk.PhotoImage(self.resized_img)

        lbl = Label(self.master,text = 'You hacked my data', font = 'Arial 38 bold italic underline',image=self.new_img)
        lbl.grid(row = 0,column= 0)



if __name__ == '__main__':
    root =Tk()
    app = LoginWindow(root)
    app.mainloop()