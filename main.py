from STUDENT import Student

class Database:
    list=[]
    def run(self):
        student=Student(
            input("Name: ").upper(),
            input("Lastname: ").upper(),
            float(input("Grades: ")),
            input("Id: ")
        )
        self.list.append(student)
        response=input("Do you want to enter another student? Type 'y' for yes")
        if(response=='y'):
            self.run()
    def printStudents(self):
        print("Name \t Lastname \t Grades \t Id")
        for obj in self.list:
            print(f"{obj.name} \t {obj.lastname} \t {obj.grade} \t {obj.id}")
    def searchStudent(self,list,name):
        for student in self.list:
            if student.name==name:
                print(f"{student.name} \t {student.lastname} \t {student.grade} \t {student.id}")
    def modify_grade(self, name, lastname, grade):
        for obj in self.list:
            if(obj.name == name and obj.lastname == lastname):
                print("Grade was modyfied succesfully!")
                obj.grade=grade
    def sortByName(self,list):
        for i in self.list:
            for j in self.list:
                if i.name>j.name:
                    aux = i
                    i = j
                    j = aux


db = Database()
def Menu():
    print("1. Enter Students.")
    print("2. Print Students.")
    print("3. Search Student by name.")
    print("4. Modify grade by name.")
    print("0. Exit Menu.")
option=1
Menu()
while option != 0:
    option = int(input("Choose an option: "))
    if option == 1:
        db.run()
    elif option == 2:
        db.printStudents()
    elif option == 3:
        db.searchStudent(list, input("Name: ").upper())
    elif option == 4:
        db.modify_grade(name=input("Enter name: ").upper(), lastname=input("Enter lastname: ").upper(), grade=float(input("Enter the new grade: ")))
    elif option == 5:
        db.sortByName(list)
    else:
        exit(0)
