student = {
    "name":"achus",
    "age":20,
    "course":"cse"
}

def show_student(student):
    print("name" , student["name"])
    print("age" , student["age"])
    print("course" , student["course"] )
show_student(student)  

def change_age(student):
   student["age"] =21

change_age (student)
print(student)

def change_course(student):
    student["course"]="computer science"

change_course(student)
print(student)

def change_name(student):
    student["name"]="google engineer"
change_name(student)
print(student)

def change_age(student):
    student["age"]=22
change_age(student)
print(student)