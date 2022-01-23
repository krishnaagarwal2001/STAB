

from pathlib import Path
from main.main import *
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def splash():

    window = Tk()

    window.geometry("1280x720")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        950.0,
        316.0,
        1095.0,
        378.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        790.0,
        316.0,
        934.0,
        378.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        668.0,
        316.0,
        773.0,
        378.0,
        fill="#FFFFFF",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        320.0,
        400.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        80.0,
        fill="#3888FF",
        outline="")

    canvas.create_text(
        668.0,
        121.0,
        anchor="nw",
        text="STAB Calculator for Stocks",
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
        664.0,
        180.0,
        1095.0,
        291.0,
        fill="#F1F5FF",
        outline="")

    canvas.create_text(
        693.0,
        217.0,
        anchor="nw",
        text="Define Stocks & Sieves.",
        fill="#273340",
        font=("OpenSansRoman Regular", 12 * -1)
    )

    canvas.create_text(
        674.0,
        190.0,
        anchor="nw",
        text="Get Solutions in 3 easy steps:",
        fill="#273340",
        font=("OpenSansRoman Bold", 14 * -1)
    )

    canvas.create_text(
        693.0,
        241.0,
        anchor="nw",
        text="Enter Sieve parameters & corresponding Stock Values.",
        fill="#273340",
        font=("OpenSansRoman Regular", 12 * -1)
    )

    canvas.create_text(
        693.0,
        265.0,
        anchor="nw",
        text="Get the calculated best solution and browse other feasible solutions.",
        fill="#273340",
        font=("OpenSansRoman Regular", 12 * -1)
    )

    canvas.create_rectangle(
        683.0,
        224.0,
        687.0,
        228.0,
        fill="#283341",
        outline="")

    canvas.create_rectangle(
        683.0,
        248.0,
        687.0,
        252.0,
        fill="#283341",
        outline="")

    canvas.create_rectangle(
        683.0,
        272.0,
        687.0,
        276.0,
        fill="#283341",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: main_window(window),
        relief="flat"
    )
    button_1.place(
        x=668.0,
        y=419.0,
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
        x=790.0,
        y=419.0,
        width=108.0,
        height=31.0
    )

    canvas.create_text(
        718.2724609375,
        326.044921875,
        anchor="nw",
        text="1",
        fill="#273340",
        font=("Inter Regular", 11 * -1)
    )

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
        x=733.95458984375,
        y=324.0,
        width=17.04541015625,
        height=17.04541015625
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=691.0,
        y=324.0,
        width=17.04541015625,
        height=17.04541015625
    )

    canvas.create_text(
        674.0,
        351.044921875,
        anchor="nw",
        text="Browse all solutions",
        fill="#273340",
        font=("OpenSansRoman Regular", 10 * -1)
    )

    canvas.create_text(
        798.0,
        353.0,
        anchor="nw",
        text="Get Lower & Upper Bounds",
        fill="#273340",
        font=("OpenSansRoman Regular", 10 * -1)
    )

    canvas.create_rectangle(
        826.0,
        327.0,
        897.0,
        327.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        826.0,
        342.0,
        897.0,
        342.0,
        fill="#000000",
        outline="")

    canvas.create_text(
        958.0,
        351.0,
        anchor="nw",
        text="Utilise all info within graphs",
        fill="#273340",
        font=("OpenSansRoman Regular", 10 * -1)
    )

    canvas.create_text(
        668.0,
        496.0,
        anchor="nw",
        text="Developed by:",
        fill="#3888FF",
        font=("OpenSansRoman Bold", 16 * -1)
    )

    canvas.create_rectangle(
        670.0,
        538.0,
        674.0,
        542.0,
        fill="#283341",
        outline="")

    canvas.create_text(
        678.0,
        532.0,
        anchor="nw",
        text="Dr. Nikhil Saboo",
        fill="#273340",
        font=("OpenSansRoman Regular", 14 * -1)
    )

    canvas.create_rectangle(
        670.0,
        580.0,
        674.0,
        584.0,
        fill="#283341",
        outline="")

    canvas.create_text(
        678.0,
        574.0,
        anchor="nw",
        text="Krishna Agarwal",
        fill="#273340",
        font=("OpenSansRoman Regular", 14 * -1)
    )

    canvas.create_rectangle(
        670.0,
        610.0,
        674.0,
        614.0,
        fill="#283341",
        outline="")
    canvas.create_text(
        678.0,
        604.0,
        anchor="nw",
        text="Sanskar Gahoi",
        fill="#273340",
        font=("OpenSansRoman Regular", 14 * -1)
    )

    canvas.create_rectangle(
        670.0,
        640.0,
        674.0,
        644.0,
        fill="#283341",
        outline="")
    canvas.create_text(
        678.0,
        634.0,
        anchor="nw",
        text="Shubhank",
        fill="#273340",
        font=("OpenSansRoman Regular", 14 * -1)
    )
    canvas.create_rectangle(
        670.0,
        670.0,
        674.0,
        674.0,
        fill="#283341",
        outline="")
    canvas.create_text(
        678.0,
        664.0,
        anchor="nw",
        text="Anurag Yadav",
        fill="#273340",
        font=("OpenSansRoman Regular", 14 * -1)
    )

    canvas.create_text(
        678.0,
        548.0,
        anchor="nw",
        text="Prof., Transportation Engg. Dept., IIT Roorkee",
        fill="#273340",
        font=("OpenSansRoman Regular", 10 * -1)
    )



    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        1022.0,
        335.0,
        image=image_image_4
    )

    canvas.create_text(
        1059.0,
        675.0,
        anchor="nw",
        text="Resources & Documentation",
        fill="#273340",
        font=("OpenSansItalic Regular", 14 * -1)
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        1048.0,
        686.0,
        image=image_image_5
    )

    canvas.create_rectangle(
        1059.0,
        693.0,
        1232.0,
        693.0,
        fill="#000000",
        outline="")
    window.resizable(False, False)
    window.mainloop()
