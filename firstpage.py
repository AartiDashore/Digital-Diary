from Tkinter import *


def main():
    win = Tk()
    win.title("Digital Diary")
    win.geometry('2000x1000')
    h1 = Label(win, text="Welcome To Digital Diary", font=('forte',20,'italic'))
    h1.pack()

    f1 = LabelFrame(win, text = 'Aarti Dashore')
    f1.grid(row=1, column=0)

    l1 = Label(f1, text = 'If already a user, Login')
    l1.grid(row=1, column=0)
    
    win.mainloop()

if __name__ == "__main__":
    main()
