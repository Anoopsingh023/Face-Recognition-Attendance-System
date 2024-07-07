from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")

        # Variables
        self.var_attendance_id=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance_status=StringVar()


# ================ Image 1 ===============
        img=Image.open(r"image\main.jpg")
        img=img.resize((800,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)


# ================ Image 2 ===============

        img1=Image.open(r"image\main2.jpg")
        img1=img1.resize((800,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        
# ================ bg Image  ===============

        imgbg=Image.open(r"image\bg.jpg")
        imgbg=imgbg.resize((1530,710),Image.LANCZOS)
        self.photoimgbg=ImageTk.PhotoImage(imgbg)

        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="Attendance Management System",font=("times new roman",35,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=48,width=1500,height=600)


# Left label frame

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"image\main2.jpg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=300)

        # Label Entry

        # Attendance ID
        attendanceId_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",12,"bold"),bg='white')
        attendanceId_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attendance_id,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=15,sticky=W)

        # Student Name
        student_name_label=Label(left_inside_frame,text="Name",font=("times new roman",12,"bold"),bg='white')
        student_name_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        student_name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=15,sticky=W)

        # Roll No
        roll_no_label=Label(left_inside_frame,text="Roll No",font=("times new roman",12,"bold"),bg='white')
        roll_no_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(left_inside_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=1,padx=10,pady=15,sticky=W)

        # Department
        dep_lebel=Label(left_inside_frame,text="Department",font=("times new roman",12,"bold"),bg='white')
        dep_lebel.grid(row=1,column=2,padx=10,sticky=W)

        dep_lebel_entry=ttk.Entry(left_inside_frame,textvariable=self.var_dep,width=20,font=("times new roman",12,"bold"))
        dep_lebel_entry.grid(row=1,column=3,padx=10,pady=15,sticky=W)

        # Time
        time_lebel=Label(left_inside_frame,text="Time",font=("times new roman",12,"bold"),bg='white')
        time_lebel.grid(row=2,column=0,padx=10,sticky=W)

        time_lebel_entry=ttk.Entry(left_inside_frame,textvariable=self.var_time,width=20,font=("times new roman",12,"bold"))
        time_lebel_entry.grid(row=2,column=1,padx=10,pady=15,sticky=W)
 
        # Date
        date_lebel=Label(left_inside_frame,text="Date",font=("times new roman",12,"bold"),bg='white')
        date_lebel.grid(row=2,column=2,padx=10,sticky=W)

        date_lebel_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_date,font=("times new roman",12,"bold"))
        date_lebel_entry.grid(row=2,column=3,padx=10,pady=15,sticky=W)

        # Attendance Status
        attendance_status_lebel=Label(left_inside_frame,text="Date",font=("times new roman",12,"bold"),bg='white')
        attendance_status_lebel.grid(row=3,column=0,padx=10,sticky=W)

        attendance_status_lebel_combo=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_attendance_status,font=("times new roman",12,"bold"))
        attendance_status_lebel_combo['values']=("Status","Present","Absent")
        attendance_status_lebel_combo.current(0)
        attendance_status_lebel_combo.grid(row=3,column=1,padx=10,pady=15,sticky=W)


        # Button Frame

        btn_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=395,width=715,height=35)

        import_btn=Button(btn_frame,text="Import CSV",command=self.importCSV,cursor="hand2",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export CSV",command=self.exportCSV,width=19,cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",width=19,cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

   
# Right label frame

        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attndance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=730,height=580)


        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=720,height=455)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendance_report_table=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendance_report_table.xview)
        scroll_y.config(command=self.attendance_report_table.yview)

        self.attendance_report_table.heading("id",text="Attendance Id")
        self.attendance_report_table.heading("roll",text="Roll No")
        self.attendance_report_table.heading("name",text="Name")
        self.attendance_report_table.heading("department",text="Department")
        self.attendance_report_table.heading("time",text="Time")
        self.attendance_report_table.heading("date",text="Date")
        self.attendance_report_table.heading("attendance",text="Attendance")
        self.attendance_report_table["show"]="headings"

        self.attendance_report_table.column("id",width=100)
        self.attendance_report_table.column("roll",width=100)
        self.attendance_report_table.column("name",width=100)
        self.attendance_report_table.column("department",width=100)
        self.attendance_report_table.column("time",width=100)
        self.attendance_report_table.column("date",width=100)
        self.attendance_report_table.column("attendance",width=100)
       

        self.attendance_report_table.pack(fill=BOTH,expand=1)

        self.attendance_report_table.bind("<ButtonRelease>",self.get_cursor)


        # ============ Fetch Data============
    def fetch_data(self,rows):
        self.attendance_report_table.delete(*self.attendance_report_table.get_children())
        for i in rows:
            self.attendance_report_table.insert("",END,values=i)

    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)
    
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
    def get_cursor(self,event=""):
        cursor_row=self.attendance_report_table.focus()
        content=self.attendance_report_table.item(cursor_row)
        rows=content['values']
        self.var_attendance_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendance_status.set(rows[6])

    def reset_data(self):
        self.var_attendance_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance_status.set("")




# Update 
    def update(self):
        def read_csv(file_name):
                data = []
                with open(file_name, 'r', newline='') as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                                data.append(row)
                return data

        def update_csv(file_name, updated_data):
    # Read existing data from the CSV file
                existing_data = read_csv(file_name)

    # Update the data in the file based on your logic
    # For example, let's update the 'Date' for a specific row with ID '123'
                for row in existing_data:
                        if row['ID'] == '123':
                                cursor_row=self.attendance_report_table.focus()
                                content=self.attendance_report_table.item(cursor_row)
                                rows=content['values']     
                                self.var_attendance_status.set(rows[6])
                                # row['Date'] = '2023-12-15'  # Update the date for ID '123'

    # Merge the updated data with the existing data
    # Here, you might have a different logic for updating the CSV file
                updated_data.extend(existing_data)

    # Write the updated data back to the CSV file
                with open(file_name, 'w', newline='') as csvfile:
                        headers = list(updated_data[0].keys())
                        writer = csv.DictWriter(csvfile, fieldnames=headers)
        
                        writer.writeheader()
                        for row in updated_data:
                                writer.writerow(row)

# File name of the CSV file to update
        csv_file_name = 'data.csv'

# Update the CSV file with new data
# Here, 'updated_data' should contain the updated information in the desired format
# For this example, the 'updated_data' list contains the updated information
        updated_data = [
                {'Name': 'John', 'ID': '123', 'Date': '2023-12-15'},  # Updated date for ID '123'
    # Include other rows and updates as needed
                ]

# Update the CSV file
        update_csv(csv_file_name, updated_data)


        




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()