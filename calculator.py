from tkinter import*

# 
fount=("arial 20 bold")

def allclear():
    text_fild.delete(0,END)


def clear():
    ex=text_fild.get()
    ex=ex[0:len(ex)-1]
    text_fild.delete(0,END)
    text_fild.insert(0,ex)


def click_cutto_fun(event):
    b=event.widget
    text=b['text']

    if text== 'x':
        text_fild.insert(END,'*')
        return
  

    if text == '=':
        try:
            ex=text_fild.get()
            ans= eval(ex)
            text_fild.delete(0,END)
            text_fild.insert(0,ans)
        except Exception:
            Error="Error..."
            text_fild.delete(0,END)
            text_fild.insert(0,Error)
            


        return
    text_fild.insert(END,text)


# creating a window
window=Tk()
window.title("calculator")
window.geometry("417x460")
window.resizable(FALSE,FALSE)


pic=PhotoImage(file='cal.png')
# add iconphoto
window.iconphoto(True,pic)

# add image in window
add_image =Label(window,image=pic)
add_image.pack(side=TOP,pady=10)

# heading text
heading=Label(window,text="Calculator",font="arial 30 bold",fg='red')
heading.pack(side=TOP)

# add entry box in window
text_fild=Entry(window,font="arial 20 bold ",justify=RIGHT)
text_fild.pack(side=TOP,fill=X,pady=10)

buttonFrame=Frame(window,bg='white')
buttonFrame.pack(side=TOP,pady=10)

# add button
num=1
for i in range(0,3):
    for j in range(0,3):
        but1=Button(buttonFrame,text=str(num),font=fount,width=5,relief="groove",activebackground='orange',activeforeground='white')
        but1.grid(row=i,column=j)
        num+=1
        but1.bind('<Button-1>',click_cutto_fun)

Zerobutton=Button(buttonFrame,text=0,font=fount,width=5,relief="groove",activebackground='orange',activeforeground='white')
Zerobutton.grid(row=3,column=0)


doutbutton=Button(buttonFrame,text='.',font=fount,width=5,relief="groove",activebackground='orange',activeforeground='white')
doutbutton.grid(row=3,column=1)


equalbutton=Button(buttonFrame,text='=',font=fount,width=5,relief="groove",activebackground='orange',activeforeground='white')
equalbutton.grid(row=3,column=2)

plusbutton=Button(buttonFrame,text='+',font=fount,width=5,relief="groove",activebackground='orange',activeforeground='white')
plusbutton.grid(row=0,column=3)

minusbutton=Button(buttonFrame,text='-',font=fount,width=5,relief="groove",activebackground='orange',activeforeground='white')
minusbutton.grid(row=1,column=3)

mulbutton=Button(buttonFrame,text='x',font=fount,width=5,relief="groove",activebackground='orange',activeforeground='white')
mulbutton.grid(row=2,column=3)

devidebutton=Button(buttonFrame,text='/',font=fount,width=5,relief="groove",activebackground='orange',activeforeground='white')
devidebutton.grid(row=3,column=3)

clearbutton=Button(buttonFrame,text='<',font=fount,width=12,relief="groove",activebackground='orange',activeforeground='white',
command=clear)
clearbutton.grid(row=4,column=0,columnspan=2)

allclearbutton=Button(buttonFrame,text='AC',font=fount,width=12,relief="groove",activebackground='orange',activeforeground='white',
command=allclear)
allclearbutton.grid(row=4,column=2,columnspan=2)


# bind button 

Zerobutton.bind('<Button-1>',click_cutto_fun)
equalbutton.bind('<Button-1>',click_cutto_fun)
doutbutton.bind('<Button-1>',click_cutto_fun)
plusbutton.bind('<Button-1>',click_cutto_fun)
minusbutton.bind('<Button-1>',click_cutto_fun)
mulbutton.bind('<Button-1>',click_cutto_fun)
devidebutton.bind('<Button-1>',click_cutto_fun)

window.mainloop()
