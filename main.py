from tkinter import*
from tkinter import ttk  
# ttk is import because it has some stylish tookit
from PIL import Image,ImageTk  
#pillow is used for images and imagestk for croping images etc
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root  #here we initialize the root
        #now from below we will set the geometry of the application
        self.root.geometry("1530x790+0+0")
        #1530=width,790=height,0from x axis (left corner to right) and 0 from y axis
        self.root.title("Face Recognition System")

        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\face-recognition-system\college_images\BestFacialRecognition.jpg")
        
        #r is used for changing the front slash into back slask bcauz python understand back slash
        #img is variable
        img=img.resize((500,130),Image.ANTIALIAS)
        #antialias convert high level image into low level
        self.photoimg=ImageTk.PhotoImage(img)

        #to set this img we are setting label below
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        #we are providing geometry how the image should show


        #we need 3 images like that. hence we are re creating this method twice


        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\face-recognition-system\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        

        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\face-recognition-system\college_images\images.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        

        #background image
        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\face-recognition-system\college_images\bgimg.jpg")
        img3=img3.resize((1550,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #student button
        img4=Image.open(r"C:\Users\HP\OneDrive\Desktop\face-recognition-system\college_images\student.jpg")
        img4=img4.resize((220,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        #this below code is used for the button 
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


        #Detect Face button
        img5=Image.open(r"C:\Users\HP\OneDrive\Desktop\face-recognition-system\college_images\face_detector1.jpg")
        img5=img5.resize((220,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        #this below code is used for the button 
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)



        #Attendance Face button
        img6=Image.open(r"C:\Users\HP\OneDrive\Desktop\face-recognition-system\college_images\report.jpg")
        img6=img6.resize((220,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        #this below code is used for the button 
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        #Help Face button
        img7=Image.open(r"C:\Users\HP\OneDrive\Desktop\face-recognition-system\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7=img7.resize((220,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        #this below code is used for the button 
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)


         #Train Face button
        img8=Image.open(r"college_images\Train.jpg")
        img8=img8.resize((220,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        #this below code is used for the button 
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)


         #Photos Face button
        img9=Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((220,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        #this below code is used for the button 
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos ",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)


        #Developers Face button
        img10=Image.open(r"college_images\Team-Management-Software-Development.jpg")
        img10=img10.resize((220,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        #this below code is used for the button 
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developers ",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)



        #Exit Face button
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((220,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        #this below code is used for the button 
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit ",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")

        
#=========Functions Button=======

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)  #here we created object of the class
    root.mainloop()
    #after running till this we get the background window of the screen