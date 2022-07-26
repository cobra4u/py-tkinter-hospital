from tkinter import ttk
from tkinter import *


import mysql.connector
import time
from numpy import random
import PIL
from PIL import Image, ImageTk


global s
s=Tk()
s.title ("Main")
s.geometry('5000x5000')
s.configure(bg='#84BF04')

def gen_color():
    
    s.configure(background=random.choice(["black", "red" , "green" , "blue",'orange','white']))
    button=Button(s,text='Click Me',command = gen_color)
    Button.place(x=100,y=100)

p= StringVar()
q= StringVar()
def delmedicin():
    database=mysql.connector.connect(host="localhost",user="root",password="",database="ycet")
    cursorobject=database.cursor()
    ra="delete from medicine"
    cursor=database.cursor()
    cursor.execute(ra)
    
def dropdw ():
    OPTIONS = [
    "Capsule",
    "Tablet",
    "Liquid"
    ]

    master = Tk()

    variable = StringVar(master)
    variable.set(OPTIONS[0]) 

    w = OptionMenu(master, variable, *OPTIONS)
    w.pack()
    print ("value is:" + variable.get())

   

def logout():
    
    s=Tk()
    k.destroy()
    

def medview ():
    
     database=mysql.connector.connect(host="localhost",user="root",password="",database="ycet")
     cursorobject=database.cursor()
     rr="select * from medicine"
     cursor=database.cursor()
     cursor.execute(rr)
     record=cursor.fetchall()
     for a in record:
        print("name is ",a[0])
        print("last name is",a[1])
        print("email is",a[2])
        print("phone is ",a[3])
        print("phone is ",a[4])

def medicin ():
    
    mm=m.get()
    nn=n.get()
    oo=o.get()
    pp=p.get()
    qq=q.get()
    database=mysql.connector.connect(host="localhost",user="root",password="",database="ycet")
    cursorobject=database.cursor()
    ss='insert Into medicine(Medicine name,Medicine Source,Medicine Type,Mfg date,Exp date)values(%s,%s,%s,%s,%s)'
    val=(mm,nn,oo,pp,qq)
    cursorobject.execute(ss,val)
    database.commit()
    
def medicine():

    g=Tk()
    
    global m
    global n
    global o
    global p
    global q
    m= StringVar()
    n= StringVar()
    o= StringVar()
    p= StringVar()
    q= StringVar()
    
    g.title("Add new supplier") 
    g.geometry('500x500')
    g.configure(bg='#A67449')
    
    L1=Label(text="Medicine name",fg='white',bg='black')
    L1.place(x=200,y=100)
    e1=Entry(textvariable=m)
    e1.place(x=300,y=100)

    L2=Label(text="Medicine Source",fg='white',bg='black')
    L2.place(x=700, y=100)
    e2=Entry(textvariable=n)
    e2.place(x=800, y=100)

    #L3=Label(text="Medicine Type",fg='white',bg='black',command=dropdw)
    #L3.place(x=200, y=200)
    #dpbuton=Button(text="Medicine Type",command =dropdw)
    #dpbuton.configure(fg='white',bg='black',height= 1, width=7)
    #dpbuton.place(x=200, y=200)
    #e3=Entry(textvariable=o)
    #e3.place(x=300, y=200)
    p=ttk.Combobox(textvariable=n)
    p['value']=(
      'liquid',
      'tablet',
      'capsules')
    p.pack()

    L4=Label(text="Mfg date",fg='white',bg='black')
    L4.place(x=700, y=200)
    e4=Entry(textvariable=p)
    e4.place(x=800, y=200)

    L5=Label(text="Exp date",fg='white',bg='black')
    L5.place(x=400, y=300)
    e5=Entry(textvariable=q)
    e5.place(x=500, y=300)
    
    B=Button(text="save",command=medicin)
    B.configure(bg='#573BBA',height = 3, width = 3)
    B.place(x=500,y=600)

def newacount():
  
    re=jj.get()
    de=ll.get()
    et=kk.get()
    ef=mm.get()
    database=mysql.connector.connect(host="localhost",user="root",password="",database="ycet")
    cursorobject=database.cursor()
    ss='insert into createacc(firstname, lastname, ID, Password)values(%s,%s,%s,%s)'
    val=(re,et,de,ef)
    cursorobject.execute(ss,val)
    database.commit()
def newaccount():
    
    z=Tk()
    global mm
    global jj
    global ll
    global kk
    jj= StringVar()
    ll= StringVar()
    kk= StringVar()
    mm=StringVar()
    
    z.title("Add new supplier") 
    z.geometry('500x500')
    z.configure(bg='#A67449')
    
    L1=Label(text="First Name",fg='black',bg='#FFFF00')
    L1.place(x=200,y=100)
    e1=Entry(textvariable=jj)
    e1.place(x=300,y=100)

    L2=Label(text="Last Name",fg='black',bg='#FFFF00')
    L2.place(x=700,y=100)
    e2=Entry(textvariable=kk)
    e2.place(x=800, y=100)

    L3=Label(text="ID",fg='black',bg='#FFFF00')
    L3.place(x=200,y=200)
    e3=Entry(textvariable=ll)
    e3.place(x=300, y=200)

    L4=Label(text="Password",fg='black',bg='#FFFF00')
    L4.place(x=500,y=200)
    e4=Entry(textvariable=mm)
    e4.place(x=700, y=200)
    
    B=Button(text="save",command=newacount)
    B.configure(bg='#573BBA',height = 3, width = 3)
    B.place(x=500,y=400)

def report():
    y=Tk()
    y.title("Report") 
    y.geometry('500x500')
    y.configure(bg='#A67449')
    
    L1=Label(text= "Add new report", fg='white', bg='black')
    L1.place(x=200,y=100)
    e1=Entry(txtv)
    e1.place(x=300,y=100)

    L2=Label(text= "Delete Report", fg='white', bg='black')
    L2.place(x=700, y=100)
    e2=Entry()
    e2.place(x=800, y=100)
    
    B=Button(text="save",command=mysup)
    B.configure(bg='#573BBA',height = 3, width = 3)
    B.place(x=500,y=600)
    
def supply():
    p=Tk()
    global sp
    global t
    global u
    global v
    sp= StringVar()
    t= StringVar()
    u= StringVar()
    v= StringVar()
    p.title("Add new supplier") 
    p.geometry('500x500')
    p.configure(bg='#A67449')

    
    L1=Label(text="name",fg='black',bg='#FFFF00')
    L1.place(x=200,y=100)
    e1=Entry(textvariable=sp)
    e1.place(x=300,y=100)


    L2=Label(text="LName",fg='black',bg='#FFFF00')
    L2.place(x=700,y=100)
    e2=Entry(textvariable=t)
    e2.place(x=800, y=100)


    L3=Label(text="email",fg='black',bg='#FFFF00')
    L3.place(x=200,y=200)
    e3=Entry(textvariable=u)
    e3.place(x=300, y=200)

    
    L4=Label(text="phone",fg='black',bg='#FFFF00')
    L4.place(x=700,y=200)
    e4=Entry(textvariable=v)
    e4.place(x=800, y=200)
    
    B=Button(text="save",command=mysup)
    B.configure(bg='#573BBA',height = 3, width = 3)
    B.place(x=500,y=400)


def mysup():
    c=sp.get()
    d=t.get()
    e=u.get()
    f=v.get()
   # L1=Label(text=c)
    #L1.place(x=500,y=100)
    database=mysql.connector.connect(host="localhost",user="root",password="",database="ycet")
    cursorobject=database.cursor()
    s='insert Into supplier(name,lname,email,phone)values(%s,%s,%s,%s)'
    val=(c,d,e,f)
    cursorobject.execute(s,val)
    database.commit()


def view():
     database=mysql.connector.connect(host="localhost",user="root",password="",database="ycet")
     cursorobject=database.cursor()
     r="select * from supplier"
     cursor=database.cursor()
     cursor.execute(r)
     record=cursor.fetchall()
     for a in record:
        print("name is ",a[0])
        print("last name is",a[1])
        print("email is",a[2])
        print("phone is ",a[3])


    

def main():
    ap=p.get()
    pp=StringVar()
    b=q.get()
    global aa
    global bb
    global a
    bb=StringVar()
    aa=StringVar()
    database=mysql.connector.connect(host="localhost",user="root",password="",database="ycet")
    cursorobject=database.cursor()
    r='select * from createacc where ID=%s and Password=%s'
    val=(ap,b)
    #cursor=database.cursor(r,val)
    cursorobject.execute(r,val)
    record=cursorobject.fetchall()
    for a in record:
        print("name is ",a[0])
        print("last name is",a[1])
        print("Id is",a[2])
        print("Password is ",a[3])
    print(ap)
    aa=a[2]
    bb=a[3]
    print(aa)
    global k
    if(aa==ap and bb==b):
        k=Tk()
        s.destroy()
        k.title("Menubar")
        k.geometry("500x500")
        menubar=Menu(k)
        k.config(bg='#008BAB', menu=menubar)
        p
        supp=Menu(menubar)
        menubar.add_cascade(label="supplier",menu=supp)
        supp.add_command(label="Add new supplier", command=supply)
        supp.add_command(label="View All Supplier",command =view)
        

        med=Menu(menubar)
        menubar.add_cascade(label="Medicine",menu=med)
        med.add_command(label="Add new medicine", command=medicine)
        med.add_command(label="view all medicine",command = medview)
        med.add_command(label="delete medicine")

        rep=Menu(menubar)
        menubar.add_cascade(label="report",menu=rep)
        rep.add_command(label="Add new report", command=report)
        rep.add_command(label="delete report")
        
        log=Menu(menubar)
        menubar.add_cascade(label="Logout",menu=log)
        log.add_command(label="logout",command=logout)
        log.add_command(label="create new account",command=newaccount)
        
         
    else:
        L5=Label(text="Invalid User",fg='white',bg='purple', font=('times',20))
        L5.place(x=750,y=50)


#img=PhotoImage(file="D:/img1.img", format='img')
#lo=Label(s,image=img)
#lo.place(x=200,y=300)
frame2 = PhotoImage(file="E:/back.png", format="png")
#frame2 = [PhotoImage(file='D:/shapes_dribbble.gif', format = 'gif -index %i' %i)
          

e1=Entry(textvariable=p, font=(20))
e1.place(x=750,y=250)

L1=Label(text="username",fg='white',bg='black', font=('times',20))
L1.place(x=640,y=250)

e2=Entry(show="*" ,textvariable=q,font=(20))
e2.place(x=750, y=400)
L2=Label(text="Password",fg='white',bg='black', font=('times',20))
L2.place(x=640,y=400)

B=Button(text="Login",command = main)
B.place(x=750,y=700)
B=Button(text="color",command = gen_color)
B.place(x=800,y=750)


