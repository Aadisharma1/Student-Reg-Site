# Inside ReportClass
def show(self):
    con = mysql.connector.connect(host="localhost", user="root", password="YOUR_PASSWORD", database="student_result_management")
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM result")
        rows = cur.fetchall()
        self.ResultTable.delete(*self.ResultTable.get_children())
        for row in rows:
            self.ResultTable.insert('', END, values=row)
    except Exception as ex:
        messagebox.showerror("Error", f"Error : {str(ex)}", parent=self.root)

def delete(self):
    con = mysql.connector.connect(host="localhost", user="root", password="YOUR_PASSWORD", database="student_result_management")
    cur = con.cursor()
    try:
        if self.var_id == "": # var_id captured from get_data event
            messagebox.showerror("Error", "Search Student Result First", parent=self.root)
        else:
            cur.execute("DELETE FROM result WHERE rid=%s", (self.var_id,))
            con.commit()
            messagebox.showinfo("Success", "Result Deleted Successfully", parent=self.root)
            self.show()
    except Exception as ex:
        messagebox.showerror("Error", f"Error : {str(ex)}", parent=self.root)