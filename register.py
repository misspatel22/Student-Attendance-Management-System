from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

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
    root = Tk()
    app = Register(root)
    root.mainloop()