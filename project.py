from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
def loginuser():
    if userentry.get()=='' or passentry.get()=='':
        messagebox.showerror('ERROR','All fields must be filled')
    elif userentry.get()=='USERNAME' or passentry.get()=='PASSWORD':
        messagebox.showerror('ERROR','All fields must be filled')
    else:
        try:
            conn=pymysql.connect(host='localhost',user='root',password='dhan@32952')
            mycursor=conn.cursor()
        except:
            messagebox.showerror('ERROR','Database connectivity issues,please try again')
            return
        
        query='use signupdata'
        mycursor.execute(query)


        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(userentry.get(),passentry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('ERROR','Wrong username and password')
            
        else:
            messagebox.showinfo('SUCCESS','Login Successfull')
            import nextpage




           
    
    
           
            
            

def onenter(event):
    if userentry.get()=='USERNAME':
        userentry.delete(0,END)
def twoentry(event2):
    if passentry.get()=='PASSWORD':
        passentry.delete(0,END)
def hide():
    openeye.config(file='closeye.png')
    passentry.config(show='*')
    eyebutton.config(command=show)
def show():
    openeye.config(file='openeye.png')
    passentry.config(show='')
    eyebutton.config(command=hide)
def signuppage():
    login_window.destroy()
    import signup


login_window=Tk()
login_window.geometry("990x660+50+50")
login_window.resizable(0,0)
login_window.title("login page")
bgImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

headLabel=Label(login_window,text="USER LOGIN",font=("comicsansms 25 bold "),bg="white",fg="#ea9999")
headLabel.place(x=600,y=115)

userentry=Entry(login_window,font="aerial 13 bold",fg="#434343",bd=0)
userentry.place(x=600,y=200,width=210,height=25)
userentry.insert(0,'USERNAME')
userentry.bind('<FocusIn>',onenter)


frame1=Frame(login_window,width=220,height=2,bg="#e06666")
frame1.place(x=600,y=226)

passentry=Entry(login_window,font="aerial 13 bold",fg="#434343",bd=0)
passentry.place(x=600,y=270,width=210,height=25)
passentry.insert(0,'PASSWORD')
passentry.bind('<FocusIn>',twoentry)
openeye=PhotoImage(file='openeye.png')
eyebutton=Button(login_window,image=openeye,bd=0,bg="white",cursor='hand2',command=hide)
eyebutton.place(x=785,y=273)

frame2=Frame(login_window,width=220,height=2,bg="#e06666")
frame2.place(x=600,y=298)


forgetbutton=Button(login_window,text="Forget Password?",bd=0,bg="white",cursor='hand2',fg="#ea6666")
forgetbutton.place(x=730,y=320)
frame3=Frame(login_window,width=98,bg="#ea6666")
frame3.place(x=730,y=340)

loginbutton=Button(login_window,text="LOGIN",width=18,height=1,font="aerial 15 bold",activeforeground='white',activebackground='firebrick1',bg='firebrick1',bd=0,fg='white',command=loginuser)
loginbutton.place(x=600,y=370)

orlabel=Label(login_window,text="------------OR------------",font='aerial 16 bold',bd=0,bg='white',fg='firebrick1')
orlabel.place(x=610,y=430)

createacc=Label(login_window,text="Dont have an account?",font="opensans 8 bold",bg='white',fg='firebrick1',bd=0)
createacc.place(x=610,y=485)

createbutton=Button(login_window,text="Create One",font='aerial 9 bold',bg='white',fg='blue',bd=0,cursor='hand2',command=signuppage)
createbutton.place(x=745,y=482)

frame4=Frame(login_window,width=65,height=2,bg='blue')
frame4.place(x=748,y=500)



login_window.mainloop()
