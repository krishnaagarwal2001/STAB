import datetime
from operator import itemgetter
from tkinter import *
from tkinter import ttk
from Results import *
# from .EnterValues1.build.EnterValues1 import *
from EnterValues3.build.EnterValues3 import *

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

    print(data)

    corData = [[0] * 2] * numSieves
    temp=0
    print(len(corData),len(corData[0]))

    for ent in sieve_entries:

        corData[int(temp/2)][int(temp % 2)] = float(ent.get())

        # print(temp, ent.get(),int(temp/2),int(temp%2),corData[int(temp / 2)][int(temp % 2)],corData[0][0],corData[0][1],corData[1][0])

        temp += 1

    print(temp)
    # temp=0;
    # for ent in sieve_entries:
    #     print(ent.get(), corData[int(temp / 2)][int(temp % 2)])
    #     if(corData[int(temp / 2)][int(temp % 2)]!=float(ent.get())):
    #         print("False")
    #     temp += 1

    print("cordata",corData[0][0])
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
                currentSolution={"Solution": arr,"Error":error,"val":val}
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

    result_fn(root,possibleSolutions,corData,numSieves,numStockPiles);







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
