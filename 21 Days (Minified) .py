from save import *
from datetime import date,timedelta
from tkinter import Button,Label,Tk
_B='white'
_A='black'
main=Tk()
main.config(bg=_A)
dr=int(Num)
def Save():
	global dr;t=date.today()+timedelta(1);dr-=1
	if dr<1:dr=21
	data=open('save.py','w');data.write(f'Num = str({dr})\ntoday = "{t}"');data.close();label.config(text=str(dr).zfill(2));exit()
label=Label(main,text=Num.zfill(2),font=('Helvetica',166,'bold'),fg=_B,bg=_A)
ask=Button(main,text='CHECK',bd=15,command=Save,bg=_A,fg=_B)
if str(date.today())==today:ask.config(state='normal')
else:ask.config(state='disable')
label.grid(pady=500)
ask.grid()
main.mainloop()
