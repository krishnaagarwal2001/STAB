import datetime
from operator import itemgetter
from tkinter import *
from tkinter import ttk
from Results import *
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from algo import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def Enter_Values3(root,numSieves,numStocks,sievegrad):
    window = Toplevel(root)
    window.geometry("1280x720")
    window.title("STAB")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        80.0,
        fill="#3888FF",
        outline="")

    canvas.create_text(
        63.0,
        121.0,
        anchor="nw",
        text="Enter Values",
        fill="#3888FF",
        font=("Inter Medium", 28 * -1)
    )

    canvas.create_text(
        70.0,
        23.0,
        anchor="nw",
        text="STAB Calculator",
        fill="#FFFFFF",
        font=("Inter Bold", 28 * -1)
    )

    canvas.create_text(
        1176.0,
        28.0,
        anchor="nw",
        text="Version 2.3",
        fill="#FFFFFF",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        1129.0,
        48.0,
        anchor="nw",
        text="All Rights Reserved",
        fill="#FFFFFF",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        63.0,
        99.0,
        anchor="nw",
        text="Define Stocks & Sieves",
        fill="#273340",
        font=("OpenSansRoman Regular", 12 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        194.0,
        108.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        35.0,
        40.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        1118.0,
        55.0,
        image=image_image_3
    )

    canvas.create_rectangle(
        63.0,
        180.0,
        1039.0,
        687.0,
        fill="#F1F5FF",
        outline="")





    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        197.5,
        245.0,
        image=entry_image_1
    )


    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        window,
        text="Calculate",
        borderwidth=0,
        highlightthickness=0,
        bg="#3888FF",
        fg="#FFFFFF",
        command=lambda: calculate(numStocks.get(),sievenum,entries,sieve_entries,window) ,
        relief="flat"
    )
    button_1.place(
        x=1094.0,
        y=184.0,
        width=108.0,
        height=31.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=1094.0,
        y=223.0,
        width=108.0,
        height=31.0
    )

    canvas.create_rectangle(
        20.0,
        124.0,
        48.0,
        152.0,
        fill="#000000",
        outline="")

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=20.0,
        y=124.0,
        width=28.0,
        height=28.0
    )

    ###Upper Lower Bound Blue box###
    canvas.create_rectangle(
        147.0,
        190.0,
        248.0,
        219.0,
        fill="#C1D6FF",
        outline="")
    canvas.create_rectangle(
        256.0,
        190.0,
        357.0,
        219.0,
        fill="#C1D6FF",
        outline="")
    ###Upper Lower Bound Blue box###


    ######Upper Lower Bound######
    canvas.create_text(
        155.0,
        195.0,
        anchor="nw",
        text="Lower Bound",
        fill="#273340",
        font=("OpenSansRoman SemiBold", 12 * -1)
    )

    canvas.create_text(
        264.0,
        195.0,
        anchor="nw",
        text="Upper Bound",
        fill="#273340",
        font=("OpenSansRoman SemiBold", 12 * -1)
    )

    ######Upper Lower Bound######

    #####SIEVE ENTRIES####
    sievenum=numSieves.get()
    if(sievegrad.get()=="BC - 19mm"):
        sievenum=11
    elif(sievegrad.get()=="BC - 13.2mm"):
        sievenum = 10
    elif (sievegrad.get() == "SMA - 13mm"):
        sievenum =9
    elif (sievegrad.get() == "SMA - 19mm"):
        sievenum =10
    elif (sievegrad.get() == "DBM - 37.5mm"):
        sievenum =8
    elif (sievegrad.get() == "DBM - 26.5mm"):
        sievenum =8
    elif (sievegrad.get() == "PQC"):
        sievenum =9
    elif (sievegrad.get() == "DLC"):
        sievenum =12
    elif (sievegrad.get() == "WMM"):
        sievenum = 8
    elif (sievegrad.get() == "WBM"):
        sievenum =12
    sieve_entries = []
    y1=233
    for i in range(sievenum):
        entry_1 = Entry(
            window,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_1.place(
            x=147.0,
            y=y1,
            width=101.0,
            height=22.0
        )
        entry_2 = Entry(
            window,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_2.place(
            x=256.0,
            y=y1,
            width=101.0,
            height=22.0
        )
        sieve_entries.append(entry_1)
        sieve_entries.append(entry_2)
        y1+=30

    array=[]
    if (sievegrad.get() == "BC - 19mm"):
        array=[100,100,90,100,59,79,52,72,35,55,28,44,20,34,15,27,10,20,5,13]
    elif (sievegrad.get() == "BC - 13.2mm"):
        array=[100,100,90,100,70,88,53,71,42,58,34,48,26,38,18,28,12,20,4,10]
    elif (sievegrad.get() == "SMA - 13mm"):
        array=[100,100,90,100,50,75,20,28,16,24,13,21,12,18,10,20,8,12]
    elif(sievegrad.get() == "SMA - 19mm"):
        array=[100,100,90,100,45,70,25,60,20,28,16,24,13,21,12,18,10,20,8,12]
    elif(sievegrad.get() == "DBM - 37.5mm"):
        array=[100,100,95,100,63,93,55,75,38,54,28,42,7,21,2,8]
    elif(sievegrad.get() == "DBM - 26.5mm"):
        array=[100,100,90,100,71,95,56,80,38,54,28,42,7,21,2,8]
    elif (sievegrad.get() == "PQC"):
        array=[]
    elif(sievegrad.get() == "DLC"):
        array=[]
    elif (sievegrad.get() == "WMM"):
        array=[100,100,95,100,60,80,40,60,25,40,15,30,8,22,0,5]
    elif (sievegrad.get() == "WBM"):
        array=[]




    if (sievegrad.get() == "BC - 19mm"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")
    elif (sievegrad.get() == "BC - 13.2mm"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")
    elif (sievegrad.get() == "SMA - 13mm"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")

    elif(sievegrad.get() == "SMA - 19mm"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")

    elif(sievegrad.get() == "DBM - 37.5mm"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")

    elif(sievegrad.get() == "DBM - 26.5mm"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")

    elif (sievegrad.get() == "PQC"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")

    elif(sievegrad.get() == "DLC"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")

    elif (sievegrad.get() == "WMM"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")

    elif (sievegrad.get() == "WBM"):
        for i in range(len(sieve_entries)):
            sieve_entries[i].insert(0,array[i])
            sieve_entries[i].configure(state="disabled")







    #####SIEVE ENTRIES####

    #####Sieve labels#####
    y1=236.0
    for i in range(sievenum):
        canvas.create_text(
            79.0,
            y1,
            anchor="nw",
            text="Sieve"+str(i+1),
            fill="#273340",
            font=("OpenSansRoman Regular", 12 * -1)
        )
        y1+=30


    #####Sieve labels#####

    #####Stock Labels#####
    x1=377.0
    # print(numStocks.get())
    for i in range(numStocks.get()):
        canvas.create_rectangle(
            x1,
            190.0,
            x1+101,
            219.0,
            fill="#C1D6FF",
            outline="")

        canvas.create_text(
            x1+8,
            195.0,
            anchor="nw",
            text="Stock "+str(i+1),
            fill="#273340",
            font=("OpenSansRoman SemiBold", 12 * -1)
        )
        x1 += 109
    #####Stock Labels#####

    #####Creating Entries#####


    entries=[]
    x1 = 377
    for i in range(numStocks.get()):
        y1 = 233
        for j in range(sievenum):
            entry_1 = Entry(
                window,
                bd=0,
                bg="#FFFFFF",
                highlightthickness=0
            )
            # entry_1.insert(0,0)

            entry_1.place(
                x=x1,
                y=y1,
                width=101.0,
                height=22.0
            )
            y1 += 30
            entries.append(entry_1)
        x1 += 109


    #####Creating Entries#####


    window.resizable(False, False)
