from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance :
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1545x795+0+0")
        self.root.title("Student Attendance")
        
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_dept = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_status = StringVar()
        
        title_lbl = Label(self.root,text="STUDENT  ATTENDANCE" , font=("times new roman" , 35 , "bold") , bg="white" , fg="green")
        title_lbl.place(x=0,y=0,width=1545,height=45)
        
        img_left = Image.open("D:/Student Attendence System/images/sa2.png")
        img_left = img_left.resize((800,200),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=800,height=200)
        
        img_right = Image.open("D:/Student Attendence System/images/sa3.png")
        img_right = img_right.resize((800,200),Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=800,y=0,width=800,height=200)
        
        bgimg = Image.open("D:/Student Attendence System/images/bgimg.png")
        bgimg = bgimg.resize((1545,595),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(bgimg)
        bg_img = Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=200,width=1545,height=595)
        
        title_lbl = Label(bg_img,text="STUDENT  ATTENDANCE  SYSTEM" , font=("times new roman" , 35 , "bold") , bg="white" , fg="green")
        title_lbl.place(x=0,y=0,width=1545,height=45)
        
        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=25,y=50,width=1480,height=530)
        
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=500)
        
        img1 = Image.open("D:/Student Attendence System/images/sa1.png")
        img1 = img1.resize((715,200),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(Left_frame,image=self.photoimg1)
        f_lbl.place(x=5,y=0,width=715,height=200)
        
        Left_inside_frame = LabelFrame(Left_frame,bd=2,relief=RIDGE)
        Left_inside_frame.place(x=5,y=210,width=715,height=185)
        
        id_label = Label(Left_inside_frame,text="AttendanceId:",font=("times new roman",12,"bold"))
        id_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        
        id_entry = ttk.Entry(Left_inside_frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        id_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        name_label = Label(Left_inside_frame,text="Name:",font=("times new roman",12,"bold"))
        name_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)
        
        name_entry = ttk.Entry(Left_inside_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        name_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)
        
        roll_label = Label(Left_inside_frame,text="RollNo:",font=("times new roman",12,"bold"))
        roll_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        
        roll_entry = ttk.Entry(Left_inside_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        dept_label = Label(Left_inside_frame,text="Department:",font=("times new roman",12,"bold"))
        dept_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)
        
        dept_entry = ttk.Entry(Left_inside_frame,textvariable=self.var_dept,width=20,font=("times new roman",12,"bold"))
        dept_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        
        time_label = Label(Left_inside_frame,text="Time:",font=("times new roman",12,"bold"))
        time_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        
        time_entry = ttk.Entry(Left_inside_frame,textvariable=self.var_time,width=20,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        date_label = Label(Left_inside_frame,text="Date:",font=("times new roman",12,"bold"))
        date_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)
        
        date_entry = ttk.Entry(Left_inside_frame,textvariable=self.var_date,width=20,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)
        
        status_label = Label(Left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"))
        status_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        
        status_combo = ttk.Combobox(Left_inside_frame,textvariable=self.var_status,font=("times new roman",12,"bold"),state="readonly",width=18)
        status_combo["values"]=("Select","Present","Absent")
        status_combo.current(0)
        status_combo.grid(row=3,column=1,padx=10,pady=10)
        
        btn_frame1 = Frame(Left_frame,relief=RIDGE)
        btn_frame1.place(x=5,y=420,width=700,height=40)
        
        import_btn = Button(btn_frame1,text="Import CSV",command=self.import_csv,font=("times new roman",12,"bold"),width=15,bg="#d9d9d9",fg="black")
        import_btn.grid(row=0,column=0,padx=18)
        
        export_btn = Button(btn_frame1,text="Export CSV",command=self.export_csv,font=("times new roman",12,"bold"),width=15,bg="#d9d9d9",fg="black")
        export_btn.grid(row=0,column=1,padx=12)
        
        update_btn = Button(btn_frame1,text="Update",font=("times new roman",12,"bold"),width=15,bg="#d9d9d9",fg="black")
        update_btn.grid(row=0,column=2,padx=12)
        
        reset_btn = Button(btn_frame1,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),width=15,bg="#d9d9d9",fg="black")
        reset_btn.grid(row=0,column=3,padx=12)
        
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=715,height=500)
        
        table_frame = Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=700,height=460)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.attendance_table = ttk.Treeview(table_frame,columns=("id","name","roll","dept","time","date","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)
        
        self.attendance_table.heading("id",text="AttendanceId")
        self.attendance_table.heading("name",text="Name")
        self.attendance_table.heading("roll",text="RollNo")
        self.attendance_table.heading("dept",text="Department")
        self.attendance_table.heading("time",text="Time")
        self.attendance_table.heading("date",text="Date")
        self.attendance_table.heading("status",text="Status")
        
        self.attendance_table["show"] = "headings"
        
        self.attendance_table.column("id",width=100)
        self.attendance_table.column("name",width=100)
        self.attendance_table.column("roll",width=100)
        self.attendance_table.column("dept",width=100)
        self.attendance_table.column("time",width=100)
        self.attendance_table.column("date",width=100)
        self.attendance_table.column("status",width=100)
        
        self.attendance_table.pack(fill=BOTH,expand=1)
        
        self.attendance_table.bind("<ButtonRelease>",self.get_cursor)
        
    def fetch_data(self,rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)
            
    def import_csv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)
            
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to  " + os.path.basename(fln) + " successfully!!")
        except Exception as es:
            messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
            
    def get_cursor(self,event=""):
        cursor_focus = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_focus)
        data = content["values"]
        
        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_roll.set(data[2]),
        self.var_dept.set(data[3]),
        self.var_time.set(data[4]),
        self.var_date.set(data[5]),
        self.var_status.set(data[6])
    
    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_dept.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("Select")

if __name__ == "__main__" :
    root = Tk()
    obj = Attendance(root)
    root.mainloop()