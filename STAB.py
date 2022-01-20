import datetime
from operator import itemgetter
from tkinter import *
from tkinter import ttk
from Results import *


splash_root = Tk()
splash_root.title("STAB")
splash_root.geometry("300x300")
splash_label = Label(splash_root, text="Welcome to STAB")
splash_label.pack(pady=20)


def calculate(numStockPiles,numSieves,entries,sieve_entries,root):
    data = [[0] * numStockPiles] * numSieves

    temp=0
    for ent in entries:
        data[int(temp /numStockPiles)][int(temp % numStockPiles)] = float(ent.get())
        temp += 1


    corData = [[0] * 2] * numSieves
    temp=0

    # print(len(corData),len(corData[0]))
    for ent in sieve_entries:
        # print(ent.get(),temp)
        corData[int(temp / 2)][int(temp % 2)] = float(ent.get())
        # print(data[int(temp % numStockPiles.get())][int(temp / numStockPiles.get())], temp)
        temp += 1

    filename=""
    if (int(numStockPiles) == 2):
        filename = './possibilities/p22.txt'
    elif (int(numStockPiles) == 3):
        filename='./possibilities/p33.txt'
    elif (int(numStockPiles) == 4):
        filename='./possibilities/p44.txt'
    elif (int(numStockPiles) == 5):
        filename='./possibilities/p55.txt'

    a = datetime.datetime.now()


    print("Processing...")
    numSolutions=0
    possibleSolutions=[]

    with open(filename) as f:
        contents=f.readline()

        while(contents):
            contents = f.readline()
            contents=contents.rstrip("\n")

            if(contents==""):
                break

            mp=map(int,contents.split(","))
            arr=list(mp)


            val=[]

            # print(type(arr[0]),type(data[0][0]))
            for sieve in range(numSieves):
                temp=0
                for pile in range(numStockPiles):
                    # print(data[sieve][pile])
                    temp += arr[pile]*float(data[sieve][pile])

                val.append(temp/100)

            flag=True

            for i in range(numSieves):
                if(val[i]>corData[i][1] or val[i]<corData[i][0]):
                    flag=False

            if(flag==True):
                numSolutions+=1

                error=0.0
                for sieve in range(numSieves):
                    error+=((corData[sieve][0]+corData[sieve][1])/2 - val[sieve])*((corData[sieve][0]+corData[sieve][1])/2 - val[sieve])
                    # print(error)
                currentSolution={"Solution": arr,"Error":error}
                possibleSolutions.append(currentSolution)


    # print(type(possibleSolutions))

    print(numSolutions)
    possibleSolutions=sorted(possibleSolutions,key=itemgetter('Error'))
    print(len(possibleSolutions))

    if numSolutions>0:
        print("Best Solution")
        print(possibleSolutions[0]['Solution'])
    else:
        print("No solution")

    b = datetime.datetime.now()
    print(b-a)

    result_fn(root,possibleSolutions);
    # newWindow = Toplevel(root)
    # newWindow.geometry("500x500")
    #
    # solution_frame = LabelFrame(newWindow, padx=20, pady=10)
    # solution_frame.pack(padx=10, pady=10, fill=X, expand=1, )
    #
    # # Canvas
    # solutionCanvas = Canvas(solution_frame)
    # solutionCanvas.pack(side=LEFT, fill=X, expand=1)
    #
    # solutionFrame = Frame(solutionCanvas)
    #
    # solutionCanvas.create_window((50, 50), window=solutionFrame, anchor="nw")
    #
    #
    # Label_NumOfStockPiles = Label(newWindow, text="Number of Possible Solutions")
    # Label_NumOfStockPiles.place(relx=0.3, rely=0.4, anchor=CENTER)
    #
    # Label_NumOfStockPiles = Label(newWindow, text=numSolutions)
    # Label_NumOfStockPiles.place(relx=0.8, rely=0.4, anchor=CENTER)
    #
    # Label_NumOfStockPiles = Label(newWindow, text="Best Solution")
    # Label_NumOfStockPiles.place(relx=0.3, rely=0.7, anchor=CENTER)
    #
    #
    #
    # if(numSolutions > 0):
    #     Label_NumOfStockPiles = Label(newWindow, text=possibleSolutions[0]['Solution'])
    #     Label_NumOfStockPiles.place(relx=0.8, rely=0.7, anchor=CENTER)
    # else:
    #     Label_NumOfStockPiles = Label(newWindow, text="NA")
    #     Label_NumOfStockPiles.place(relx=0.8, rely=0.7, anchor=CENTER)








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
