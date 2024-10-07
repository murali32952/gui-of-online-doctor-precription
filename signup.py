from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import messagebox

def clear():
    emailentry.delete(0,END)
    userentry.delete(0,END)
    passentry.delete(0,END)
    confirmpassentry.delete(0,END)
    check.set(0)

def connectdatabase():
    if emailentry.get()=='' or userentry.get()=='' or passentry.get()=='' or confirmpassentry.get()=='':
        messagebox.showerror('ERROR','All boxes must be filled')
    elif passentry.get()!=confirmpassentry.get():
        messagebox.showerror('ERROR','password and confirm password are not matching')
    elif check.get()==0:
        messagebox.showerror('ERROR','Must agree to terms and conditions')
    else:
        try:
            conn=pymysql.connect(host='localhost',user='root',password='dhan@32952')
            mycursor=conn.cursor()
        except:
            messagebox.showerror('ERROR','Database Connectivity Issue,Please try again')
            return
        
        query='use signupdata'
        mycursor.execute(query)


        
        email=emailentry.get()
        username=userentry.get()
        password=passentry.get()

        query='select * from data where username=%s'
        mycursor.execute(query,(userentry.get()))
        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror('ERROR','Username already exists')
        else:
            insertquery="insert into data(email,username,password)values(%s,%s,%s)"
            vals=(email,username,password)
            mycursor.execute(insertquery,vals)
            conn.commit()
        
            conn.close()
            messagebox.showinfo('SUCCESS','Database has been updated')
            clear()
            signup.destroy()
            import project

        


def loginpage():
    signup.destroy()
    import project

def hide1():
    closeeye.config(file='openeye.png')
    confirmpassentry.config(show='')
    eyebutton.config(command=show1)
def show1():
    closeeye.config(file='closeye.png')
    confirmpassentry.config(show='*')
    eyebutton.config(command=hide1)    
signup=Tk()
signup.geometry("790x512")
signup.title('sign up')
backgrnd=ImageTk.PhotoImage(file='background.jpg')
backgrndimage=Label(signup,image=backgrnd)
backgrndimage.place(x=0,y=0)
signup.resizable(0,0)

createlabel=Label(signup,text="CREATE AN ACCOUNT",font='comicsansms 18 bold',bg='white',fg='firebrick1',bd=0)
createlabel.place(x=470,y=57)

emaillabel=Label(signup,text='Email',fg='firebrick1',font='aerial 12 bold')
emaillabel.place(x=470,y=115)

emailentry=Entry(signup,bg='#ea6666',fg='#000000',font='aerial 13 bold')
emailentry.place(x=473,y=145,width=250,height=25)

userlabel=Label(signup,text='Username',bg='white',fg='firebrick1',font='aerial 12 bold')
userlabel.place(x=470,y=188)

userentry=Entry(signup,bg='#ea6666',fg='#000000',font='aerial 13 bold')
userentry.place(x=473,y=214,width=250,height=25)

passlabel=Label(signup,text='Password',bg='white',fg='firebrick1',font='aerial 12 bold')
passlabel.place(x=470,y=258)

passentry=Entry(signup,bg='#ea6666',fg='#000000',font='aerial 13 bold')
passentry.place(x=473,y=288,width=250,height=25)

confirmpasslabel=Label(signup,text='Confirm Password',bg='white',fg='firebrick1',font='aerial 12 bold')
confirmpasslabel.place(x=470,y=330)

confirmpassentry=Entry(signup,bg='#ea6666',fg='#000000',font='aerial 13 bold')
confirmpassentry.place(x=473,y=360,width=250,height=25)
check=IntVar()
termandconditions=Checkbutton(signup,text='i agree to the term and conditions',bg='white',fg='firebrick1',font='aerial 10 bold',variable=check)
termandconditions.place(x=468,y=395)

signupbutton=Button(signup,text='SIGN UP',bg='firebrick1',fg='white',activebackground='white',activeforeground='firebrick1',font='comicsansms 16',bd=0,command=connectdatabase)
signupbutton.place(x=473,y=435,width=230,height=30)

alreadyacclabel=Label(signup,text='Already have an account?',fg='firebrick1',font='aerial 9 bold',bd=0)
alreadyacclabel.place(x=473,y=478)

loginbutton=Button(signup,text='Log in',bg='white',fg='blue',bd=0,font='aerial 10 bold',cursor='hand2',command=loginpage)
loginbutton.place(x=625,y=473)



closeeye=PhotoImage(file='closeye.png')
eyebutton=Button(signup,image=closeeye,bd=0,bg='white',command=show1)
eyebutton.place(x=700,y=363,width=20,height=18)










signup.mainloop()
