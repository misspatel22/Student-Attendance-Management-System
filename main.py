from tkinter import*
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime
from student import Student
from traindata import Traindata
from facedetector import FaceDetector
from attendance import Attendance
from chatbot import ChatBot
from help import Helpdesk

class Face_Recognition_System :
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1545x790+0+0")
        self.root.title("Face Recognition System")
        
        img1 = Image.open("D:/Student Attendence System/images/img1.png")
        img1 = img1.resize((515,130),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=515,height=130)
        
        img2 = Image.open("D:/Student Attendence System/images/img2.png")
        img2 = img2.resize((515,130),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=515,y=0,width=515,height=130)
        
        img3 = Image.open("D:/Student Attendence System/images/img3.png")
        img3 = img3.resize((515,130),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1030,y=0,width=515,height=130)
        
        bgimg = Image.open("D:/Student Attendence System/images/bgimg.png")
        bgimg = bgimg.resize((1545,790),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(bgimg)
        bg_img = Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=130,width=1545,height=790)
        
        title_lbl = Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM  SOFTWARE" , font=("times new roman" , 35 , "bold") , bg="white" , fg="red")
        title_lbl.place(x=0,y=0,width=1545,height=45)
        
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
            
        lbl = Label(bg_img,font=('times new romaan',12,'bold'),background='darkblue',foreground='white')
        lbl.place(x=1413,y=45,width=120,height=50)
        time()
        
        img4 = Image.open("D:/Student Attendence System/images/img4.png")
        img4 = img4.resize((220,220),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img , image=self.photoimg4 , command=self.student_details , cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        b1_1 = Button(bg_img , text="Student Details" , command=self.student_details , cursor="hand2" , font=("times new roman" , 15 , "bold") , bg="darkblue" , fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        img5 = Image.open("D:/Student Attendence System/images/img5.png")
        img5 = img5.resize((220,220),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img , image=self.photoimg5 , command=self.face_detector , cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)
        b1_1 = Button(bg_img , text="Face Detector", command=self.face_detector , cursor="hand2" , font=("times new roman" , 15 , "bold") , bg="darkblue" , fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        img6 = Image.open("D:/Student Attendence System/images/img6.png")
        img6 = img6.resize((220,220),Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img , image=self.photoimg6 , command=self.std_attendance , cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)
        b1_1 = Button(bg_img , text="Attendance" , command=self.std_attendance , cursor="hand2" , font=("times new roman" , 15 , "bold") , bg="darkblue" , fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        img7 = Image.open("D:/Student Attendence System/images/img7.png")
        img7 = img7.resize((220,220),Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img , image=self.photoimg7 , command=self.help_desk , cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)
        b1_1 = Button(bg_img , text="Help Desk" , command=self.help_desk , cursor="hand2" , font=("times new roman" , 15 , "bold") , bg="darkblue" , fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        img8 = Image.open("D:/Student Attendence System/images/img8.png")
        img8 = img8.resize((220,220),Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img , image=self.photoimg8 , command=self.train_data , cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)
        b1_1 = Button(bg_img , text="Train Data" , command=self.train_data , cursor="hand2" , font=("times new roman" , 15 , "bold") , bg="darkblue" , fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)
        
        img9 = Image.open("D:/Student Attendence System/images/img9.png")
        img9 = img9.resize((220,220),Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_img , image=self.photoimg9 , command=self.open_img , cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)
        b1_1 = Button(bg_img , text="Photos" , command=self.open_img , cursor="hand2" , font=("times new roman" , 15 , "bold") , bg="darkblue" , fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)
        
        img10 = Image.open("D:/Student Attendence System/images/img10.png")
        img10 = img10.resize((220,220),Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img , image=self.photoimg10 , command=self.chatbot, cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)
        b1_1 = Button(bg_img , text="ChatBot" , cursor="hand2" , font=("times new roman" , 15 , "bold") , bg="darkblue" , fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        img11 = Image.open("D:/Student Attendence System/images/img11.png")
        img11 = img11.resize((220,220),Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b1 = Button(bg_img , image=self.photoimg11 , command=self.exit , cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)
        b1_1 = Button(bg_img , text="Exit" , command=self.exit , cursor="hand2" , font=("times new roman" , 15 , "bold") , bg="darkblue" , fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)
        
    def student_details(self):
        self. new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def open_img(self):
        os.startfile("data")
        
    def train_data(self):
        self. new_window=Toplevel(self.root)
        self.app=Traindata(self.new_window)
        
    def face_detector(self):
        self. new_window=Toplevel(self.root)
        self.app=FaceDetector(self.new_window)
        
    def std_attendance(self):
        self. new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def chatbot(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)
        
    def help_desk(self):
        self. new_window=Toplevel(self.root)
        self.app=Helpdesk(self.new_window)
        
    def exit(self):
        self.exit = tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project !?",parent=self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return
        
if __name__ == "__main__" :
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()