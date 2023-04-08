from tkinter import*
from tkinter import ttk  
# ttk is import because it has some stylish tookit
from PIL import Image,ImageTk  
#pillow is used for images and imagestk for croping images etc
from tkinter import messagebox
import cv2
import cvzone
import mysql.connector
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root  #here we initialize the root
        #now from below we will set the geometry of the application
        self.root.geometry("1530x790+0+0")
        #1530=width,790=height,0from x axis (left corner to right) and 0 from y axis
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
#
        img_top=Image.open(r"college_images\facialrecognition.png")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)


#
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)

        img_bottom=Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)

        #
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale images  
            imageNp=np.array(img,'uint8') #it is a data type uint8
            id=int(os.path.split(image)[1].split('.')[1])             

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #====================Train the classifier and save======================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data set completed!!")



if __name__ == "__main__":
    root=Tk()
    obj=Train(root)  #here we created object of the class
    root.mainloop()
    #after running till this we get the background window of the screen