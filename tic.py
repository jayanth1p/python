from tkinter import*
root=Tk()
def per(): 
    x=9
    y=5
    a=x-y
    b=x+y
    c=int(x/y)
    la=Label(root,text=f"hi {a} and {b}, {c}",bd=5,bg="darkgreen" )
    la.pack()
   
    pass
def display():
     l=Label(root,text="you cliked Button")
     l.grid(row=2,column=2)
     pass
lab=Label(root,text="hi i made it?",bg="#FFF806", width=10,height=5)
but=Button(root,text="hit me if you can ",command=display,bd=5)
photo=PhotoImage(file="m.png")
root.iconphoto(False,photo)
root.title("tic ta To")


b=Button(root,text="hai i am there to help you",bd=6,bg="lightgreen",command=per)
b.grid(row=0,column=0,pady=0)
but.grid(row=1,column=0)

lab.grid(row=1,column=1)
root.mainloop()




