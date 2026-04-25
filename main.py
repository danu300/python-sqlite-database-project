import sqlite3

# Connect to database
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    credit INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS registrations (
    reg_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(course_id) REFERENCES courses(course_id)
)
""")

conn.commit()

# Functions
def add_student():
    name = input("Enter student name: ")
    dept = input("Enter department: ")
    cursor.execute(
        "INSERT INTO students (name, department) VALUES (?, ?)",
        (name, dept)
    )
    conn.commit()
    print("Student added successfully.")

def add_course():
    name = input("Enter course name: ")
    credit = input("Enter course credit: ")
    cursor.execute(
        "INSERT INTO courses (course_name, credit) VALUES (?, ?)",
        (name, credit)
    )
    conn.commit()
    print("Course added successfully.")

def register_student():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    cursor.execute(
        "INSERT INTO registrations (student_id, course_id) VALUES (?, ?)",
        (student_id, course_id)
    )
    conn.commit()
    print("Student registered successfully.")

def view_registrations():
    cursor.execute("""
    SELECT students.name, courses.course_name
    FROM registrations
    JOIN students ON registrations.student_id = students.student_id
    JOIN courses ON registrations.course_id = courses.course_id
    """)
    results = cursor.fetchall()
    if results:
        for row in results:
            print("Student:", row[0], "| Course:", row[1])
    else:
        print("No registrations found.")

# Menu
while True:
    print("\n--- Student Course Registration System ---")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Register Student")
    print("4. View Registrations")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_course()
    elif choice == "3":
        register_student()
    elif choice == "4":
        view_registrations()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

# Close database
conn.close()