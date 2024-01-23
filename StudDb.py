from StudDbEntry import StudDbEntry

class StudDb:
    def __init__(self, class_number, name, gender, college_department, course):
        self.class_number = class_number
        self.name = name
        self.gender = gender
        self.college_department = college_department
        self.course = course

class StudentDatabase:
    def __init__(self, db_name='student.db'):
        self.conn = StudDbEntry.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                class_number INTEGER PRIMARY KEY,
                name TEXT,
                gender TEXT,
                college_department
                course TEXT
            )
        ''')
        self.conn.commit()

    def create_entry(self, stud_entry):
        self.cursor.execute('''
            INSERT INTO students (class_number, name, gender, college_department, course)
            VALUES (?, ?, ?, ?)
        ''', (stud_entry.class_number, stud_entry.name, stud_entry.gender, stud_entry.college_department, stud_entry.course))
        self.conn.commit()

    def read_entry(self, class_number):
        self.cursor.execute('SELECT * FROM students WHERE class_number = ?', (class_number,))
        return self.cursor.fetchone()

    def update_entry(self, stud_entry):
        self.cursor.execute('''
            UPDATE students
            SET name=?, gender=?, college_department=?, course=?
            WHERE class_number=?
        ''', (stud_entry.name, stud_entry.gender, stud_entry.college_department, stud_entry.course ,stud_entry.class_number))
        self.conn.commit()

    def delete_entry(self, class_number):
        self.cursor.execute('DELETE FROM students WHERE class_number = ?', (class_number,))
        self.conn.commit()

def main():
    student_db = StudentDatabase()

    # Create an entry
    new_student = StudDbEntry(class_number=1, name='Anne Hathaway', gender='Female', college_department='Engineering', course='Electronics Engineering')
    student_db.create_entry(new_student)

    # Read the entry
    retrieved_student = student_db.read_entry(class_number=1)
    print("Read Entry:", retrieved_student)

    # Update the entry
    updated_student = StudDbEntry(class_number=1, name='Anne Updated', gender='Female', college_department='Engineering', course='Electronics Engineering')
    student_db.update_entry(updated_student)

    # Read the updated entry
    updated_retrieved_student = student_db.read_entry(class_number=1)
    print("Updated Entry:", updated_retrieved_student)

    # Delete the entry
    student_db.delete_entry(class_number=1)

    # Read after deletion
    deleted_retrieved_student = student_db.read_entry(class_number=1)
    print("Deleted Entry:", deleted_retrieved_student)

if __name__ == "__main__":
    main()
