from save import *
from datetime import date,timedelta
from tkinter import Button,Label,Tk,messagebox
_B='white'
_A='black'
main=Tk()
main.config(bg=_A)
dr=int(Num)
check=Checked_Days
skip=Skipped_Days
Split=date(int(Split[0]),int(Split[1]),int(Split[2]))
Date=date.today()
if Date>Split:skip=(Date-Split).days
def Save():
	global dr,check;t=Date+timedelta(1);dr-=1;check+=1
	if dr<1:dr=21
	data=open('save.py','w');data.write(f'Num = str({dr})\nToday = "{t}"\nSplit = Today.split("{"-"}")\nChecked_Days = {check}\nSkipped_Days = {skip}');data.close();label.config(text=str(dr).zfill(2));exit()
label=Label(main,text=Num.zfill(2),font=('Helvetica',169,'bold'),fg=_B,bg=_A)
ask=Button(main,bd=15,bg=_A,fg=_B)
if str(Date)==Today:ask.config(text='CHECK',command=Save)
else:messagebox.showinfo('PROGRESS',f"Check Days = {check}\nSkip Days = {skip}");ask.config(text='EXIT',command=main.destroy)
label.grid(pady=500)
ask.grid()
main.mainloop()
