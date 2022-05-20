from tkinter import*

root = Tk()
root.title('Hola mundo: checkbox')

root.geometry('500x500')

var = StringVar()
var.set('no')

def mostrar():
    l = Label(root, text=var.get())
    l.pack()

c = Checkbutton(root, text='Soy un checkbox', variable=var, onvalue='si', offvalue='no')
c.pack()

btn = Button(root, text='Click', command=mostrar)
btn.pack()

root.mainloop()