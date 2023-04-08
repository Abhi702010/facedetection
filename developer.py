from tkinter import*
from tkinter import ttk  
# ttk is import because it has some stylish tookit
from PIL import Image,ImageTk  
#pillow is used for images and imagestk for croping images etc
from tkinter import messagebox
#this mssgbox will help to show the mssg
import mysql.connector
import cv2
#it is a open source vision library

class Developer:
    def __init__(self,root):
        self.root = root  #here we initialize the root
        #now from below we will set the geometry of the application
        self.root.geometry("1530x790+0+0")
        #1530=width,790=height,0from x axis (left corner to right) and 0 from y axis
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
#,
        img_top=Image.open(r"college_images\dev.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)



            #frame 
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1=Image.open(r"college_images\abhi.jpg")
        img_top1=img_top1.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)


        #23 minutes remaining sharp  thats it for the day meet u tommorow


#main program        
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)  #here we created object of the class
    root.mainloop()
    #after running till this we get the background window of the screen