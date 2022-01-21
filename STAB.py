import datetime
from operator import itemgetter
from tkinter import *
from tkinter import ttk
from Results import *
from EnterValues1.build.EnterValues1 import *
from algo import *

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

    def openNewWindow():

        newWindow = Toplevel(root)
        newWindow.geometry("800x800")

        frame = Frame(
            newWindow,
            bg='red',
            width=newWindow.winfo_screenwidth(),
            height=newWindow.winfo_screenheight(),
        )
        frame.pack(expand=True,fill="none")

        canvas = Canvas(
            frame,
            bg='#4A7A8C',
            # scrollregion=canvas.bbox("all"),
        )


        vertibar = Scrollbar(
            frame,
            orient=VERTICAL
        )
        vertibar.pack(side=RIGHT, fill=Y)
        vertibar.config(command=canvas.yview)

        horibar = Scrollbar(
            frame,
            orient=HORIZONTAL
        )
        horibar.pack(side=BOTTOM, fill=X)
        horibar.config(command=canvas.xview)

        canvas.config(
            xscrollcommand=horibar.set,
            yscrollcommand=vertibar.set
        )
        canvas.pack(side=TOP, fill="none")
        canvas.configure(scrollregion=canvas.bbox("all"))

        entries = []
        for i in range(numStockPiles.get()):
            Label(canvas, text="Stock" + str(i + 1)).grid(row=0, column=i + 1, pady=20, padx=5)
        for i in range(numSieves.get()):  # A for loop for row entries
            Label(canvas, text="Sieve" + str(i + 1)).grid(row=i + 1, column=0, pady=20, padx=5)
            for j in range(numStockPiles.get()):  # A for loop for column entries
                ent = Entry(canvas)
                ent.grid(row=i + 1, column=j + 1, pady=20, padx=5)
                # print(ent.get())
                entries.append(ent)

        sieve_entries = []
        Label(canvas, text="Lower Bound").grid(row=numSieves.get()+1, column=1, pady=20, padx=5)
        Label(canvas, text="Upper Bound").grid(row=numSieves.get()+1, column=2, pady=20, padx=5)

        for i in range(numSieves.get()):  # A for loop for row entries
            Label(canvas, text="Sieve" + str(i + 1)).grid(row=numSieves.get()+1+i + 1, column=0, pady=20, padx=5)
            for j in range(2):  # A for loop for column entries
                ent = Entry(canvas)
                ent.grid(row=i + 1+numSieves.get()+1, column=j + 1, pady=20, padx=5)
                sieve_entries.append(ent)

        temp = 0

        Button(canvas, text="Calculate", command=lambda:calculate(numStockPiles.get(),numSieves.get(),entries,sieve_entries,newWindow)).grid(row=2*numSieves.get()+3,column=int((numStockPiles.get()+1)/2))




    Button(root, text="Enter", command=openNewWindow).place(relx=0.5, rely=0.8, anchor=CENTER)


splash_root.after(1500, main_window)

mainloop()
