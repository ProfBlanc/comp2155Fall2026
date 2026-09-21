class Animal:
    def speak(self):
        return "Makes noise"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

a = Animal()
d = Dog()
c = Cat()

print(a.speak(), d.speak(), c.speak(), sep="\n")
