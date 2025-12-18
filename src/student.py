# Inside StudentClass __init__
self.var_course = StringVar()
self.course_list =
# Function to fetch course names
def fetch_course():
    con = mysql.connector.connect(host="localhost", user="root", password="YOUR_PASSWORD", database="student_result_management")
    cur = con.cursor()
    cur.execute("SELECT name FROM course")
    rows = cur.fetchall()
    if len(rows) > 0:
        for row in rows:
            self.course_list.append(row)
fetch_course()

self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list, state='readonly', justify=CENTER, font=("goudy old style", 15))
self.txt_course.place(x=150, y=100, width=200)
self.txt_course.set("Select")