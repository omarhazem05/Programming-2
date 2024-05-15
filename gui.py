from tkinter import *
from tkinter.messagebox import showerror
w=Tk()
w.title("loan calculator")
w.geometry("600x600+400+400")
w.configure(bg='black')
def the_payment():
    loan=float(e2.get())
    year=int(e3.get())
    if year==1:
        rate=13.76
    elif year==3:
        rate=14.06
    elif year==5:
        rate=14.87
    elif year==7:
        rate=15.71
    else:
        print (show_error())
    interest=(loan*rate/100)
    totalinterest=interest*(year)
    totalloan=totalinterest+(loan)
    ppmonth=totalloan/(year*12)
    label_amount.config(text=f"Payment per month: {ppmonth}")
    label_amount1.config(text=f"Total loan: {totalloan}")
    label_amount2.config(text=f"Interest: {interest}")
    label_amount3.config(text=f"Total interest{totalinterest}")
def show_error():
    showerror("show error","error")
def clear():
    e1.delete(0,'end')
    e2.delete(0,'end')
    e3.delete(0,'end')
    label_amount.config(text='')
def exit():
    w.quit()
photo=PhotoImage(file="misr1.png")
l=Label(w,image=photo)
l.pack()
l1=Label(w,text="Enter your current job",bg="cyan")
l1.pack()
e1=Entry(bd=10)
e1.pack()
l2=Label(w,text="Enter the loan amount",bg="cyan")
l2.pack()
e2=Entry(bd=10)
e2.pack()
l3=Label(w,text="Enter the number of years",bg="cyan")
l3.pack()
e3=Entry(bd=10)
e3.pack()
b1=Button(w,text="Calculate", command=the_payment)
b1.pack()
b2=Button(w,text="Clear",command=clear)
b2.pack()
b3=Button(w,text="Exit",command=exit)
b3.pack()
label_amount=Label(w)
label_amount.pack()

label_amount1=Label(w)
label_amount1.pack()

label_amount2=Label(w)
label_amount2.pack()

label_amount3=Label(w)
label_amount3.pack()

w.mainloop()
