import school.courses.courses as Crs
import school.students.students as Std
import school.teachers.teachers as Tch
import school.queries.connection as Cnx

#connect to  the server as root
#Cnx.connectServer("127.0.0.1", "root", "welcome123", 10)

#connect to the school database as root
Cnx.connectDB("127.0.0.1", "school", "root", "welcome123", 10)

#add 2 courses
c = Crs.Course("root", "welcome123")
c.addCourse(['id', 'teacherId', 'title', 'credit', 'duration', 'class', 'year', 'description'], ("PY101", "Edinio", 2, 64, "SK1", 2021, "Python course"))
c.addCourse(['id', 'teacherId', 'title', 'credit', 'duration', 'class', 'year', 'description'], ("PY102", "Zacko", 2, 64, "SK1", 2021, "MySQL course"))
print("2 courses added!")

#add 10 students to the school database
s = Std.Student("root", "welcome123")
s.addStudent(['id', 'name', 'email', 'phone', 'address', 'uname', 'pwd', 'level', 'grade'], ("ST1", "Kevin", "kevinnkouimi@gmail.com", "691343915", "Douala", "Kevin", "kevin", "2", 3))
s.addStudent(['id', 'name', 'email', 'phone', 'address', 'uname', 'pwd', 'level', 'grade'], ("ST2", "Hadja", "hadja@gmail.com", "694353915", "Douala", "Hadja", "hadja", "2", 3))
s.addStudent(['id', 'name', 'email', 'phone', 'address', 'uname', 'pwd', 'level', 'grade'], ("ST3", "Arouna", "arouna@gmail.com", "651815245", "Douala", "Arouna", "arouna", "1", 2))
s.addStudent(['id', 'name', 'email', 'phone', 'address', 'uname', 'pwd', 'level', 'grade'], ("ST4", "Brice", "brice@gmail.com", "625236141", "Douala", "Brice", "brice", "2", 3))
s.addStudent(['id', 'name', 'email', 'phone', 'address', 'uname', 'pwd', 'level', 'grade'], ("ST5", "Yves", "yves@gmail.com", "625252525", "Douala", "Yves", "yves", "1", 1))
s.addStudent(['id', 'name', 'email', 'phone', 'address', 'uname', 'pwd', 'level', 'grade'], ("ST6", "Messi", "messi@gmail.com", "691020202", "Douala", "Messi", "messi", "2", 3))
s.addStudent(['id', 'name', 'email', 'phone', 'address', 'uname', 'pwd', 'level', 'grade'], ("ST7", "Kelly", "kelly@gmail.com", "692303030", "Douala", "Kelly", "kelly", "1", 1))
s.addStudent(['id', 'name', 'email', 'phone', 'address', 'uname', 'pwd', 'level', 'grade'], ("ST8", "Herve", "herve@gmail.com", "693030303", "Douala", "Herve", "herve", "2", 3))
s.addStudent(['id', 'name', 'email', 'phone', 'address', 'uname', 'pwd', 'level', 'grade'], ("ST9", "Alain", "alain@gmail.com", "695050505", "Douala", "Alain", "alain", "1", 3))
s.addStudent(['id', 'name', 'email', 'phone', 'address', 'uname', 'pwd', 'level', 'grade'], ("ST10", "Jean", "jean@gmail.com", "655050505", "Douala", "Jean", "jean", "2", 2))
print("10 students added!")

#add 2 teachers to the school database
t = Tch.Teacher("root", "welcome123")
t.addTeacher(['id', 'name', 'email', 'phone', 'address', 'uname', 'pwd'], ("SKT1", "Edinio", "edinio@gmail.com", "691239454", "Yaounde", "Edinio", "edinio"))
t.addTeacher(['id', 'name', 'email', 'phone', 'address', 'uname', 'pwd'], ("SKT2", "Zacko", "zacko@gmail.com", "685858585", "Zacko", "Zacko", "zacko"))
print("2 teachers added!")
