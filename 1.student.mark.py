nb_student = int(input("Number of student: "))
id_student = []
name_student = []
DoB_student = []
for i in range(nb_student):
    x = input("ID of the student: ")
    id_student.append(x)
    y = input("Name of the student: ")
    name_student.append(y)
    z = input("DoB of the student: ")
    DoB_student.append(z)

nb_course = int(input("Number of the courses: "))
id_course = []
name_course = []
for i in range(nb_course):
    a = input("ID of the course: ")
    id_course.append(a)
    b = input("Name of the course: ")
    name_course.append(b)

point = []
v=0
for i in range(nb_course):
    for j in range(nb_student):
        score = float(input(name_course[nb_course]+" mark of "+ name_student[nb_student]+":"))
        point.append(score)

for i in range(nb_student):
    print("\t"+id_course[i],name_course[i]+":")
    for j in range(nb_course):
        print("  ||  "+id_student[j],name_student[j],DoB_student[j]+"  ||  "+str(+point(v)))
        v+=1