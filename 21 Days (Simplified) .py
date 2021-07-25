from save import *
from tkinter import Button, Label, Tk

main = Tk()
main.config(bg="black")

label = Label(
    main, text=Num.zfill(2), font=("Helvetica", 166, "bold"), fg="white", bg="black"
)
label.grid(pady=500)

dr = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
]

c = count


def Save():
    global dr, c
    if c == 21:
        c = 0
    c += 1
    data = open("save.py", "w")
    data.write(f"count = {c}\nNum = str({dr[-c]})")
    data.close()
    label.config(text=str(dr[-c].zfill(2)))


ask = Button(main, text="CHECK", bd=15, command=Save, bg="black", fg="white")
ask.grid()
main.mainloop()
