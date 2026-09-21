from example2 import Person

class Student(Person):
    # overrode our constructor
    def __init__(self, name="", age=0, student_id=12345, courses=[]):
        super().__init__(name=name, age=age)
        self.student_id = student_id
        self.courses = courses
    def __str__(self):
        return super().__str__() \
            + f" and has a student id of {self.student_id} and is taking {len(self.courses)} courses"
def main():
    stu1 = Student(name="stu1", age=25)
    print(stu1)
    print(stu1.people_count)
    stu2 = Student.from_string("stu2,30")
    print(stu2)

if __name__ == '__main__':
    main()