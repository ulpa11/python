import tkinter
from tkinter import *
def fun():
    info = e1.get()
    a=info.split()
    num=[]
    for i in range(len(a)):
        b=a[i]
        if b.isdigit():
            num.append(int(b))

    if 'add'  in a or 'addition'  in a:
        r=num[0]+num[1]
        result['text']=r

    elif 'subtract' in a or 'subtraction'  in a:
        r=num[0]-num[1]
        result['text']=r

    elif 'multiply' in a or 'multiplication'  in a:
        r=num[0]*num[1]
        result['text']=r

    elif 'divide' in a or 'division'  in a:
        r=num[0]/num[1]
        result['text']=r

    elif 'mod' in a or 'modulous'  in a:
        r=num[0]%num[1]
        result['text']=r

    else:
        result['text']='error'


win=Tk()
win.geometry('400x400')
win.title('smart bugger')
win.config(bg='black')
l1=Label(win,text='I am a Smart calculator',width=20,padx=3)
l1.place(x=123,y=30)
l2=Label(win,text='My name is Pagger',padx=3)
l2.place(x=145,y=70)
l3=Label(win,text='How can i help you',padx=3)
l3.place(x=145,y=150)

e1=Entry(win,width=30)
e1.place(x=110,y=180)


b1=Button(win,text='Just this',borderwidth=10,command=fun)
b1.place(x=170,y=210)

result=Label(win,width=20,height=3,bg='white')
result.place(x=130,y=260)
win.mainloop()
