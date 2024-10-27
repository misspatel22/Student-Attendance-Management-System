from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Traindata :
    
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1545x795+0+0")
        self.root.title("Train Data")
        
        title_lbl = Label(self.root,text="TRAIN  DATA  SET" , font=("times new roman" , 35 , "bold") , bg="white" , fg="green")
        title_lbl.place(x=0,y=0,width=1545,height=45)
        
        img_top = Image.open("D:/Student Attendence System/images/td2.png")
        img_top = img_top.resize((1545,353),Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1545,height=353)
        
        btn = Button(self.root , text="Train Data" , command=self.train_classifier , cursor="hand2" , font=("times new roman" , 20 , "bold") , bg="darkblue" , fg="white")
        btn.place(x=0,y=395,width=1545,height=45)
        
        img_bottom = Image.open("D:/Student Attendence System/images/td2.png")
        img_bottom = img_top.resize((1545,353),Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1545,height=353)
        
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Train Data",imageNp)
            cv2.waitKey(1) == 13
            
        ids = np.array(ids)
        
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")
        
if __name__ == "__main__" :
    root = Tk()
    obj = Traindata(root)
    root.mainloop()