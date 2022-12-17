from tkinter import *
import tkinter.messagebox as mbox
root=Tk()
canvas_width=750
canvas_height=600
root.geometry(f"{canvas_width}x{canvas_height}")
root.minsize(750,600)
root.maxsize(750,600)
root.title("Saiteja's editor" )
# var=IntVar()
def msg():
    mbox.showinfo('Order Template','''Thank You For Coming....Your order will be recieved soon.... ''')
    mbox.askquestion('RATING','DID U LIKE THE SERVICE?')

c_widget=Canvas(root,width=canvas_width,height=canvas_height,bg='black')
c_widget.place(x=0,y=0)
c_widget.create_line(0,0,750,600,fill='blue',width=10)
c_widget.create_line(750,0,0,600,fill='green',width=10)
c_widget.create_line(375,0,375,600,fill='yellow',width=10)
c_widget.create_line(0,300,750,300,fill='aqua',width=10)
c_widget.create_oval(20,20,730,580,fill='yellow',outline='brown',width=10)
c_widget.create_text(375,300,text='WELCOME TO CBIT CANTEEN',font='Times 20 bold',fill='dark blue')
# b1=Button(root,text='CLICK HERE',bg='aqua',fg='black',font='calibri 12 bold',padx=10,pady=10,command=msg)
# b1.place(x=320,y=260)
b2=Button(root,text='EXIT',bg='aqua',fg='black',font='calibri 12 bold',padx=30,pady=10,command=quit)
b2.place(x=320,y=330)
mainmenu=Menu(root)
bfmenu=Menu(mainmenu,tearoff=0)
bfmenu.add_command(label='Plain Dosa',activebackground='black',font='calibri 12 bold',activeforeground='yellow',command=msg)
bfmenu.add_command(label='Masala Dosa',activebackground='black',font='calibri 12 bold',activeforeground='yellow',command=msg)
bfmenu.add_command(label='Bonda/Punugulu',activebackground='black',font='calibri 12 bold',activeforeground='yellow',command=msg)
bfmenu.add_command(label='Idly',activebackground='black',font='calibri 12 bold',activeforeground='yellow',command=msg)
bfmenu.add_command(label='Vada',activebackground='black',font='calibri 12 bold',activeforeground='yellow',command=msg)
mainmenu.add_cascade(label='BreakFast',menu=bfmenu,font='calibri 12 bold')
# r1=Radiobutton(bfmenu,text='samosa',variable=var,value=0)
# r1.pack()
# r2=Radiobutton(bfmenu,text='cutlet',variable=var,value=1)
# r2.pack()

Lunchmenu=Menu(mainmenu,tearoff=0)
Lunchmenu.add_command(label='Meals',activebackground='black',activeforeground='yellow',font='calibri 12 bold',command=msg)
Lunchmenu.add_command(label='Biryani',activebackground='black',font='calibri 12 bold',activeforeground='yellow',command=msg)
Lunchmenu.add_command(label='Puri',activebackground='black',font='calibri 12 bold',activeforeground='yellow',command=msg)
Lunchmenu.add_command(label='Fried Rice',activebackground='black',font='calibri 12 bold',activeforeground='yellow',command=msg)
Lunchmenu.add_command(label='Pulav',activebackground='black',font='calibri 12 bold',activeforeground='yellow',command=msg)
Lunchmenu.add_command(label='Special',activebackground='black',font='calibri 12 bold',activeforeground='yellow',command=msg)
mainmenu.add_cascade(label='Lunch',menu=Lunchmenu)


root.config(menu=mainmenu)

root.mainloop()
