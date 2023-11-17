from tkinter import*
import random
import time;
import Restaurant2

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")

text_Input=StringVar()
operator=""

Tops = Frame(root,width = 1600,height = 50,bg="black",relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 800,height = 700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width = 300,height = 700,relief=SUNKEN)
f2.pack(side=RIGHT)
#==========================Time===================================================================================
localtime=time.asctime(time.localtime(time.time()))
#==========================Info===================================================================================
lblInfo = Label(Tops, font=('arial',50, 'bold'),text="Restaurant Management System",fg="red",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('arial',20, 'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#==========================Calculator==============================================================================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup =str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(10908 , 500876)
    randomRef=str(x)
    rand.set(randomRef)

    CoSoup = float(Soup.get())
    CoDrinks = float(Drinks.get())
    CoTandoor_Chicken = float(Tandoor_Chicken.get())
    CoNoodle = float(Noodle.get())
    CoChicken_Biryani = float(Chicken_Biryani.get())
    CoMutton_Biryani = float(Mutton_Biryani.get())

    CostofSoup = CoSoup * 35
    CostofDrinks = CoDrinks * 50
    CostofTandoor_Chicken = CoTandoor_Chicken * 150
    CostofNoodle = CoNoodle * 70
    CostofChicken_Biryani = CoChicken_Biryani * 120
    CostofMutton_Biryani = CoMutton_Biryani * 150

    CostofMeal = "Rs.", str('%.2f' % (CostofSoup + CostofDrinks + CostofTandoor_Chicken + CostofNoodle + CostofChicken_Biryani + CostofMutton_Biryani))
    
    PayTax = ((CostofSoup + CostofDrinks + CostofTandoor_Chicken + CostofNoodle + CostofChicken_Biryani + CostofMutton_Biryani) * 0.02)
    
    TotalCost = (CostofSoup + CostofDrinks + CostofTandoor_Chicken + CostofNoodle + CostofChicken_Biryani + CostofMutton_Biryani)

    Ser_Charge = ((CostofSoup + CostofDrinks + CostofTandoor_Chicken + CostofNoodle + CostofChicken_Biryani + CostofMutton_Biryani)/99)

    Service = "Rs.", str('%.2f' % Ser_Charge)
    OverAllCost = "Rs.", str('%.2f' % (PayTax + TotalCost + Ser_Charge ))
    PaidTax =  "Rs.", str('%.2f' % PayTax)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    Subtotal.set(CostofMeal)
    Total.set(OverAllCost)
    Restaurant2.AddRestaurantRecord(randomRef,Soup.get(),Noodle.get(),Tandoor_Chicken.get(),Chicken_Biryani.get(),Mutton_Biryani.get(),Drinks.get(),Cost.get(),Service_Charge.get(),Tax.get(),Subtotal.get(),Total.get())
   
      
def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Soup.set("")
    Noodle.set("")
    Tandoor_Chicken.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Biryani.set("")
    Mutton_Biryani.set("")
    
    
txtDisplay = Entry(f2,font=('arial',20, 'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="7",bg="powder blue",command=lambda: btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="8",bg="powder blue",command=lambda: btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="9",bg="powder blue",command=lambda: btnClick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="+",bg="powder blue",command=lambda: btnClick("+")).grid(row=2,column=3)

#----------------------------------------------------------------------------------------------------------------------

btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="4",bg="powder blue",command=lambda: btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="5",bg="powder blue",command=lambda: btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="6",bg="powder blue",command=lambda: btnClick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="-",bg="powder blue",command=lambda: btnClick("-")).grid(row=3,column=3)

#------------------------------------------------------------------------

btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="1",bg="powder blue",command=lambda: btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="2",bg="powder blue",command=lambda: btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="3",bg="powder blue",command=lambda: btnClick(3)).grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="*",bg="powder blue",command=lambda: btnClick("*")).grid(row=4,column=3)

#------------------------------------------------------------------------

btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="0",bg="powder blue",command=lambda: btnClick(0)).grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="C",bg="powder blue",command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="=",bg="powder blue",command=btnEqualsInput).grid(row=5,column=2)

Divition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text="/",bg="powder blue",command=lambda: btnClick("/")).grid(row=5,column=3)

#----------------------------------------------------Restaurant Info 1-------------------
rand=StringVar()
Soup=StringVar()
Noodle=StringVar()
Tandoor_Chicken=StringVar()
Subtotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Chicken_Biryani=StringVar()
Mutton_Biryani=StringVar()

lblReference = Label(f1,font=('arial',16,'bold'), text="Reference", bd=16, anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtReference.grid(row=0,column=1)

lblSoup = Label(f1,font=('arial',16,'bold'), text="Manchow Soup", bd=16, anchor='w')
lblSoup.grid(row=1,column=0)
txtSoup=Entry(f1,font=('arial',16,'bold'),textvariable=Soup,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtSoup.grid(row=1,column=1)

lblNoodle = Label(f1,font=('arial',16,'bold'), text="Noodle", bd=16, anchor='w')
lblNoodle.grid(row=2,column=0)
txtNoodle=Entry(f1,font=('arial',16,'bold'),textvariable=Noodle,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtNoodle.grid(row=2,column=1)

lblTandoor_Chicken = Label(f1,font=('arial',16,'bold'), text="Tandoor_Chicken", bd=16, anchor='w')
lblTandoor_Chicken.grid(row=3,column=0)
txtTandoor_Chicken=Entry(f1,font=('arial',16,'bold'),textvariable=Tandoor_Chicken,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtTandoor_Chicken.grid(row=3,column=1)

lblChicken = Label(f1,font=('arial',16,'bold'), text="Chicken Biryani", bd=16, anchor='w')
lblChicken.grid(row=4,column=0)
txtChicken=Entry(f1,font=('arial',16,'bold'),textvariable=Chicken_Biryani,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtChicken.grid(row=4,column=1)

lblMutton = Label(f1,font=('arial',16,'bold'), text="Mutton_Biryani", bd=16, anchor='w')
lblMutton.grid(row=5,column=0)
txtMutton=Entry(f1,font=('arial',16,'bold'),textvariable=Mutton_Biryani,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtMutton.grid(row=5,column=1)

#----------------------------------------------------Restaurant Info 2------------------------------

lblDrinks = Label(f1,font=('arial',16,'bold'), text="Drinks", bd=16, anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg='#ffffff',justify='right')
txtDrinks.grid(row=0,column=3)

lblCost = Label(f1,font=('arial',16,'bold'), text="Cost of Meal", bd=16, anchor='w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg='#ffffff',justify='right')
txtCost.grid(row=1,column=3)

lblService = Label(f1,font=('arial',16,'bold'), text="Service Charge", bd=16, anchor='w')
lblService.grid(row=2,column=2)
txtService=Entry(f1,font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg='#ffffff',justify='right')
txtService.grid(row=2,column=3)

lblStateTax = Label(f1,font=('arial',16,'bold'), text="StateTax", bd=16, anchor='w')
lblStateTax.grid(row=3,column=2)
txtStateTax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg='#ffffff',justify='right')
txtStateTax.grid(row=3,column=3)

lblSubtotal = Label(f1,font=('arial',16,'bold'), text="Subtotal", bd=16, anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal=Entry(f1,font=('arial',16,'bold'),textvariable=Subtotal,bd=10,insertwidth=4,bg='#ffffff',justify='right')
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1,font=('arial',16,'bold'), text="Total  Cost", bd=16, anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal=Entry(f1,font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg='#ffffff',justify='right')
txtTotal.grid(row=5,column=3)
#========================================Buttons====================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="blue",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="blue",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="blue",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)

root.mainloop()

