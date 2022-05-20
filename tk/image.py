from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola Mundo')

# imagen = Image.open('teclas.png')
# imagen.show()

img = ImageTk.PhotoImage(Image.open('teclas.png'))
l = Label(image=img)
l.pack()

root.mainloop()
