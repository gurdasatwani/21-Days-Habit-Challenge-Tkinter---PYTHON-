from save import *
from tkinter import Button, Label, Tk

main = Tk()
main.config(bg="black")

label = Label(
    main, text=Num.zfill(2), font=("Helvetica", 166, "bold"), fg="white", bg="black"
)
label.grid(pady=500)

dr = int(Num)


def Save():
    global dr
    dr -= 1
    if dr < 1:
        dr = 21
    data = open("save.py", "w")
    data.write(f"Num = str({dr})")
    data.close()
    label.config(text=str(dr).zfill(2))
    exit()


ask = Button(main, text="CHECK", bd=15, command=Save, bg="black", fg="white")
ask.grid()
main.mainloop()
