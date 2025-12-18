class ResultClass:
    #... GUI Setup code...
    def search(self):
        con = mysql.connector.connect(host="localhost", user="root", password="YOUR_PASSWORD", database="student_result_management")
        cur = con.cursor()
        try:
            cur.execute("SELECT name, course FROM student WHERE roll_no=%s", (self.var_roll.get(),))
            row = cur.fetchone()
            if row!= None:
                self.var_name.set(row)
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "Record Not Found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error : {str(ex)}", parent=self.root)

    def add(self):
        con = mysql.connector.connect(host="localhost", user="root", password="YOUR_PASSWORD", database="student_result_management")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please Search Student Record First", parent=self.root)
            else:
                # Calculate Percentage
                per = (int(self.var_marks.get()) * 100) / int(self.var_full_marks.get())
                
                cur.execute("SELECT * FROM result WHERE roll_no=%s AND course=%s", (self.var_roll.get(), self.var_course.get()))
                row = cur.fetchone()
                if row!= None:
                    messagebox.showerror("Error", "Result already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO result (roll_no, name, course, marks_ob, full_marks, percentage) VALUES (%s, %s, %s, %s, %s, %s)", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Result Added Successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error : {str(ex)}", parent=self.root)