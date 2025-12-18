from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass
import time

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        
        # Header
        title = Label(self.root, text="Student Result Management System", font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)
        
        # Menu Frame
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=80)
        
        btn_course = Button(M_Frame, text="Course", command=self.add_course, font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=20, y=5, width=200, height=40)
        btn_student = Button(M_Frame, text="Student", command=self.add_student, font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=240, y=5, width=200, height=40)
        btn_result = Button(M_Frame, text="Result", command=self.add_result, font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=460, y=5, width=200, height=40)
        btn_view = Button(M_Frame, text="View Results", command=self.add_report, font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=680, y=5, width=200, height=40)
        btn_logout = Button(M_Frame, text="Logout", command=self.root.quit, font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=900, y=5, width=200, height=40)
        btn_exit = Button(M_Frame, text="Exit", command=self.root.quit, font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=1120, y=5, width=200, height=40)

        # Content Window (Example Placeholder)
        self.bg_img = Image.open("images/bg.png") # Ensure this file exists
        self.bg_img = self.bg_img.resize((920, 350), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=400, y=180, width=920, height=350)

        # Update Clock
        self.lbl_clock = Label(self.root, text="Time: HH:MM:SS", font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=650, relwidth=1, height=30)
        self.update_clock()

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ReportClass(self.new_win)

    def update_clock(self):
        # Recursive time update 
        now = time.strftime("%H:%M:%S")
        self.lbl_clock.config(text=f"Welcome to SRMS \t\t Time: {now}")
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()