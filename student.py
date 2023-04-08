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

class Student:
    def __init__(self,root):
        self.root = root  #here we initialize the root
        #now from below we will set the geometry of the application
        self.root.geometry("1530x790+0+0")
        #1530=width,790=height,0from x axis (left corner to right) and 0 from y axis
        self.root.title("Face Recognition System")

        #here we aree creating variables for the storing data of the student form
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\face-recognition-system\college_images\face-recognition.png")
        
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


        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\face-recognition-system\college_images\smart-attendance.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        

        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\face-recognition-system\college_images\iStock-182059956_18390_t12.jpg")
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

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)



        # we will create the frame below and give name as main frame
        #background image chya vr apn frame bnvt ahe
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)
        
        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)


        img_left=Image.open(r"C:\Users\HP\OneDrive\Desktop\face-recognition-system\college_images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)


        #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=125)


        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


          #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=2,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly")
        course_combo["values"]=("Select Course","BCA","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        
          #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


         #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","2020-21","2021-22","2022-23","2023-24")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #Class Student information
        class_Students_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_Students_frame.place(x=5,y=250,width=720,height=300)


        #student id
        studentId_label=Label(class_Students_frame,text="studentId:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        studentId_entry=ttk.Entry(class_Students_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #student name
        studentId_label=Label(class_Students_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        studentId_entry=ttk.Entry(class_Students_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


         #Class Division
        class_div_label=Label(class_Students_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Students_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=20)
        div_combo["values"]=("A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


         #Roll No
        Roll_No_label=Label(class_Students_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        Roll_No_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        Roll_No_entry=ttk.Entry(class_Students_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        Roll_No_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)



         #Gender
        Gender_label=Label(class_Students_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_Students_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=20)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


          #DOB
        DOB_label=Label(class_Students_frame,text="Date Of Birth:",font=("times new roman",12,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        DOB_entry=ttk.Entry(class_Students_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)



          #Email
        Email_label=Label(class_Students_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        Email_entry=ttk.Entry(class_Students_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)



          #phone no
        phone_no_label=Label(class_Students_frame,text="Phone no:",font=("times new roman",12,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        phone_no_entry=ttk.Entry(class_Students_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


          #Address
        Address_label=Label(class_Students_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        Address_entry=ttk.Entry(class_Students_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)




          #Teacher name
        Teacher_name_label=Label(class_Students_frame,text="Teacher name:",font=("times new roman",12,"bold"),bg="white")
        Teacher_name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        Teacher_name_entry=ttk.Entry(class_Students_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        Teacher_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)




        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Students_frame,variable=self.var_radio1,text="take photo Sample", value="Yes")
        radiobtn1.grid(row=6,column=0)

       
        radiobtn2=ttk.Radiobutton(class_Students_frame,variable=self.var_radio1,text="No photo Sample", value="No")
        radiobtn2.grid(row=6,column=1)



        #buttons Frame
        btn_frame=Frame(class_Students_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

         #savebutton 
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        #updatebutton
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        #deletebutton
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)


        #resetbutton
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)





        #buttons Frame for the update and take photo sample images
        btn_frame1=Frame(class_Students_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)
        
        
         #Take a photo sample
        take_photo_btn=Button(btn_frame1,command=self.generate_data_set,text="Take a photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
         #Update a photo sample
        update_photo_btn=Button(btn_frame1,text="update a photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)






        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        img_right=Image.open(r"C:\Users\HP\OneDrive\Desktop\face-recognition-system\college_images\student.jpg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)


        #============Search System=============

        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select"," Roll No","Phone number")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)


      #table frame srv data show krnya sathi it will usefull


        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_Y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        dep =""
        course =""

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_Y.set)

        #here below we will pack our scroll bar 
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_Y.config(command=self.student_table.yview)


        #whole data will be shown here
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

            #to set the width use the following code
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
        
        
    #========function  declartion===========
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All feilds are required",parent=self.root) #parent=self.root yas sathi waprl karn jo mssg jya window vr dakhvycha ahe tyach widnow vr dakhvlya gela pyje
        else:
              try:
                  conn=mysql.connector.connect(host="localhost",username="root",password="2705",database="face_recognizer")
                  my_cursor=conn.cursor()
                  my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_semester.get(),
                                                                                                                    self.var_std_id.get(),
                                                                                                                    self.var_std_name.get(),
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_radio1.get()
                                                                                            
                                                                                                              ))
                  conn.commit()
                  self.fetch_data()
                  conn.close()
                  messagebox.showinfo("success","Student details has been added",parent=self.root)
              except Exception as es:
                  messagebox.showinfo("Error",f"Due to:{str(es)}",parent=self.root)




        #========================Fetch Data==============
    def fetch_data(self):
      conn=mysql.connector.connect(host="localhost",username="root",password="2705",database="face_recognizer")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from student")
      data=my_cursor.fetchall()

      if len(data)!=0:
          self.student_table.delete(*self.student_table.get_children())
          for i in data:
              self.student_table.insert("",END,values=i)   
          conn.commit()
          #commit ya sathi kelya jate karn data insert hot raho mhnun 
      conn.close() 

       #        get cursorr
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus() 
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),     
        self.var_course.set(data[1]),     
        self.var_year.set(data[2]),     
        self.var_semester.set(data[3]),     
        self.var_std_id.set(data[4]),     
        self.var_std_name.set(data[5]),     
        self.var_div.set(data[6]),     
        self.var_roll.set(data[7]),     
        self.var_gender.set(data[8]),     
        self.var_dob.set(data[9]),     
        self.var_email.set(data[10]),     
        self.var_phone.set(data[11]),     
        self.var_address.set(data[12]),     
        self.var_teacher.set(data[13]),     
        self.var_radio1.set(data[14])   

        #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All feilds are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="2705",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.var_std_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get(),
                                                                                            self.var_std_id.get()
                                                                                        ))
                    
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student detail succesfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


      #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error",f"Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="2705",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    

    #reset funtion
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set(" ")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")



        # Generate data set and take photo samples for the face recognition
    
    def generate_data_set(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All feilds are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="2705",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.var_std_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get(),
                                                                                            self.var_std_id.get()==id+1
                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                

                #cv2 contains the haar cascade algorithm which helps to recognize the face
                #load predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                #this file is used for the object detectioon
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#this is used for converting color images into the gray scale images
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #1.3 is the sclaing factor, 5 Minimum neighbor
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w] #ya size cha pic crop houn yeil ani mg detech hoil crop vhy sathi ahe te logic
                        return face_cropped
                    
                cap=cv2.VideoCapture(0) #0 is used because 0 is used for the web camera and for the other camera we have to use 1
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        #2 is the scale
                        #0,255,0 is the rgb color combination
                        # 2 is the thickness of the text
                        cv2.imshow("Cropped Face",face)#this is used for to show the camera
                        
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                    #100 is written there bcauz it will take the 100 samples
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)               



#main program        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)  #here we created object of the class
    root.mainloop()
    #after running till this we get the background window of the screen