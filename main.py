import sqlite3

conn = sqlite3.connect("students_info.db")
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE students (
#      student_name TEXT,
#      avg_score INT,
#      class TEXT,
#      parent_name TEXT
#  );
# ''')
# cursor.execute('''INSERT INTO students(student_name, avg_score, class, parent_name) VALUES 
#                     ("Саддам Хусейн", 11, "11-А", "Абд аль-Маджи́д"),
#                      ("Лера Позвоночник", 9, "11-А", "Позвоночник Алексей"),
#                      ("Рамаль Сокка", 8, "11-А", "Рамаль Нарман"),
#                      ("Вика Подцветочник", 10, "11-А", "Подцветочник Олег"),
#                      ("Артур Морган", 6, "11-А", "Морган Джон");
#  ''')
cursor.execute('''SELECT * FROM students WHERE avg_score >= 9;''')

for i in cursor.fetchall():
    print(i)
conn.commit()