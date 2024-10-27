from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from register import Register
from main import Face_Recognition_System

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1545x795+0+0")
        
        # self.bg = ImageTk.PhotoImage(file="D:/Student Attendence System/images/loginbg.png")
        # lbl_bg = Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        img_bg = Image.open("D:/Student Attendence System/images/loginbg.png")
        img_bg = img_bg.resize((1545,795),Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        f_lbl = Label(self.root,image=self.photoimg_bg)
        f_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame = Frame(self.root,bg="black")
        frame.place(x=600,y=170,width=340,height=450)
        
        logo = Image.open("D:/Student Attendence System/images/loginlogo.png")
        logo = logo.resize((100,100),Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(logo)
        lbllogo = Label(image=self.photoimage,bg="black",borderwidth=0)
        lbllogo.place(x=725,y=175,width=100,height=100)
        
        get_str = Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=100)
        
        username_lbl = Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)
        
        self.txtuser = ttk.Entry(frame,font=("times new roman",12,"bold"))
        self.txtuser.place(x=40,y=185,width=260,height=30)
        
        password_lbl = Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=70,y=230)
        
        self.txtpass = ttk.Entry(frame,font=("times new roman",12,"bold"))
        self.txtpass.place(x=40,y=260,width=260,height=30)
        
        icon1 = Image.open("D:/Student Attendence System/images/icon1.png")
        icon1 = icon1.resize((25,25),Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(icon1)
        lblicon = Label(frame,image=self.photoimage1,bg="black",borderwidth=0)
        lblicon.place(x=40,y=157,width=25,height=25)
        
        icon2 = Image.open("D:/Student Attendence System/images/icon2.png")
        icon2 = icon2.resize((25,25),Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(icon2)
        lblicon = Label(frame,image=self.photoimage2,bg="black",borderwidth=0)
        lblicon.place(x=40,y=232,width=25,height=25)
        
        loginbtn = Button(frame,text="Login",command=self.login,font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="gray",activeforeground="white",activebackground="gray")
        loginbtn.place(x=40,y=310,width=260,height=35)
        
        ortxt_lbl = Label(frame,text="Forgot",font=("times new roman",10,"bold"),fg="white",bg="black")
        ortxt_lbl.place(x=110,y=360)
        
        forgotpassbtn = Button(frame,command=self.forgot_pswd_window,text="Password ?",font=("times new roman",12,"bold"),borderwidth=0,fg="blue",bg="black",activeforeground="blue",activebackground="black")
        forgotpassbtn.place(x=152,y=353,height=35)
        
        ortxt_lbl = Label(frame,text="Do not have an account ?",font=("times new roman",10,"bold"),fg="white",bg="black")
        ortxt_lbl.place(x=60,y=385)
        
        registerbtn = Button(frame,command=self.register_window,text="Register",font=("times new roman",12,"bold"),borderwidth=0,fg="blue",bg="black",activeforeground="blue",activebackground="black")
        registerbtn.place(x=200,y=378,height=35)
    
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required!")
        # elif self.txtuser.get()=="vidhi" and self.txtpass.get()=="patel":
        #     messagebox.showinfo("Success","Login successfully!")
        else:
            # messagebox.showerror("Invalid","Invalid username & password")
            conn = mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid Username & Password!",parent=self.root)
            else:
                open_main = messagebox.askyesno("YesNo","Access only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            
    def reset_pswd(self):
        if self.security_Q_combo.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.security_A_entry.get()=="":
            messagebox.showerror("Error","Please enter the security answer",parent=self.root2)
        elif self.new_pswd_entry.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition")
            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE email=%s and securityQ=%s and securityA=%s")
            value = (self.txtuser.get(),self.security_Q_combo.get(),self.security_A_entry.get())
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query = ("UPDATE register SET password=%s WHERE email=%s")
                value = (self.new_pswd_entry.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login new password!",parent=self.root2)
                self.root2.destroy()
            
    def forgot_pswd_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email id to reset password",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition")
            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("Error","Please enter the valid username!",parent=self.root2)
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("350x450+590+170")
                
                l = Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                security_Q_lbl = Label(self.root2,text="Select Security Quetions",font=("times new roman",15,"bold"))
                security_Q_lbl.place(x=50,y=80)
                self.security_Q_combo = ttk.Combobox(self.root2,font=("times new roman",12),state="readonly",width=250)
                self.security_Q_combo["values"]=("Select","Your Birth Place","Your Mother Name","Your Bestfriend Name")
                self.security_Q_combo.current(0)
                self.security_Q_combo.place(x=50,y=110,width=250)
                
                security_A_lbl = Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"))
                security_A_lbl.place(x=50,y=150)
                self.security_A_entry = ttk.Entry(self.root2,font=("times new roman",12))
                self.security_A_entry.place(x=50,y=180,width=250)
                
                new_pswd_lbl = Label(self.root2,text="New Password",font=("times new roman",15,"bold"))
                new_pswd_lbl.place(x=50,y=220)
                self.new_pswd_entry = ttk.Entry(self.root2,font=("times new roman",12))
                self.new_pswd_entry.place(x=50,y=250,width=250)
                
                btn = Button(self.root2,command=self.reset_pswd,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="gray")
                btn.place(x=130,y=320,width=100)
   
class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1545x795+0+0")
        
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pswd = StringVar()
        self.var_confpswd = StringVar()
        
        # self.bg = ImageTk.PhotoImage(file="D:/Student Attendence System/images/loginbgi.png")
        # lbl_bg = Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        img_bg = Image.open("D:/Student Attendence System/images/loginbg.png")
        img_bg = img_bg.resize((1545,795),Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        bg_lbl = Label(self.root,image=self.photoimg_bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        img_left = Image.open("D:/Student Attendence System/images/rleftimg.png")
        img_left = img_left.resize((600,595),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        lefti_lbl = Label(self.root,image=self.photoimg_left)
        lefti_lbl.place(x=100,y=100,width=600,height=595)
        
        frame = Frame(self.root,bg="white")
        frame.place(x=700,y=100,width=720,height=595)
        
        register_lbl = Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
        
        fname_lbl = Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname_lbl.place(x=70,y=100)
        fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname_entry.place(x=70,y=130,width=250)
        
        lname_lbl = Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname_lbl.place(x=390,y=100)
        lname_entry = ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        lname_entry.place(x=390,y=130,width=250)
        
        contact_lbl = Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact_lbl.place(x=70,y=180)
        contact_entry = ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        contact_entry.place(x=70,y=210,width=250)
        
        email_lbl = Label(frame,text="Email Id",font=("times new roman",15,"bold"),bg="white")
        email_lbl.place(x=390,y=180)
        email_entry = ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        email_entry.place(x=390,y=210,width=250)
        
        security_Q_lbl = Label(frame,text="Select Security Quetions",font=("times new roman",15,"bold"),bg="white")
        security_Q_lbl.place(x=70,y=260)
        security_Q_combo = ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15),state="readonly",width=250)
        security_Q_combo["values"]=("Select","Your Birth Place","Your Mother Name","Your Bestfriend Name")
        security_Q_combo.current(0)
        security_Q_combo.place(x=70,y=290,width=250)
        
        security_A_lbl = Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A_lbl.place(x=390,y=260)
        security_A_entry = ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        security_A_entry.place(x=390,y=290,width=250)
        
        pswd_lbl = Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd_lbl.place(x=70,y=340)
        pswd_entry = ttk.Entry(frame,textvariable=self.var_pswd,font=("times new roman",15))
        pswd_entry.place(x=70,y=370,width=250)
        
        conf_pswd_lbl = Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        conf_pswd_lbl.place(x=390,y=340)
        conf_pswd_entry = ttk.Entry(frame,textvariable=self.var_confpswd,font=("times new roman",15))
        conf_pswd_entry.place(x=390,y=370,width=250)
        
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I agree the term & condition",font=("times new roman",15),onvalue=1,offvalue=0)
        checkbtn.place(x=70,y=430)
        
        img_register = Image.open("D:/Student Attendence System/images/registerbtn.png")
        img_register = img_register.resize((150,35),Image.LANCZOS)
        self.photoimg_register = ImageTk.PhotoImage(img_register)
        register_lbl = Button(frame,command=self.register_data,image=self.photoimg_register,borderwidth=0,cursor="hand2",bg="white")
        register_lbl.place(x=205,y=500,width=150,height=35)
        
        img_login = Image.open("D:/Student Attendence System/images/loginbtn.png")
        img_login = img_login.resize((150,35),Image.LANCZOS)
        self.photoimg_login = ImageTk.PhotoImage(img_login)
        login_lbl = Button(frame,command=self.return_login,image=self.photoimg_login,borderwidth=0,cursor="hand2",bg="white")
        login_lbl.place(x=365,y=500,width=150,height=35)
        
    def register_data(self):
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_securityA.get()=="" or self.var_pswd.get()=="" or self.var_confpswd.get()=="") :
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pswd.get()!=self.var_confpswd.get():
            messagebox.showerror("Error","Password & Confirm Password must be same!")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our term & condition!")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition")
            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","User already exist, please try another email")
            else:
                my_cursor.execute("INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pswd.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully!")  
    
    def return_login(self):
        self.root.destroy()      
        
if __name__ == "__main__":
    main()