from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from tkinter import messagebox
import mysql.connector
import cv2
import os
from time import strftime
from datetime import datetime
import numpy as np
from PIL import Image 
from student import Student
from attendance import Attendance
from recognize import Recognize


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")


# ================ Image 1 ===============
        img=Image.open("image/main.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


# ================ Image 2 ===============

        img1=Image.open(r"image\main2.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


# ================ Image 3 ===============

        img2=Image.open(r"image\mainpage.jpg")
        img2=img2.resize((550,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


# ================ bg Image  ===============

        imgbg=Image.open(r"image\bg.jpg")
        imgbg=imgbg.resize((1540,710),Image.LANCZOS)
        self.photoimgbg=ImageTk.PhotoImage(imgbg)

        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=130,width=1540,height=710)

        title_lbl=Label(bg_img,text="Face Recognition Attendance System Software",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1540,height=45)


        
# ================ Student Button  ===============

        img_st_button=Image.open(r"image\student.jpg")
        img_st_button=img_st_button.resize((220,220),Image.LANCZOS)
        self.photoimg_st_button=ImageTk.PhotoImage(img_st_button)

        b1=Button(bg_img,image=self.photoimg_st_button,command=self.student_details ,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)



        
# ================ Detect Face Button  ===============

        img_dt_button=Image.open(r"image\detect.jpg")
        img_dt_button=img_dt_button.resize((220,220),Image.LANCZOS)
        self.photoimg_dt_button=ImageTk.PhotoImage(img_dt_button)

        b1=Button(bg_img,image=self.photoimg_dt_button,command=self.face_recognition,cursor="hand2")
        b1.place(x=600,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_recognition,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=600,y=300,width=220,height=40)

        
# ================ Attendance Button  ===============

        img_at_button=Image.open(r"image\attendance.jpg")
        img_at_button=img_at_button.resize((220,220),Image.LANCZOS)
        self.photoimg_at_button=ImageTk.PhotoImage(img_at_button)

        b1=Button(bg_img,image=self.photoimg_at_button,command=self.attendance_details,cursor="hand2")
        b1.place(x=1000,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",command=self.attendance_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=300,width=220,height=40)


#  ================ Train Button  ===============

        img_tr_button=Image.open(r"image\train.jpg")
        img_tr_button=img_tr_button.resize((220,220),Image.LANCZOS)
        self.photoimg_tr_button=ImageTk.PhotoImage(img_tr_button)

        b1=Button(bg_img,image=self.photoimg_tr_button,command=self.train_classifier,cursor="hand2")
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Train",cursor="hand2",command=self.train_classifier,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=600,width=220,height=40)


#  ================ Photo Button  ===============

        img_ph_button=Image.open(r"image\photo.jpg")
        img_ph_button=img_ph_button.resize((220,220),Image.LANCZOS)
        self.photoimg_ph_button=ImageTk.PhotoImage(img_ph_button)

        b1=Button(bg_img,image=self.photoimg_ph_button,cursor="hand2",command=self.open_img)
        b1.place(x=600,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Photo",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=600,y=600,width=220,height=40)


#  ================ Exit Button  ===============

        img_ex_button=Image.open(r"image\exit.jpg")
        img_ex_button=img_ex_button.resize((220,220),Image.LANCZOS)
        self.photoimg_ex_button=ImageTk.PhotoImage(img_ex_button)

        b1=Button(bg_img,image=self.photoimg_ex_button,command=self.exit,cursor="hand2")
        b1.place(x=1000,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",command=self.exit,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=600,width=220,height=40)


# ============== Open Saved Image=============
    def open_img(self):
        os.startfile("data")

# ==============Train data ============
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        # ============ Train the classifier===========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!")
         
# =========== Attendance==============
    def mark_attendance(self,i,r,n,d):
        with open("Attendance.csv","r+",newline="\n")as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d2=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d2},Present")




# ============ Face Reecognition ==============
    def face_recognition(self):
        def draw_boundray(img,classifier,scaleFactor,mineNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,mineNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                conn=mysql.connector.connect(host="localhost",username="root",password="mysql2023",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n= "+".join(n)

                my_cursor.execute("select Roll from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
        

                if confidence > 77:
                    cv2.putText(img,f"Student Id:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,127,36),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,127,36),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,127,36),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,127,36),3)
                    self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

# Exit Button
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent=self.root)
        if self.exit >0:
            self.root.destroy()
        else:
            return


# ============= Function Button =============

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def attendance_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def recognition(self):
        self.new_window=Toplevel(self.root)
        self.app = Recognize(self.new_window)




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()