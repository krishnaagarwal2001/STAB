import datetime
from operator import itemgetter
from tkinter import *
from tkinter import ttk
from Results import *
from algo import *
from EnterValues3.build.EnterValues3 import *

splash_root = Tk()
splash_root.title("STAB")
splash_root.geometry("300x300")
splash_label = Label(splash_root, text="Welcome to STAB")
splash_label.pack(pady=20)


def main_window():
    splash_root.destroy()
    root = Tk()
    root.geometry("300x300")
    root.minsize(300, 300)
    root.maxsize(300, 300)

    Label_NumOfStockPiles = Label(root, text="Number of Stock Piles")
    Label_NumOfStockPiles.place(relx=0.3, rely=0.2, anchor=CENTER)

    numStockPiles = IntVar()
    numStockPiles.set(2)
    OptionMenu(root, numStockPiles, 2, 3, 4, 5).place(relx=0.8, rely=0.2, anchor=CENTER)

    Label_NumOfSieves = Label(root, text="Number of Sieves")
    Label_NumOfSieves.place(relx=0.3, rely=0.5, anchor=CENTER)

    numSieves = IntVar()
    numSieves.set(1)
    OptionMenu(root, numSieves, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12).place(relx=0.8, rely=0.5, anchor=CENTER)


        # Button(canvas, text="Calculate", command=lambda:calculate(numStockPiles.get(),numSieves.get(),entries,sieve_entries,newWindow)).grid(row=2*numSieves.get()+3,column=int((numStockPiles.get()+1)/2))

    # print(numSieves.get(),numStockPiles.get())
    Button( text="Enter", command=lambda: Enter_Values3(root,numSieves,numStockPiles)).place(relx=0.5, rely=0.8, anchor=CENTER)


splash_root.after(1500, main_window)

mainloop()
