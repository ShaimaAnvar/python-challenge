from tkinter import *
window=Tk()
window.geometry("700x500")

#-------heading------
label6=Label(window,text="Vintage Restaurent",font="times 25 bold italic underline")
label6.place(x=200,y=10)

#---define function---
def calculate():
    if len(e1.get()) == 0:
        aloo_paratha=0
    else:
        aloo_paratha=e1.get()

    if len(e2.get()) == 0:
        samosa=0
    else:
        samosa=e2.get()

    if len(e3.get()) == 0:
        fried_rice=0
    else:
        fried_rice=e3.get()
    
    if len(e4.get()) == 0:
        tea=0
    else:
        tea=e4.get()
    #print(type(aloo_paratha))
    total=int(aloo_paratha)*30+int(samosa)*5+int(fried_rice)*35+int(tea)*5
    label12=Label(window,text="total: "+str(total),font="times 18 italic")
    label12.place(x=100,y=350)
    print(total)

#-------menu------
label1=Label(window,text="Menu",font="times 20 bold italic",fg="brown")
label1.place(x=520,y=70)

label2=Label(window,text="aloo paratha      Rs.30",font="times 18 italic")
label2.place(x=450,y=120)

label3=Label(window,text="samosa                Rs.5",font="times 18 italic")
label3.place(x=450,y=160)

label4=Label(window,text="fried rice            Rs.35",font="times 18 italic")
label4.place(x=450,y=200)

label5=Label(window,text="tea                       Rs.5",font="times 18 italic")
label5.place(x=450,y=240)

#-------billing section------

label7=Label(window,text="aloo paratha",font="times 18 italic")
label7.place(x=20,y=120)
e1=Entry(window)
e1.place(x=20,y=150)

label8=Label(window,text="samosa",font="times 18 italic")
label8.place(x=200,y=120)
e2=Entry(window)
e2.place(x=200,y=150)

label9=Label(window,text="fried rice",font="times 18 italic")
label9.place(x=20,y=220)
e3=Entry(window)
e3.place(x=20,y=250)

label10=Label(window,text="tea",font="times 18 italic")
label10.place(x=200,y=220)
e4=Entry(window)
e4.place(x=200,y=250)

label11=Label(window,text="Select the items",font="times 18 italic bold",fg="brown")
label11.place(x=50,y=70)

btn=Button(window,text="bill",width=20,command=calculate)
btn.place(x=100,y=320)



window.mainloop()