import mysql.connector

def create_db():
    # Connect to MySQL Server (Update password)
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="YOUR_PASSWORD")
        cur = con.cursor()
        
        # Create Database
        cur.execute("CREATE DATABASE IF NOT EXISTS student_result_management")
        cur.execute("USE student_result_management")
        
        # Table 1: Course
        cur.execute("""
            CREATE TABLE IF NOT EXISTS course (
                cid INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                duration VARCHAR(50),
                charges VARCHAR(50),
                description TEXT
            )
        """)
        
        # Table 2: Student (Linked to Course via 'course' name) 
        cur.execute("""
            CREATE TABLE IF NOT EXISTS student (
                roll_no VARCHAR(20) PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                email VARCHAR(50),
                gender VARCHAR(20),
                dob VARCHAR(20),
                contact VARCHAR(20),
                admission VARCHAR(20),
                course VARCHAR(50),
                state VARCHAR(50),
                city VARCHAR(50),
                pin VARCHAR(10),
                address TEXT
            )
        """)
        
        # Table 3: Result (Linked to Student via 'roll_no')
        cur.execute("""
            CREATE TABLE IF NOT EXISTS result (
                rid INT AUTO_INCREMENT PRIMARY KEY,
                roll_no VARCHAR(20),
                name VARCHAR(50),
                course VARCHAR(50),
                marks_ob VARCHAR(20),
                full_marks VARCHAR(20),
                percentage VARCHAR(20),
                FOREIGN KEY (roll_no) REFERENCES student(roll_no) ON DELETE CASCADE
            )
        """)
        
        con.commit()
        con.close()
        print("Database Created Successfully")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_db()