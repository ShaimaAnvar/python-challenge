from tkinter import *
window=Tk() 
btn = Button(window, text = 'Click me !', bd = '5',command = window.destroy)
btn.pack(side = 'top')   
window.mainloop()
