'''
This is the interface to an SQLite Database
'''

import sqlite3

class StudDbSqlite:
    def __init__(self, dbName='Student.db'):
        super().__init__()
        self.dbName = dbName
        self.csvFile = self.dbName.replace('.db', '.csv')
        self.conn = sqlite3.connect(self.dbName)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Employees (
                class_number TEXT PRIMARY KEY,
                name TEXT,
                gender TEXT,
                college_department TEXT,
                course TEXT)''')
        self.conn.commit()
        self.conn.close()

    def connect_cursor(self):
        self.conn = sqlite3.connect(self.dbName)
        self.cursor = self.conn.cursor()        

    def commit_close(self):
        self.conn.commit()
        self.conn.close()        

    def create_table(self):
        self.connect_cursor()
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Employees (
                    class_number TEXT PRIMARY KEY,
                    name TEXT,
                    gender TEXT,
                    college_department TEXT,
                    course TEXT)''')
        self.commit_close()

    def fetch_students(self):
        self.connect_cursor()
        self.cursor.execute('SELECT * FROM Students')
        students =self.cursor.fetchall()
        self.conn.close()
        return students

    def insert_student(self, class_number, name, gender, college_department, course):
        self.connect_cursor()
        self.cursor.execute('INSERT INTO Employees (class_number, name, gender, college_department, course) VALUES (?, ?, ?, ?, ?)',
                    (class_number, name, gender, college_department, course))
        self.commit_close()

    def delete_student(self, class_number):
        self.connect_cursor()
        self.cursor.execute('DELETE FROM Students WHERE class_number = ?', (class_number,))
        self.commit_close()

    def update_student(self, new_name, new_gender, new_college_department, new_course, class_number):
        self.connect_cursor()
        self.cursor.execute('UPDATE Students SET name = ?, gender = ?, college_department = ?, course = ? WHERE class_number = ?',
                    (new_name, new_gender, new_college_department, new_course, class_number))
        self.commit_close()

    def class_number_exists(self, class_number):
        self.connect_cursor()
        self.cursor.execute('SELECT COUNT(*) FROM Students WHERE class_number = ?', (class_number,))
        result =self.cursor.fetchone()
        self.conn.close()
        return result[0] > 0

    def export_csv(self):
        with open(self.csvFile, "w") as filehandle:
            dbEntries = self.fetch_students()
            for entry in dbEntries:
                print(entry)
                filehandle.write(f"{entry[0]},{entry[1]},{entry[2]},{entry[3]},{entry[4]}\n")

def test_StudDb():
    iStudDb = StudDbSqlite(dbName='StudDbSql.db')

    for entry in range(30):
        iStudDb.insert_student(entry, f'Name{entry} Surname{entry}', f'Female {entry}', 'Engineering', 'Electronics Engineer')
        assert iStudDb.class_number_exists(entry)

    all_entries = iStudDb.fetch_students()
    assert len(all_entries) == 30

    for entry in range(10, 20):
        iStudDb.update_student(f'Name{entry} Surname{entry}', f'Female {entry}', 'Engineering', 'Electronics Engineer', entry)
        assert iStudDb.class_number_exists(entry)

    all_entries = iStudDb.fetch_students()
    assert len(all_entries) == 30

    for entry in range(10):
        iStudDb.delete_student(entry)
        assert not iStudDb.class_number_exists(entry) 

    all_entries = iStudDb.fetch_students()
    assert len(all_entries) == 20