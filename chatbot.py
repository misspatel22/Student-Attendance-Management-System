from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class ChatBot:
    def __init__(self,root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("730x620+100+50")
        self.root.bind('<Return>',self.enter_func)
        
        main_frame = Frame(self.root,bd=2,bg='powder blue',width=610)
        main_frame.pack()
        
        img_chat = Image.open('images/bot.png')
        img_chat = img_chat.resize((200,70),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)
        
        title_label = Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text="CHAT ME",font=('arial',30,'bold'),fg='green',bg='white')
        title_label.pack(side=TOP)
        
        self.scroll_y = ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text = Text(main_frame,width=65,height=20,bd=2,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()
        
        btn_frame = Frame(self.root,bd=2,bg='white',width=730)
        btn_frame.pack()
        
        lbl_label = Label(btn_frame,text="Type Something...",font=('arial',14,'bold'),fg='green',bg='white')
        lbl_label.grid(row=0,column=0,padx=5,sticky=W)
        
        self.entry_var = StringVar()
        self.entry = ttk.Entry(btn_frame,textvariable=self.entry_var,width=40,font=('arial',14))
        self.entry.grid(row=0,column=1,padx=5,sticky=W)
        
        self.send = Button(btn_frame,text="Send",command=self.send,font=('arial',14,'bold'),width=5,bg='green',cursor="hand2")
        self.send.grid(row=0,column=2,padx=5,sticky=W)
        
        self.clear = Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',14,'bold'),width=10,bg='red',cursor="hand2")
        self.clear.grid(row=1,column=0,padx=5,sticky=W)
        
        self.msg=''
        self.err_label = Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.err_label.grid(row=1,column=1,padx=5,sticky=W)
    
    def enter_func(self,event):
        self.send.invoke()
        self.entry_var.set('')    
    
    def send(self):
        send = '\t'+"You : "+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)
        
        if(self.entry_var.get()==''):
            self.msg = "Please enter some input"
            self.err_label.config(text=self.msg,fg='red')
            
        else:
            self.msg=''
            self.err_label.config(text=self.msg,fg='red')
            
        if(self.entry_var.get()=="Hello"):
            self.text.insert(END,'\n'+'\t'+"Bot : Hello! How are you?")
            
        elif(self.entry_var.get()=="Hii"):
            self.text.insert(END,'\n'+'\t'+"Bot : Hii! How are you?")
        
        elif(self.entry_var.get()=="Hey"):
            self.text.insert(END,'\n'+'\t'+"Bot : Hey! How are you?")
        
        elif(self.entry_var.get()=="Good Morning"):
            self.text.insert(END,'\n'+'\t'+"Bot : Good Morning")
        
        elif(self.entry_var.get()=="Good Afternoon"):
            self.text.insert(END,'\n'+'\t'+"Bot : Good Afternoon")
        
        elif(self.entry_var.get()=="Good Evening"):
            self.text.insert(END,'\n'+'\t'+"Bot : Good Evening")
        
        elif(self.entry_var.get()=="Good Night"):
            self.text.insert(END,'\n'+'\t'+"Bot : Good Night")
            
        elif(self.entry_var.get()=="I am good. How are you?"):
            self.text.insert(END,'\n'+'\t'+"Bot : I am doing well, thank you! Ready to help you with anything you need. What’s up?")
        
        elif(self.entry_var.get()=="I need help about face recognition based student attendance management system."):
            self.text.insert(END,'\n'+'\t'+"Bot : What specific question do you have about the Face Recognition based Student Attendance Management System?")
        
        elif(self.entry_var.get()=="What is a Face Recognition based Student Attendance Management System?"):
            self.text.insert(END,'\n'+'\t'+"Bot : A system that uses facial recognition technology to identify and verify students' identities and mark their attendance automatically.")
        
        elif(self.entry_var.get()=="How does facial recognition work in this system?"):
            self.text.insert(END,'\n'+'\t'+"Bot : Facial recognition works by capturing an image of the student’s face, extracting key facial features (like the distance between the eyes, nose width, etc.), and comparing those features with the existing database of student images for authentication.")
        
        elif(self.entry_var.get()=="Which algorithm is commonly used for face recognition?"):
            self.text.insert(END,'\n'+'\t'+"Bot : Haar Cascade for face detection, LBPH (Local Binary Pattern Histogram) for simple face recognition")
        
        elif(self.entry_var.get()=="What are the main advantages of using facial recognition for attendance?"):
            self.text.insert(END,'\n'+'\t'+"Bot : Attendance is marked quickly without manual effort, Reduces the chances of errors like proxy attendance, Only authorized individuals are allowed, Fully automated process without manual intervention.")
        
        elif(self.entry_var.get()=="How is the attendance data stored and managed?"):
            self.text.insert(END,'\n'+'\t'+"Bot : Attendance data is usually stored in a database like MySQL, PostgreSQL, or MongoDB. Each student's facial data (converted to mathematical representations) and their attendance status (date and time) are saved and can be retrieved or reported later.")
        
        elif(self.entry_var.get()=="Okay, Thanks"):
            self.text.insert(END,'\n'+'\t'+"Bot : You're welcome! If you have any more questions or need further assistance, feel free to ask. Good luck with your project!")
        
        elif(self.entry_var.get()=="Okay, Thanks for help"):
            self.text.insert(END,'\n'+'\t'+"Bot : Anytime! If you have more questions or need help with anything else, just let me know. I'm here to help!")
        
        elif(self.entry_var.get()=="Okay"):
            self.text.insert(END,'\n'+'\t'+"Bot : Okay, Have a great day!")
        
        elif(self.entry_var.get()=="Yaa, Thanks"):
            self.text.insert(END,'\n'+'\t'+"Bot : No problem! Enjoy your day!")
        
        elif(self.entry_var.get()=="Yes"):
            self.text.insert(END,'\n'+'\t'+"Bot : Great!")
        
        elif(self.entry_var.get()=="Nice talking with you"):
            self.text.insert(END,'\n'+'\t'+"Bot : Thank you! It was nice talking with you too. Take care, and see you next time!")
        
        elif(self.entry_var.get()=="Bye"):
            self.text.insert(END,'\n'+'\t'+"Bot : Goodbye!")
        
        else:
            self.text.insert(END,'\n'+'\t'+"Bot : Sorry I didn't get it")
            
        self.entry_var.set('')
            
    def clear(self):
        self.text.delete('1.0',END)
        self.entry_var.set('')
        
if __name__ == '__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()