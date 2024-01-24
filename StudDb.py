import sqlite3

def create_table():
    conn = sqlite3.connect('Students.db')
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Students (
            class_number INTEGER PRIMARY, 
            name TEXT,
            gender TEXT)''')
    conn.commit()
    conn.close()

def fetch_students():
    conn = sqlite3.connect('Students.db')
    cursor = conn.cursor()
    cursor.execute ('SELECT * FROM Students')
    Students = cursor.fetchall()
    conn.close()
    return Students

def insert_student(class_number, name, gender):
    conn = sqlite3.connect('Students.db')
    cursor =conn.cursor()
    cursor.execute ('INSERT INTO Students (class_number, name, gender) VALUES (?, ?, ?)', 
                    (class_number, name, gender))
    conn.commit()
    conn.close()

def delete_student(class_number):
    conn = sqlite3.connect('Students.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Students WHERE class_number = ?', (class_number,))
    conn.commit()
    conn.close()

def update_product(new_name, new_gender, class_number):
    conn = sqlite3.connect('Students.db')
    cursor = conn.cursor()
    cursor.execute ('UPDATE Students SET name = ?, gender = ? WHERE class_number = ?',
                    (new_name, new_gender, class_number))
    conn.commit()
    conn.close()

def class_number_exists(class_number):
    conn = sqlite3.connect('Students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Students WHERE class_number = ?', (class_number))
    result = cursor.fetchone()
    conn.close()
    return result [0] > 0

#create_table()