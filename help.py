from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Helpdesk :
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1545x795+0+0")
        self.root.title("Help Desk")
        
        title_lbl = Label(self.root,text="HELP  DESK" , font=("times new roman" , 35 , "bold") , bg="white" , fg="green")
        title_lbl.place(x=0,y=0,width=1545,height=45)
        
        img_top = Image.open("D:/Student Attendence System/images/hd.png")
        img_top = img_top.resize((1545,750),Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1545,height=750)
        
        email_label = Label(f_lbl,text="Email : vpp7541@gmail.com",font=("times new roman",20,"bold"),fg="blue",bg="white")
        email_label.place(x=1150,y=670)
        
if __name__ == "__main__" :
    root = Tk()
    obj = Helpdesk(root)
    root.mainloop()