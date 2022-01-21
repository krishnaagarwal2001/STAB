import datetime
from operator import itemgetter
from tkinter import *
from tkinter import ttk
from Results import *
from EnterValues1.build.EnterValues1 import *


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

    result_fn(root, possibleSolutions, corData, numSieves, numStockPiles);