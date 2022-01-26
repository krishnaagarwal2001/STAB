from Results import result_fn
from EnterValues3.build.EnterValues3 import *

def result_utility(numStockPiles,numSieves,entries,sieve_entries,root,mainroot,wp):
    if(wp.get()=="Weight"):
        print("HELL")
        j=0
        temp=0
        sum=0
        for i in range(len(entries)):
            sum+=float(entries[i].get())
            temp+=1
            if(temp==numSieves):
                temp_sum=sum
                for k in range(j,numSieves):
                    temp_sum-=float(entries[k].get())
                    print(float(temp_sum*100)/float(sum))
                    entries[k].insert(0,float(temp_sum*100)/float(sum))
                sum=0
                temp=0
                j+=numSieves

    for i in range(len(entries)):
        print(entries[i].get(),type(entries[i].get()))

    calculate(numStockPiles, numSieves, entries, sieve_entries, root, mainroot)