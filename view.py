
from tkinter import *
from tkinter import ttk
import model
import htmlCreater as hc

root = None
ent = None
lbl = None
lbl1 = None

def createMenu():
    global root
    global ent
    global lbl
    global lbl1
    root= Tk()
    root.title("Телефонный справочник")

    ttk.Button(root, text="Вывести телефонный справочник", command=printResult).grid(sticky=N)
    lbl1 = Label(root, text="")  
    lbl1.grid(sticky=N)   
    ent = Entry(root, width=27)
    ent.grid(column=0, row=2)  
    ttk.Button(root, text="Поиск", command=printSearch).grid(column=1, row=2) 
    lbl = Label(root, text="")  
    lbl.grid(column=0, row=3)   
    ttk.Button(root, text="Создать HTML", command=createHtml).grid(sticky=SW)
    ttk.Button(root, text="Quit", command=root.destroy).grid(sticky=SW)
    root.mainloop()

def printResult():
    global lbl1
    lbl1.configure(text= model.printDict())


def printSearch():
    global ent
    global lbl
    b = format(ent.get())
    res = model.findPhoneNumber(b)
    lbl.configure(text= res)


def createHtml():
    hc.create()


