from EnterValues3 import Enter_Values3
from EnterValues4 import Enter_Values4


def main_utility(root,numSieves,numStocks,sievegrad,mainroot,wp):
    if(sievegrad.get()=="Other"):
        Enter_Values3(root,numSieves,numStocks,sievegrad,mainroot,wp);
    else:
        Enter_Values4(root, numSieves, numStocks, sievegrad, mainroot,wp);
