
import datetime
from operator import itemgetter
from tkinter import *
from tkinter import ttk, messagebox
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

from back_utility import back_utl
from filter_sol import filter_sol
from save_report import *
import numpy as np



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def fix(root,possibleSolutions,corData,numSieves,numStockPiles,entries,sieve_entries,mainroot):
    a = datetime.datetime.now()
    numsol=len(possibleSolutions)
    root.withdraw()
    window =Toplevel(root)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    app_width = 1280
    app_height = 720
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)-30
    window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    window.title("FIX")
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
        66.0,
        247.0,
        1214.0,
        659.0,
        fill="#F1F5FF",
        outline="")

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
        text="Result",
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
        text="Version 2.0",
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
        989.0,
        263.0,
        anchor="nw",
        text="Legends/Instructions:",
        fill="#273340",
        font=("OpenSansRoman Regular", 16 * -1)
    )

    canvas.create_text(
        82.0,
        259.0,
        anchor="nw",
        text="Values",
        fill="#273340",
        font=("OpenSansRoman Regular", 16 * -1)
    )

    canvas.create_text(
        63.0,
        99.0,
        anchor="nw",
        text="Define StockPiles & Sieves",
        fill="#273340",
        font=("OpenSansRoman Regular", 12 * -1)
    )

    canvas.create_text(
        227.0,
        99.0,
        anchor="nw",
        text="Enter Values",
        fill="#273340",
        font=("OpenSansRoman Regular", 12 * -1)
    )

    canvas.create_text(
        342.0,
        259.0,
        anchor="nw",
        text="Graph",
        fill="#273340",
        font=("OpenSansRoman Regular", 16 * -1)
    )

    # Graph Canvas
    canvas.create_rectangle(
        342.0,
        291.0,
        937.0,
        643.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        636.0,
        678.0,
        anchor="nw",
        text="1",
        fill="#273340",
        font=("Inter Regular", 16 * -1)
    )

    image_image_1 = PhotoImage(
        file="assets/next_write.png")
    image_1 = canvas.create_image(
        215.0,
        107.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file="assets/IITR_Logo.png")
    image_2 = canvas.create_image(
        35.0,
        40.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file="assets/copyright.png")
    image_3 = canvas.create_image(
        1118.0,
        55.0,
        image=image_image_3
    )

    image_4 = canvas.create_image(
        301.0,
        107.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file="assets/back_button.png")
    button_1 = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_utl(root, window),
        relief="flat"
    )
    button_1.place(
        x=20.0,
        y=124.0,
        width=28.0,
        height=28.0
    )

    button_image_2 = PhotoImage(
        file="assets/filter_by_fixing_button.png")
    button_2 = Button(
        window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: filter_sol(numStockPiles,numSieves,entries,sieve_entries,window,fix_entries,possibleSolutions,corData,mainroot),
        relief="flat"
    )
    button_2.place(
        x=183.0,
        y=385 + (numStockPiles - 1) * 37.0,
        width=108.0,
        height=31.0
    )

    canvas.create_text(
        1001.0,
        296.0,
        anchor="nw",
        text="Please use percentage values",
        fill="#273340",
        font=("OpenSansRoman Regular", 14 * -1)
    )

    canvas.create_text(
        1001.0,
        323.0,
        anchor="nw",
        text="Graph is to scale of such.",
        fill="#273340",
        font=("OpenSansRoman Regular", 14 * -1)
    )

    canvas.create_rectangle(
        82.0,
        296.0,
        184.0,
        325.0,
        fill="#C1D6FF",
        outline="")



    canvas.create_rectangle(
        188.0,
        296.0,
        290.0,
        325.0,
        fill="#C1D6FF",
        outline="")



    canvas.create_text(
        90.0,
        301.0,
        anchor="nw",
        text="Stock",
        fill="#273340",
        font=("OpenSansRoman Regular", 14 * -1),
        width=325.0,
    )

    canvas.create_text(
        196.0,
        301.0,
        anchor="nw",
        text="Percentage",
        fill="#273340",
        font=("OpenSansRoman Regular", 14 * -1)
    )




    canvas.create_text(
        78.0,
        175.0,
        anchor="nw",
        text="No. of Possible Solutions:",
        fill="#273340",
        font=("OpenSansRoman Regular", 18 * -1)
    )

    canvas.create_rectangle(
        66.0,
        185.0,
        72.0,
        191.0,
        fill="#000000",
        outline="")

    if(numsol>0):
        canvas.create_text(
            300.0,
            173.0,
            anchor="nw",
            text=numsol,
            fill="#273340",
            font=("OpenSansRoman SemiBold", 20 * -1)
        )
    else:
        canvas.create_text(
            300.0,
            173.0,
            anchor="nw",
            text="No Solution Possible",
            fill="#FF5A5A",
            font=("OpenSansRoman SemiBold", 20 * -1)
        )


    canvas.create_text(
        78.0,
        212.0,
        anchor="nw",
        text="Best Solution",
        fill="#273340",
        font=("OpenSansRoman Regular", 18 * -1)
    )

    canvas.create_rectangle(
        66.0,
        222.0,
        72.0,
        228.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        991.0,
        304.0,
        995.0,
        308.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        991.0,
        331.0,
        995.0,
        335.0,
        fill="#000000",
        outline="")



    if (numsol > 0):
        x1 = 82
        x2 = 188
        x3=184
        x4=290
        y1 = 333
        y2=362
        fix_entries=[]
        print(type(canvas))
        for i in range(0, numStockPiles):
            # print(x1,y1)
            canvas.create_rectangle(
                x1,
                y1,
                x3,
                y2,
                fill="#FFFFFF",
                outline="")

            # print(x1+8,y1+2)
            canvas.create_text(
                x1 + 8,
                y1 + 6,
                anchor="nw",
                text="Stock " + str(i + 1),
                fill="#283341",
                font=("OpenSansRoman Regular", 14 * -1),
                width=325.0,
            )


            # print(x2+8,y1+2)
            entry_1 = Entry(
                window,
                bd=0,
                bg="#FFFFFF",
                highlightthickness=0
            )
            entry_1.place(
                x=x2,
                y=y1,
                width=102.0,
                height=29.0
            )
            y1 += 37
            y2+=37
            fix_entries.append(entry_1)

    b = datetime.datetime.now()
    print(b-a)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            mainroot.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.resizable(False, False)
    window.mainloop()

