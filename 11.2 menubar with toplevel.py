from tkinter import  *
root=Tk()
root.geometry('750x600')
def one():
    top=Toplevel()
    top.geometry('500x350')
    top.title('toplevel1')
    Label(top,text='one',fg='yellow',bg='black').pack(side=TOP)
def two():
    top=Toplevel()
    top.geometry('500x350')
    top.title('toplevel2')
    Label(top,text='two',fg='yellow',bg='black').pack(side=TOP)
def three():
    top=Toplevel()
    top.geometry('500x350')
    top.title('toplevel2')
    Label(top,text='three',fg='yellow',bg='black').pack(side=TOP)
def ok():
    print("OK")

mainmenu=Menu(root)
filemenu=Menu(mainmenu,tearoff=0)
filemenu.add_command(label='one',command=one)
filemenu.add_command(label='two',command=two)
filemenu.add_command(label='three',command=three)
mainmenu.add_cascade(label='File',menu=filemenu)

editmenu=Menu(mainmenu,tearoff=0)
editmenu.add_command(label='ok',command=ok)
editmenu.add_command(label='exit',command=root.destroy)
mainmenu.add_cascade(label='Edit',menu=editmenu)

root.config(menu=mainmenu)
root.mainloop()