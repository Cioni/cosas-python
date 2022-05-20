from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola Mundo')

# solucion uno
# def open():
#     img = ImageTk.PhotoImage(Image.open('teclas.png'))
#     top = Toplevel()
#     top.title('Hola mundo, nueva ventana')
#     l = Label(top, text='soy un texto en una segunda ventana')
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()
#     top.mainloop()

#solucion 2(pasarlo por variable global)
# def open():
#     global img
#     img = ImageTk.PhotoImage(Image.open('teclas.png'))
#     top = Toplevel()
#     top.title('Hola mundo, nueva ventana')
#     l = Label(top, text='soy un texto en una segunda ventana')
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()
#     top.mainloop()

#solucion 3(definir la imagen antes y pásarla como argumento)
def open(img):
    top = Toplevel()
    top.title('Hola mundo, nueva ventana')
    l = Label(top, text='soy un texto en una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()

img = ImageTk.PhotoImage(Image.open('teclas.png'))
btn = Button(root, text='Click', command=lambda: open(img)).pack()

root.mainloop() 