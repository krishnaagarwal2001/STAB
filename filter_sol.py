from FilterResults import filter_result_fn
from operator import itemgetter

def filter_sol(numStockPiles,numSieves,entries,sieve_entries,root,fix_entries,possibleSolutions,corData,mainroot):
    updatedSolutions=[]
    for i in range(len(possibleSolutions)):
        flag=True
        for j in range(len(fix_entries)):
            if len(fix_entries[j].get()) != 0:
                if (int(possibleSolutions[i]['Solution'][j])!=int(fix_entries[j].get())):
                    flag=False

        if(flag==True):
            updatedSolutions.append(possibleSolutions[i])

    updatedSolutions = sorted(updatedSolutions, key=itemgetter('Error'))
    filter_result_fn(root, updatedSolutions, corData, numSieves, numStockPiles, entries, sieve_entries,mainroot)
