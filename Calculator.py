from tkinter import *
root = Tk()

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value=eval(screen.get())

            scvalue.set(value)
            screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root.geometry("544x700")
scvalue=StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue)
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

f = Frame(root,bg="grey")

b=Button(f,text="9",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b=Button(f,text="7",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root,bg="grey")

b=Button(f,text="6",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b=Button(f,text="4",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root,bg="grey")

b=Button(f,text="3",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b=Button(f,text="1",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

f.pack()

f.pack()

f = Frame(root,bg="grey")

b=Button(f,text="0",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b=Button(f,text="+",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

f.pack()

f.pack()

f = Frame(root,bg="grey")

b=Button(f,text="*",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b=Button(f,text="%",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

f.pack()

f.pack()

f = Frame(root,bg="grey")

b=Button(f,text="=",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b=Button(f,text="C",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b=Button(f,text=".",padx=23,pady=25)
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

f.pack()


root.mainloop()