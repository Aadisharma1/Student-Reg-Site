from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Courses")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Variables
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        # Widgets
        title = Label(self.root, text="Manage Course Details", font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=10, y=15, width=1180, height=35)
        
        lbl_course = Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        lbl_duration = Label(self.root, text="Duration", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        lbl_charges = Label(self.root, text="Charges", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        lbl_desc = Label(self.root, text="Description", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)

        self.txt_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_course.place(x=150, y=60, width=200)
        
        self.txt_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_duration.place(x=150, y=100, width=200)
        
        self.txt_charges = Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_charges.place(x=150, y=140, width=200)
        
        self.txt_desc = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_desc.place(x=150, y=180, width=500, height=100)

        # Buttons
        self.btn_add = Button(self.root, text="Save", command=self.add, font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2")
        self.btn_add.place(x=150, y=400, width=110, height=40)
        self.btn_update = Button(self.root, text="Update", command=self.update, font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2")
        self.btn_update.place(x=270, y=400, width=110, height=40)
        self.btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2")
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2")
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # Search Panel
        self.var_search = StringVar()
        lbl_search = Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
        txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=870, y=60, width=180)
        btn_search = Button(self.root, text="Search", command=self.search, font=("goudy old style", 15, "bold"), bg="#033054", fg="white", cursor="hand2").place(x=1070, y=60, width=120, height=28)

        # Treeview content
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)
        
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "name", "duration", "charges", "description"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        
        self.CourseTable.heading("cid", text="CID")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Description")
        self.CourseTable["show"] = 'headings'
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def add(self):
        con = mysql.connector.connect(host="localhost", user="root", password="YOUR_PASSWORD", database="student_result_management")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name=%s", (self.var_course.get(),))
                row = cur.fetchone()
                if row!= None:
                    messagebox.showerror("Error", "Course Name already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO course (name, duration, charges, description) VALUES (%s, %s, %s, %s)", (
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_desc.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = mysql.connector.connect(host="localhost", user="root", password="YOUR_PASSWORD", database="student_result_management")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_desc.delete("1.0", END)
        self.txt_desc.insert(END, row[4])

    def update(self):
        # Implementation for update using UPDATE course SET... WHERE name=...
        pass # (Student must fill this based on add logic)

    def delete(self):
        # Implementation for delete using DELETE FROM course WHERE name=...
        pass # (Student must fill this)

    def clear(self):
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.txt_desc.delete("1.0", END)
        self.var_search.set("")

    def search(self):
        # Implementation for search using SELECT * FROM course WHERE name LIKE...
        pass