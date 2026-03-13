student = []



class Student:
    def __init__(self, code, name, course, grade):
        self.code = code
        self.name = name
        self.course = course
        self.grade = grade
        
        

    def __repr__(self):
        return f"Student(code={self.code}, name={self.name}, course={self.course}, grade={self.grade})"

    def get_student_info(self):
        return f"{self.code}: {self.name} enrolled in {self.course} with grade {self.grade}"

with open(r"C:\Users\User\Desktop\BYU_Classes\CSE110\CSE110\main_project\w6\students.txt", "r") as file:
    next(file)
    
    for line in file:
        parts = line.strip().split(",")
        
        
        
        code = parts[0]
        name = parts[1]
        course = parts[2]
        grade = int(parts[3])



        # Process the extracted data as needed
        


        
    
    

import random
import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        course TEXT,
        marks INTEGER
    )
''')
courses = [
    "Computer Science",
    "Software Engineering",
    "Information Technology",
    "Data Science",
    "Cyber Security",
    "Artificial Intelligence",
    "Database Management"
]
names = [
    "Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Jamie", "Cameron",
    "Drew", "Avery", "Quinn", "Parker", "Reese", "Hayden", "Kendall", "Skyler",
    "Emerson", "Finley", "Rowan", "Sawyer", "Blake", "Dakota", "Harper", "Jesse",
    "Logan", "Micah", "Phoenix", "River", "Sage", "Tatum", "Winter", "Zion"
]



for _ in range(120):
    name = random.choice(names) + " " + random.choice(names)
    course = random.choice(courses)
    marks = random.randint(20, 95)
    cursor.execute(
        "INSERT INTO students (name, course, marks) VALUES (?, ?, ?)",
        (name, course, marks)
    )
    
    if grade >= 90:
        
conn.commit()
conn.close()

# --- IGNORE ---
student.append(Student(code, name, course, grade))
print(student[-1].get_student_info())
