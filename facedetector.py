from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class FaceDetector :
    
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1545x795+0+0")
        self.root.title("Face Detector")
        
        title_lbl = Label(self.root,text="FACE  DETECTOR" , font=("times new roman" , 35 , "bold") , bg="white" , fg="green")
        title_lbl.place(x=0,y=0,width=1545,height=45)
        
        img_left = Image.open("D:/Student Attendence System/images/facedetector1.png")
        img_left = img_left.resize((650,750),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=0,y=45,width=650,height=750)
        
        img_right = Image.open("D:/Student Attendence System/images/facedetector.png")
        img_right = img_right.resize((895,750),Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=650,y=45,width=895,height=750)
        
        btn = Button(f_lbl , text="Face Detect" , command=self.face_detect , cursor="hand2" , font=("times new roman" , 15 , "bold") , bg="darkblue" , fg="white")
        btn.place(x=345,y=660,width=200,height=40)

    def mark_attendance(self,i,n,r,d):
        with open("Student_Data.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (r not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{r},{d},{dtString},{d1},Present")
        
    def face_detect(self):
        
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord = []
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int(100*(1-predict/300))
                conn = mysql.connector.connect(host="localhost",username="root",password="",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Id FROM student WHERE Id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)
                my_cursor.execute("SELECT Name FROM student WHERE Id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)
                my_cursor.execute("SELECT RollNo FROM student WHERE Id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)
                my_cursor.execute("SELECT Department FROM student WHERE Id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)
                if confidence>77:
                    cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"RollNo:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_attendance(i,n,r,d)
                else :
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord = [x,y,w,h]
            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)
        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face detector",img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        
if __name__ == "__main__" :
    root = Tk()
    obj = FaceDetector(root)
    root.mainloop()