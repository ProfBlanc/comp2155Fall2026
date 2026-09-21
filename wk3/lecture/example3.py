import example2

# inheritance
# create a class BASED on a previous existing class
# question: is a 2026 version of a product
# have MORE features or LESS features than 2025 version
# when adding more features => more specific
"""
previous product                current product

parent class                    child class
super class                     sub class
base class                      derived class

more general                    more specific
"""

# you cannot remove presence of attributes/values of previous class from new class
# you cannot remove presence of method/actions of previous class from new class
    # However, you can override the behavior

from example2 import Person

class Student(Person):
    pass

def main():
    stu1 = Student(name="stu1", age=25)
    print(stu1)
    print(stu1.people_count)
    stu2 = Student.from_string("stu2,30")
    print(stu2)

if __name__ == '__main__':
    main()