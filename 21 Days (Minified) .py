from save import *
from tkinter import Button,Label,Tk
_B='white'
_A='black'
main=Tk()
main.config(bg=_A)
label=Label(main,text=Num.zfill(2),font=('Helvetica',166,'bold'),fg=_B,bg=_A)
label.grid(pady=500)
dr=int(Num)
def Save():
	global dr;dr-=1
	if dr<1:dr=21
	data=open('save.py','w');data.write(f"Num = str({dr})");data.close();label.config(text=str(dr).zfill(2));exit()
ask=Button(main,text='CHECK',bd=15,command=Save,bg=_A,fg=_B)
ask.grid()
main.mainloop()
