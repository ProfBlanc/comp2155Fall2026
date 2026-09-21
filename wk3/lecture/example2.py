

# class definition
class Person:
    people_count = 0
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
        Person.people_count += 1
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if isinstance(value, str)\
                and len(value) >= 3:
            self.__name = value
        else:
            raise ValueError("invalid name")

    @property
    def age(self): return self.__age
    @age.setter
    def age(self, value):
        if type(value) == int and value >=0:
            self.__age = value
        else:
            raise ValueError("invalid age")
    def __str__(self):
        # summarize the object values/properties
        # what is displayed when printing entire object
        return f"{self.name} is {self.age} years old"
    #regular/instance method
    def has_long_name(self):
        return len(self.name) > 5
    # decorator
    @staticmethod # method that belongs to the class. NOT the object
    def is_adult(age):
        return age >= 18
    @classmethod  # aka factory method: create an object of class via a static method of class0
    def from_string(cls,text):
        # assume user inputs
        if "," in text and text.count(",") == 1:
            parts = text.split(",")
            name = parts[0].strip()
            age = parts[1].strip()
            try:
                age = int(age)
                return cls(name=name, age=age)
            except ValueError:
                raise ValueError("invalid age")
        raise ValueError("invalid text string")

def main():
    other = Person.from_string("Mary,20")

    print(other)

    # object instantiation
    me = Person("Prof", 100)
    you = Person("Student", 20)

    # static method syntax to use to execute
    print(Person.is_adult(100))
    print(Person.is_adult(1))
    
    # possible but should not user
    print(me.is_adult(50))
    print(you.is_adult(5))

if __name__ == '__main__':
    main()