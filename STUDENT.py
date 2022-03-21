from Person import Person

class Student(Person):
    def __init__(self, name, lastname, grade, id):
        super().__init__(name, lastname)
        self.grade = grade
        self.id = id
