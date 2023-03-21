import numpy as np
import math
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
        self.__credit = int(input("\t Enter the course's credit: "))
    #Escapsulation part
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name 
    def get_credit(self):
        return self.__credit
    def set_subject(self):
        return(f"ID:{self.get_id()}     Name:{self.get_name()}  Credit:{self.get_credit()}")
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
     def __init__(self):
         self.__score = int(input(f"\t Enter the mark: "))
     def get_score(self):
         return self.__score
     def set_score(self):
         return(f"Average score:{self.get_score()}  ")
#Create GPA
class GPA:
    def __init__(self, gpa: float):
        self.__gpa = gpa
    def get_gpa(self):
        return f"{round(self.__gpa,2)}"
#Create list
All_students = []
All_courses = []
marks = []
cour_name = []
cour_credit = []
stu_name = []
average_mark = []
average_GPA = []
point = np.array([])
sum_credit = 0
count = 0
#the info of the student
n = int(input("Number of student: "))
for i in range(n):
    stu = Student()
    All_students.append(stu.set_student())
    #To get the student's name
    stu_name.append(stu.get_name())

#the info of the course
m = int(input("Number of course: "))
for i in range(m):
    cour = Course()
    All_courses.append(cour.set_subject())
#To get the course's name and credit
    cour_name.append(cour.get_name())
    sum_credit += cour.get_credit() 
    cour_credit.append(cour.get_credit())


#Use the student's name and couse's name to print the mark part
for i in range(len(stu_name)):
    print(f"Add score for student {stu_name[i]}: ")
    for j in range(len(cour_name)):
        mark = Score()
        marks.append(mark.get_score())
        point = np.concatenate((point,marks))
        stu_point = np.array_split(point, len(stu_name))
for i in range(len(All_students)):
    avg = 0
    k = 0
    for j in range(len(cour_credit)):
        avg += marks[count] * cour_credit[k]
        k+=1
        count+=1
        if k == len(cour_credit):
            average_mark.append(avg)
            avg = 0

for i in range(len(average_mark)):
    avg_gpa = average_mark[i]/sum_credit
    score_gpa = GPA(avg_gpa)
    average_GPA.append(score_gpa.get_gpa())
    
cnt = 0
print("List students: ")
for i in range(len(All_students)):
    print(All_students[i])
print("List course: ")
for i in range(len(All_courses)):
    print(All_courses[i])
for i in range(len(stu_name)):
    print(f"{stu_name[i]}:")
    for j in range(len(cour_name)):
        print(f"   ||   {cour_name[j]}:  {marks[cnt]}   ||")
        cnt+=1
print(average_GPA)
print("Sort GPA")
average_GPA.sort(reverse= True)
print(average_GPA)