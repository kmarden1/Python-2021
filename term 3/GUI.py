from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.bttn_clicks = 0
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.lbl = Label(self, text="YOU HAVE CLICKED THE BUTTON " + str(self.bttn_clicks) + " TIMES")
        self.lbl.grid()

        self.bttn1 = Button(self, text="add to count")
        self.bttn1.grid()
        self.bttn1["command"] = self.add_to_count

        Label(self, text="THIS IS BUTTON 2")
        self.grid()
        self.bttn2 = Button(self, text = "minus to count")
        self.bttn2.grid()
        self.bttn2["command"] = self.minus_to_count

        Label(self, text="THIS IS BUTTON 3")
        self.grid()
        self.bttn3 = Button(self, text = "reset count" )
        self.bttn3.grid()
        self.bttn3["command"] = self.reset_count

        Label(self, text="THIS IS BUTTON 4")
        self.grid()
        self.bttn4 = Button(self, text="Do not press")
        self.bttn4.grid()
        self.bttn4["command"] = self.quit_program

    def add_to_count(self):
        """Increase click count and display new total """
        self.bttn_clicks += 2
        self.lbl.config(text="YOU HAVE CLICKED THE BUTTON " + str(self.bttn_clicks) + " TIMES")
        if self.bttn_clicks >= 0:
            self.lbl.config(bg="green")
        else:
            self.lbl.config(bg="red")

    def minus_to_count(self):
        """Subtract"""
        self.bttn_clicks -= 2
        self.lbl.config(text="YOU HAVE CLICKED THE BUTTON " + str(self.bttn_clicks) + " TIMES")
        if self.bttn_clicks >= 0:
            self.lbl.config(bg="green")
        else:
            self.lbl.config(bg="red")

    def reset_count(self):
        """does nothing"""
        self.bttn_clicks = 0
        self.lbl.config(text="YOU HAVE CLICKED THE BUTTON " + str(self.bttn_clicks) + " TIMES")
        if self.bttn_clicks >= 0:
            self.lbl.config(bg="green")
        else:
            self.lbl.config(bg="red")

    def quit_program(self):
        """does nothing"""
        self.bttn_clicks = 0
        self.lbl.config(text="YOU HAVE CLICKED THE BUTTON " + str(self.bttn_clicks))
        if self.bttn_clicks >= 0:
            quit()


def main():
    root = Tk()
    root.title("HAHAHA")
    root.geometry("1000x1000")
    app = Application(root)
    root.mainloop()


main()


from tkinter import *

root = Tk()
root.geometry("1000x1000")
root.title("window exe")

top = Frame(root, bg="moccasin", heigth=100, width=400)
top.pack()

mid = Frame(root, bg="yellow",heigth=100,width=400)
mid.pack()

bot = Frame(root, bg="yellow",heigth=100,width=400)
bot.pack()

#topgrid = Frame(root, heigth = 250, width = 250)
#topgrid.pack()
#topleft = Frame(topgrid, heigth = 250, width = 250, bg="yellow")
#topleft.pack(side=LEFT)
#topright.pack(side=LEFT)
#brbttn = Button(topright,text= "button")
#brbttn.pack(padx=102,pady=90)
#botright = Frame(topgrid, heigth = 250, width = 250, bg="green")
#botright.pack(side=LEFT)
#topright.pack(side=LEFT)
#trbttn = Button(botright,text = "button")
#trbttn.pack(padx = 102, pady = 90)


#botgrid = Frame(root, heigth = 250, width = 250)
#botgrid.pack()
#botleft = Frame(botgrid, heigth = 250, width = 250, bg="red")
#botleft.pack(side=LEFT)
#topright.pack(side=LEFT)
#brbttn = Button(botleft,text= "button")
#brbttn.pack(padx=102,pady=90)
#botright = Frame(botgrid, heigth = 250, width = 250, bg="blue")
#botright.pack(side=LEFT)
#topright.pack(side=LEFT)
#blbttn = Button(botright,text = "button")


root.mainloop()

from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.bttn_clicks = 0
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.lbl = Label(self, text="YOU HAVE CLICKED THE BUTTON " + str(self.bttn_clicks) + " TIMES")
        self.lbl.grid()

        self.bttn1 = Button(self, text="add to count")
        self.bttn1.grid()
        self.bttn1["command"] = self.add_to_count

        Label(self, text="THIS IS BUTTON 2")
        self.grid()
        self.bttn2 = Button(self, text = "minus to count")
        self.bttn2.grid()
        self.bttn2["command"] = self.minus_to_count

        Label(self, text="THIS IS BUTTON 3")
        self.grid()
        self.bttn3 = Button(self, text = "reset count" )
        self.bttn3.grid()
        self.bttn3["command"] = self.reset_count

    def add_to_count(self):
        """Increase click count and display new total """
        self.bttn_clicks += 1
        self.lbl.config(text="YOU HAVE CLICKED THE BUTTON " + str(self.bttn_clicks) + " TIMES")
        if self.bttn_clicks >= 0:
            self.lbl.config(bg="green")
        else:
            self.lbl.config(bg="red")

    def minus_to_count(self):
        """Subtract"""
        self.bttn_clicks -= 2
        self.lbl.config(text="YOU HAVE CLICKED THE BUTTON " + str(self.bttn_clicks) + " TIMES")
        if self.bttn_clicks >= 0:
            self.lbl.config(bg="green")
        else:
            self.lbl.config(bg="red")

    def reset_count(self):
        """does nothing"""
        self.bttn_clicks = 0
        self.lbl.config(text="YOU HAVE CLICKED THE BUTTON " + str(self.bttn_clicks) + " TIMES")
        if self.bttn_clicks >= 0:
            self.lbl.config(bg="green")
        else:
            self.lbl.config(bg="red")



def main():
    root = Tk()
    root.title("HAHAHA")
    root.geometry("1000x1000")
    app = Application(root)
    root.mainloop()


main()
