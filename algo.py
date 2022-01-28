import datetime
from operator import itemgetter
from tkinter import *
from tkinter import ttk
from Results import *
# from EnterValues1.build.EnterValues1 import *
from weight_to_percent import *

def calculate(numStockPiles,numSieves,entries,sieve_entries,root,mainroot,wp,pan):
    flag=True
    for i in range(len(entries)):
        if(len(entries[i].get())) == 0:
            flag=False

    for i in range(len(sieve_entries)):
        if(len(sieve_entries[i].get())) == 0:
            flag=False

    if(flag==False):
        messagebox.showerror("Error",  "Please enter all the fields",icon='error')
        return

    temp=0
    data=[]
    td=[]
    if(wp.get()=="Percentage"):
        for ent in entries:
            td.append(float(ent.get()))
            temp += 1
            if(temp==numSieves):
                temp=0
                data.append(td)
                td=[]
    else:
        data=convert(entries,numSieves,pan)


    corData = []
    temp=0
    td=[]
    for ent in sieve_entries:
        td.append(float(ent.get()))
        temp += 1
        if (temp == 2):
            temp = 0
            corData.append(td)
            td = []



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
                    temp += arr[pile]*float(data[pile][sieve])

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

    possibleSolutions=sorted(possibleSolutions,key=itemgetter('Error'))


    b = datetime.datetime.now()
    print("Algo Time",b-a)

    result_fn(root, possibleSolutions, corData, numSieves, numStockPiles,entries,sieve_entries,mainroot)
