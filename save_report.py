from _csv import writer
import pathlib
from tkinter.filedialog import asksaveasfile


def saveresults(possibleSolution,numSieves,numStocks):
    lab=[]
    for i in range(numStocks):
        lab.append("StockPile "+str(i+1))
    lab.append("Error")

    sv=[]
    for i in range(len(possibleSolution)):
        t=[]
        for j in range(numStocks):
            t.append(possibleSolution[i]['Solution'][j])
        t.append(possibleSolution[i]['Error'])
        sv.append(t)

    data = [('csv files', '*.csv')]
    filed = asksaveasfile(filetypes=data, defaultextension=data)
    try:
        with open(filed.name,"w",newline="") as file:
            Writer=writer(file)
            Writer.writerow(lab)
            Writer.writerows(sv)
    except:
        print("Please create file")