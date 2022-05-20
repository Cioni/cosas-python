from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hola Mundo')

# def click():
#    messagebox.showwarning('Popup', 'Hola Mundo')

# def click():
#    messagebox.showinfo('Popup', 'Hola Mundo')

# def click():
#    messagebox.showerror('Popup', 'Hola Mundo :(')

#  def click():
#     respuesta = messagebox.askquestion('Popup', 'Hola Mundo :(')
#     print(respuesta)
#     if respuesta == 'yes':
#         messagebox.showinfo('Respuesta', 'la respues fue ' + respuesta)
#     else:
#         messagebox.showinfo('Respuesta', 'la respuesta fue ' + respuesta) 

# def click():
#     respuesta = messagebox.askokcancel('Hola Mundo', 'Desea realizar acción?')
#     if respuesta:
#         messagebox.showinfo('hola Mundo', 'La respuesta fue OK')
#     else:
#         messagebox.showinfo('Hola Mundo', 'La respuesta fue cancelar')
        
def click():
    respuesta = messagebox.askyesno('Hola Mundo', 'Desea realizar acción?')
    if respuesta:
        messagebox.showinfo('hola Mundo', 'La respuesta fue Yes')
    else:
        messagebox.showinfo('Hola Mundo', 'La respuesta fue No')

btn = Button(root, text='Presioname', command=click)
btn.pack()

root.mainloop()
