from tkinter import *
root = Tk()
root.geometry("500x500")
root.title('Phone Book')

def win():
    global nameV, phoneV, lb

    lbframe = Frame(root, bg='red', width=300, height=400)
    lbframe.grid(row=4, column=2)

    add = Button(root, text='Add', width=15, pady=5, command=addN)
    add.grid(row=2, column=1)

    delete = Button(root, text='Delete', width=15, pady=5, command=delN)
    delete.grid(row=2, column=2)

    ref = Button(root, text='Refresh', width=15, pady=5, command=refresh)
    ref.grid(row=2, column=3)

    name = Label(root, text='Name')
    name.grid(row=0, column=1, sticky=E)

    nameV = StringVar()
    nameEntry = Entry(root, textvariable=nameV)
    nameEntry.grid(row=0, column=2)

    phoneV = StringVar()
    phone = Label(root, text='Phone')
    phone.grid(row=1, column=1, sticky=E)

    phoneEntry = Entry(root, textvariable=phoneV)
    phoneEntry.grid(row=1, column=2)

    lb = Listbox(lbframe, height=20)
    lb.grid(row=1, column=1)


    sb = Scrollbar(lbframe, orient=VERTICAL)
    sb.grid(row=1, column=2)

    sb.configure(command=lb.yview)
    lb.configure(yscrollcommand=sb.set)

def addN():
    n = nameV.get()
    p = phoneV.get()
    f = open('ph.txt', 'a')
    f.write('\n'+str(n))
    f.write(':'+str(p))
    
def delN():
        item= lb.curselection()
        val = lb.get(lb.curselection())
        lb.delete(item)
        with open('ph.txt', 'r') as f:
                lines = f.readlines()
        with open('ph.txt', 'w') as f:
                for line in lines:
                        if line != val:
                                f.write(line)



def ret():
    f = open('ph.txt', 'r')
    lines = f.readlines()
    f.seek(0, 0)
    for i in lines:
        l = f.readline()
        l.rstrip('\n')
        lb.insert(END, l)
def refresh():
        lb.delete(0, 'end')
        ret()
    

    
win()
ret()
root.mainloop()