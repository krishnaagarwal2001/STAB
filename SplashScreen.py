from main import *
import webbrowser
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage,messagebox

def openpdf():
    path="Manual.pdf"
    webbrowser.open_new(path)


def splash():
    window = Tk()
    screen_width=window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    app_width=1280
    app_height=720
    x=(screen_width/2)-(app_width/2)
    y=(screen_height/2)-(app_height/2)-30
    window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    window.title("STAB")
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
        file="assets\main_pic.png")
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
        70.0,
        23.0,
        anchor="nw",
        text="STAB",
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

    image_image_2 = PhotoImage(
        file="assets/IITR_Logo.png")
    image_2 = canvas.create_image(
        35.0,
        40.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file="assets\copyright.png")
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
        text="Define stockpiles & sieves.",
        fill="#273340",
        font=("OpenSansRoman Regular", 12 * -1)
    )

    canvas.create_text(
        674.0,
        190.0,
        anchor="nw",
        text="Get solutions in 3 easy steps:",
        fill="#273340",
        font=("OpenSansRoman Bold", 14 * -1)
    )

    canvas.create_text(
        693.0,
        241.0,
        anchor="nw",
        text="Enter sieve parameters & corresponding stockpile values.",
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
        file="assets/start_button.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: main_window(window,window),
        relief="flat"
    )
    button_1.place(
        x=668.0,
        y=419.0,
        width=108.0,
        height=31.0
    )

    button_image_2 = PhotoImage(
        file="assets/read_manual_button.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: openpdf(),
        relief="flat"
    )
    button_2.place(
        x=790.0,
        y=419.0,
        width=108.0,
        height=31.0
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

    canvas.create_text(
        678.0,
        548.0,
        anchor="nw",
        text="Faculty, Civil Engg. Dept., IIT Roorkee",
        fill="#273340",
        font=("OpenSansRoman Regular", 10 * -1)
    )

    canvas.create_rectangle(
        670.0,
        590.0,
        674.0,
        594.0,
        fill="#283341",
        outline="")

    canvas.create_text(
        678.0,
        584.0,
        anchor="nw",
        text="Anurag Yadav",
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
        text="Krishna Agarwal",
        fill="#273340",
        font=("OpenSansRoman Regular", 14 * -1)
    )

    canvas.create_rectangle(
        670.0,
        630.0,
        674.0,
        634.0,
        fill="#283341",
        outline="")
    canvas.create_text(
        678.0,
        624.0,
        anchor="nw",
        text="Sanskar Gahoi",
        fill="#273340",
        font=("OpenSansRoman Regular", 14 * -1)
    )
    canvas.create_rectangle(
        670.0,
        650.0,
        674.0,
        654.0,
        fill="#283341",
        outline="")
    canvas.create_text(
        678.0,
        644.0,
        anchor="nw",
        text="Shubhank",
        fill="#273340",
        font=("OpenSansRoman Regular", 14 * -1)
    )

    canvas.create_text(
        678.0,
        660.0,
        anchor="nw",
        text="UG Students, Civil Engg. Dept., IIT Roorkee",
        fill="#273340",
        font=("OpenSansRoman Regular", 10 * -1)
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
        file="assets/resources.png")
    image_5 = canvas.create_image(
        1048.0,
        686.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file="assets/heading.png")
    image_6 = canvas.create_image(
        900.0,
        140.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file="assets/frame1.png")
    image_7 = canvas.create_image(
        717.0,
        346.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file="assets/frame2.png")
    image_8 = canvas.create_image(
        842.0,
        346.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file="assets/frame3.png")
    image_9 = canvas.create_image(
        967.0,
        346.0,
        image=image_image_9
    )

    image_image_10 = PhotoImage(
        file="assets/filter_mini.png")
    image_10 = canvas.create_image(
        841.0,
        333.0,
        image=image_image_10
    )


    canvas.create_rectangle(
        1059.0,
        693.0,
        1232.0,
        693.0,
        fill="#000000",
        outline="")

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.resizable(False, False)
    window.mainloop()
