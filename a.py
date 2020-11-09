from tkinter import*


top=Tk()

top.title("quiz")
# top.iconphoto(False,f)
d=Canvas(top,width=800,height=1000)
so=PhotoImage(file="b.gif")
back=Label(top,image=so)
back.place(x=-20,y=0,relwidth=1,relheight=1)
la=Label(top,text="Mahabharat",fg="blue",font=("Algerian",20)).pack()
