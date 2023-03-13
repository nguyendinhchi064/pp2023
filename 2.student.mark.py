#Create Person
class Person():
    def __init__(self):
        self.id = input("\t Enter the person's ID: ")
        self.name = input("\t Enter the person's name:")
        self.dob = input("\t Enter the person's dob:")
#Create Course
class Course():
    def __init__(self):
        self.__id = input("\t Enter the course's ID: ")
        self.__name = input("\t Enter the course's name: ")
    #Escapsulation part
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name 
    def set_subject(self):
        return(f"ID:{self.get_id()}     Name:{self.get_name()}")
#Create Stundent inherite from Person         
class Student(Person):
    def __init__(self):
    #Polymorphism
        super().__init__()
    #Enscapsulation 
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_dob(self):
        return self.dob
    def set_student(self):
        return(f"ID:{self.get_id()}    Name:{self.get_name()}   DOB:{self.get_dob()}")
#Create Score    
class Score:
     def __init__(self,score):
         self.__score = score
     def get_score(self):
         return f"{self.__score}"
#Create list
All_students = []
All_courses = []
marks = []
cour_name = []
stu_name = []

#the info of the student
n = int(input("Number of student: "))
for i in range(n):
    stu = Student()
    All_students.append(stu.set_student())
    #To get the student's name
    stu_name.append(stu.get_name())
for i in range(len(All_students)):
    print(All_students[i])

#the info of the course
m = int(input("Number of course: "))
for i in range(m):
    cour = Course()
    All_courses.append(cour.set_subject())
    #To get the course's name
    cour_name.append(cour.get_name()) 
for i in range(len(All_courses)):
     print(All_courses[i])
     
#Use the student's name and couse's name to print the mark part
for i in range(len(stu_name)):
    for j in range(len(cour_name)):
        score = int(input(f"{cour_name[j]} score of student {stu_name[i]}: "))
        all_score = Score(score)
        marks.append(all_score.get_score())
cnt = 0
for i in range(len(All_students)):
    print(All_students[i])
for i in range(len(All_courses)):
    print(All_courses[i])
for i in range(len(stu_name)):
    print(f"{stu_name[i]}:")
    for j in range(len(cour_name)):
        print(f"   ||   {cour_name[j]}:  {marks[cnt]}||")
        cnt+=1