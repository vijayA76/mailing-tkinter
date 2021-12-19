import tkinter as tk
from tkinter import messagebox
import smtplib
import time

root=tk.Tk()
root.geometry('495x370+430+150')
root.resizable(False,False)
root.title('E-Mail')

T=tk.Label(root,text='Mailing-Box',fg='black',font=('Georgia',15,'bold')).place(x=180,y=5)
t=tk.Label(root,text='From :',fg='black',font=('Georgia',10,'bold')).place(x=5,y=45)
p=tk.Label(root,text='Password :',fg='black',font=('Georgia',10,'bold')).place(x=278,y=45)
f=tk.Label(root,text='To :',fg='black',font=('Georgia',10,'bold')).place(x=5,y=75)
s=tk.Label(root,text='Subject :',fg='black',font=('Georgia',10,'bold')).place(x=5,y=105)

fro=tk.Entry(root,width=34)
fro.place(x=70,y=45)

pas=tk.Entry(root,width=19,show="*")
pas.place(x=359,y=45)

to=tk.Entry(root,width=68)
to.place(x=70,y=75)

sub=tk.Entry(root,width=68)
sub.place(x=70,y=105)

inp=tk.Text(root,height=10,width=59)
inp.place(x=5,y=135)

def show():
    if tick.get()==1:
        pas.configure(show="")
    elif tick.get()==0:
        pas.configure(show="*")
        
tick=tk.IntVar()
cb = tk.Checkbutton(root, command = show, offvalue = 0, onvalue = 1, variable = tick)
cb.place(x = 465, y = 45)

def send():
    try:
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()

        sender=fro.get()
        password=str(pas.get())
        reciever=to.get()
        data='SUBJECT:'+str(sub.get())+'\n'+str(inp.get('1.0','end'))
    
        s.login(sender,password)
        s.sendmail(sender,reciever,data)
        s.quit()
        messagebox.showinfo('Mail',' Send Successfully')
    except:
        messagebox.showerror('error','check your internet \nconnection or gmail \nsetting(less secure app access)')
        
def discard():
    fro.delete(0,'end')
    pas.delete(0,'end')
    to.delete(0,'end')
    sub.delete(0,'end')
    inp.delete("1.0","end")
    
    
sent=tk.Button(root,text='SEND',command=send)
sent.place(x=5,y=320)
dis=tk.Button(root,text='DISCARD',command=discard)
dis.place(x=60,y=320)

