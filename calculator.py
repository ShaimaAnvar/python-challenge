from tkinter import *
import tkinter.font as font
expression = ""
#myFont = font.Font(weight=bold)
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
 
window=Tk() 
window.configure(background="black")
window.geometry("320x400")
equation = StringVar()
entry = Entry(window, bg='white',width=100 ,textvariable=equation)
entry.grid(row=0, column=0,ipadx=15, ipady=15, columnspan=75)

button1 = Button(window, text=' 1 ', bg='#999966',command=lambda: press(1), height=3, width=8)
button1.grid(row=2, column=0,padx=5, pady=5)
#button1['font'] = myFont
#button1.pack()
button2 = Button(window, text=' 2 ', bg='#999966',command=lambda: press(2), height=3, width=8)
button2.grid(row=2, column=1,padx=5, pady=5)
 
button3 = Button(window, text=' 3 ', bg='#999966',command=lambda: press(3), height=3, width=8)
button3.grid(row=2, column=2,padx=5, pady=5)

button4 = Button(window, text=' 4 ', fg='black', bg='#999966',command=lambda: press(4), height=3, width=8)
button4.grid(row=3, column=0,padx=5, pady=5)
 
button5 = Button(window, text=' 5 ', fg='black', bg='#999966',command=lambda: press(5), height=3, width=8)
button5.grid(row=3, column=1,padx=5, pady=5)
 
button6 = Button(window, text=' 6 ', fg='black', bg='#999966',command=lambda: press(6), height=3, width=8)
button6.grid(row=3, column=2,padx=5, pady=5)
 
button7 = Button(window, text=' 7 ', fg='black', bg='#999966',command=lambda: press(7), height=3, width=8)
button7.grid(row=4, column=0,padx=5, pady=5)

button8 = Button(window, text=' 8 ', fg='black', bg='#999966',command=lambda: press(8), height=3, width=8)
button8.grid(row=4, column=1,padx=5, pady=5)
 
button9 = Button(window, text=' 9 ', fg='black', bg='#999966',command=lambda: press(9), height=3, width=8)
button9.grid(row=4, column=2,padx=5, pady=5)
 
button0 = Button(window, text=' 0 ', fg='black', bg='#999966',command=lambda: press(0), height=3, width=8)
button0.grid(row=5, column=0,padx=5, pady=5)

plus = Button(window, text=' + ', fg='black', bg='#cc9900',command=lambda: press("+"), height=3, width=8)
plus.grid(row=2, column=3,padx=5, pady=5)
 
minus = Button(window, text=' - ', fg='black', bg='#cc9900',command=lambda: press("-"), height=3, width=8)
minus.grid(row=3, column=3,padx=5, pady=5)
 
multiply = Button(window, text=' * ', fg='black', bg='#cc9900',command=lambda: press("*"), height=3, width=8)
multiply.grid(row=4, column=3,padx=5, pady=5)

divide = Button(window, text=' / ', fg='black', bg='#cc9900',command=lambda: press("/"), height=3, width=8)
divide.grid(row=5, column=3,padx=5, pady=5)
 
equal = Button(window, text=' = ', fg='black', bg='#cc9900', height=3, width=8,command=equalpress)
equal.grid(row=5, column=2,padx=5, pady=5)
 
clear = Button(window, text='Clear', fg='black', bg='#cc9900', height=3, width=8, command=clear)
clear.grid(row=5, column=1)
 
Decimal= Button(window, text='.', fg='black', bg='#999966',command=lambda: press('.'), height=3, width=8)
Decimal.grid(row=6, column=0,padx=5, pady=5)
 
window.mainloop()