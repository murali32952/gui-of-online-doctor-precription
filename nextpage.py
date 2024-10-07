from tkinter import *
import pymysql
from tkinter import messagebox
from project import userentry as user
from tkinter import ttk


nextpage=Tk()
nextpage.geometry("790x512")
backgroundlabel=Label(nextpage,bg='#ffd966',width=790,height=512)
backgroundlabel.pack()
nextpage.resizable(0,0)
frame1=Frame(nextpage,width=395,height=512,bg="#351c75")
frame1.place(x=0,y=0)
frame2=Frame(nextpage,width=395,height=512,bg='#00ffff')
frame2.place(x=395,y=0)

def searchdetail():
    window2=Toplevel()
    window2.geometry("450x100")
    window2.resizable(0,0)
    window2.title('Details')
    
    def searchtherow():
        if searchentry.get()=='':
            messagebox.showerror('Error','Fill the entry field')
            
        else:
            try:
                conn=pymysql.connect(host='localhost',user='root',password='dhan@32952')
                mycursor=conn.cursor()
            except:
                messagebox.showinfo('Unsuccessfull','Connectivity issue')
                
        
            query='use signupdata;'
            mycursor.execute(query)
            query='select date,hospital,doctorname,prescription from data2 where usn=%s and doctorname=%s;'
            mycursor.execute(query,(user.get(),searchentry.get()))
            row=mycursor.fetchall()
            print(row)
            
            ##window3=Toplevel()
            ##scrollbarx=Scrollbar(window3,orient=HORIZONTAL)
            ##scrollbarx.pack(side=BOTTOM,fill=X)
            ##detailwindowttk=ttk.Treeview(window3,columns=('Date','Hospital Name','Doctors Name','Prescription'),xscrollcommand=scrollbarx.set)
            ##detailwindowttk.pack(fill=BOTH,expand=1)
            ##scrollbarx.config(command=detailwindowttk.xview)
            ##detailwindowttk.heading('Date',text='DATE')
            ##detailwindowttk.heading('Hospital Name',text='HOSPITAL NAME')
            ##detailwindowttk.heading('Doctors Name',text="DOCTOR'S NAME")
            ##detailwindowttk.heading('Prescription',text='PRESCRIPTION')
            ##detailwindowttk.config(show='headings')
            
            
            
        
    
   

    searchlabel=Label(window2,text="Enter Doctor's Name :",bg='#ffffff',fg='#434343',font=13)
    searchlabel.grid(row=0,column=0)
    searchentry=Entry(window2,width=20,font=5)
    searchentry.grid(row=0,column=1)
    searchbutton=Button(window2,text='Search',width=15,height=1,activebackground='white',command=searchtherow)
    searchbutton.grid(row=3,column=1,pady=25)
    


    


def showdetail():
    window1=Toplevel()
    window1.geometry("500x400+200+200")
    window1.resizable(0,0)
    window1.title('Details')
    ScrollbarX=Scrollbar(window1,orient=HORIZONTAL)
    ScrollbarY=Scrollbar(window1,orient=VERTICAL)
    ScrollbarX.pack(side=BOTTOM,fill=X)
    ScrollbarY.pack(side=RIGHT,fill=Y)
    detailwindowttk=ttk.Treeview(window1,columns=('Date','Hospital Name','Doctors Name','Prescription'),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
    detailwindowttk.pack(fill=BOTH,expand=1)
    ScrollbarX.config(command=detailwindowttk.xview)
    ScrollbarY.config(command=detailwindowttk.yview)
    detailwindowttk.heading('Date',text='DATE')
    detailwindowttk.heading('Hospital Name',text='HOSPITAL NAME')
    detailwindowttk.heading('Doctors Name',text="DOCTOR'S NAME")
    detailwindowttk.heading('Prescription',text='PRESCRIPTION')
    detailwindowttk.config(show='headings') 
    try:
         conn=pymysql.connect(host='localhost',user='root',password='dhan@32952')
         mycursor=conn.cursor()
    except:
        messagebox.showerror('ERROR','Database Connectivity Issues')
        return
    query='use signupdata;'
    mycursor.execute(query)
    query='select date,hospital,doctorname,prescription from data2 where usn=%s;'
    mycursor.execute(query,user.get())
    fetchdata=mycursor.fetchall()
    detailwindowttk.delete(*detailwindowttk.get_children())
    print(fetchdata)
    for data in fetchdata:
        datalist=list(data)
        detailwindowttk.insert('',END,values=datalist)




def enterdata():
    window=Toplevel()
    window.geometry("500x400+200+200")
    window.resizable(0,0)
    window.title('Data Entry')
    def connectdatabase():
        if dateentry.get()=='' or doctorentry.get()=='' or hospitalentry.get()=='' or prescriptionentry.get()=='':
            messagebox.showerror('ERROR','All fields must be filled')
        else:
            try:
                conn=pymysql.connect(host='localhost',user='root',password='dhan@32952')
                mycursor=conn.cursor()
            except:
                messagebox.showerror('ERROR','Database connectivity issues' )
                return
            query='use signupdata;'
            mycursor.execute(query)
            insertquery='insert into data2(usn,date,hospital,doctorname,prescription)values(%s,%s,%s,%s,%s);'
            mycursor.execute(insertquery,(user.get(),dateentry.get(),hospitalentry.get(),doctorentry.get(),prescriptionentry.get()))
            conn.commit()
            result=messagebox.showinfo('Success','data successfully added')
            if result:
                dateentry.delete(0,END)
                hospitalentry.delete(0,END)
                doctorentry.delte(0,END)
                prescriptionentry.delete(0,END)
            

             


            

        

    datelabel=Label(window,text='Date',font='comicsansms 18 bold',fg='black',bg='white',bd=0)
    datelabel.place(x=50,y=23)

    colonlabel=Label(window,text=':',font=17)
    colonlabel.place(x=180,y=23)

    dateentry=Entry(window,font='aerial 16 bold',fg='#000000',bg='firebrick1',bd=0)
    dateentry.place(x=220,y=25)

    hospitallabel=Label(window,text='Hospital Name',font='comicsansms 18 bold',fg='black',bg='white',bd=0)
    hospitallabel.place(x=0,y=80)

    colonlabel1=Label(window,text=':',font=17)
    colonlabel1.place(x=181,y=80)

    hospitalentry=Entry(window,font='aerial 16 bold',fg='#000000',bg='firebrick1',bd=0)
    hospitalentry.place(x=220,y=80)
    
    doctorlabel=Label(window,text="Doctor's Name",font='comicsansms 18 bold',fg='black',bg='white',bd=0)
    doctorlabel.place(x=0,y=138)

    colonlabel2=Label(window,text=':',font=17)
    colonlabel2.place(x=181,y=138)

    doctorentry=Entry(window,font='aerial 16 bold',fg='#000000',bg='firebrick1',bd=0)
    doctorentry.place(x=220,y=138)

    prescriptionlabel=Label(window,text="Prescription",font='comicsansms 18 bold',fg='black',bg='white',bd=0)
    prescriptionlabel.place(x=10,y=195)

    colonlabe3=Label(window,text=':',font=17)
    colonlabe3.place(x=181,y=195)

    prescriptionentry=Entry(window,font='aerial 16 bold',fg='#000000',bg='firebrick1',bd=0)
    prescriptionentry.place(x=220,y=195)

    connectbutton=Button(window,text='uploaad files',width=18,height=2,fg='#434343',bg='#3d85c6',activeforeground='#434343',activebackground='#3d85c6',command=connectdatabase)
    connectbutton.place(x=160,y=265)

showdetailsbutton=Button(nextpage,text='show details',width=15,height=1,fg='#000000',bg='white',font='comicsansms 10',cursor='hand2',command=showdetail)
showdetailsbutton.place(x=80,y=120)


searchbutton=Button(nextpage,text='search details',width=15,height=1,fg='#000000',bg='white',font='comicsansms 10',cursor='hand2',command=searchdetail)
searchbutton.place(x=80,y=202)



    






    

 

addinfobutton=Button(nextpage,text="Add Info",width=15,height=1,fg="#000000",bg='white',font='comicsansms 10',cursor='hand2',command=enterdata)
addinfobutton.place(x=80,y=40)









    






nextpage.mainloop()