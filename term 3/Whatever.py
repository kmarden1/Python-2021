from tkinter import *

class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgits()

    def create_widgits(self):
        self.lbl = Label(self, text="Enter password to get access to the meaning of life!")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        self.lblpw = Label(self, text="Password:")
        self.lblpw.grid(row=1, column=0, sticky=W)

        self.password = Entry(self)
        self.password.grid(row=1, column=1, columnspan=2)

        self.submit_bttn = Button(self, text="Submit", command = self.reveal)
        self.submit_bttn.grid(row = 2, column=0, columnspan = 2)

        self.reply_txt = Text(self, width=35, height=20, wrap=WORD)
        self.reply_txt.grid(row=3, column=0, columnspan=2)

        self.move_lbl = Label(self, text="What type of movies do you like?")
        self.move_lbl.grid(row=2)

    def reveal(self):
        enter_pw = self.password.get()
        if enter_pw == "password":
            message = "The Meaning of life is! \n\t\t\t\t\t >>> (42) <<<"
        else:
            message = "you don't need to know"

        self.reply_txt.delete(0.0,END)
        self.reply_txt.insert(0.0,message)


def main():
    root = Tk()
    root.title("password exe")
    app = Application(root)
    root.mainloop()
main()
