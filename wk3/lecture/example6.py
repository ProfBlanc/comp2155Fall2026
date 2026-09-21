import csv
from pathlib import Path

class Cat:
    # name, # legs
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
    def __str__(self):
        return f"{self.name} has a legs of {self.legs}"
    @classmethod
    def create_cat(cls, text):
        data = text.split(",")
        return cls(name=data[0], legs=data[1])
    @staticmethod
    def is_big(weight):
        return weight > 100

# lazy = not repeating yourself
# DRY   don't repeat yourself

class Lion(Cat):
    def __init__(self, name, legs, mane):
        super().__init__(name, legs)
        self.mane = mane
    def __str__(self):
        return super().__str__() + f" has a mane of {self.mane}"

class Tiger(Cat):
    def __init__(self, name, legs, stripes):
        super().__init__(name, legs)
        self.stripes = stripes
    def __str__(self):
        return super().__str__() + f" and has {self.stripes} stripes"

class Zoo:
    animal_count = 0
    def __init__(self, name):
        self.name = name
        self.__animals = []
    def add_animal(self, animal):
        if isinstance(animal, (Lion, Tiger)):
            self.__animals.append(animal)
            Zoo.animal_count += 1
    def display_animals(self):
        summary = ""
        for animal in self.__animals:
            summary += str(animal) + "\n"
        return summary
    def save_data(self):
        file_path = Path(f"{self.name}.csv")
        fo = file_path.open(mode="w")
        fields = "name,legs,type,mane/stripes".split(",")
        csv_writer = csv.DictWriter(fo,
                                    fieldnames=fields,
                                    lineterminator="\n")
        all_row_data = []
        for animal in self.__animals:
            single_row = dict.fromkeys(fields)
            # {key1: None, key2: None, keyN: None}
            single_row[fields[0]] = animal.name
            single_row[fields[1]] = animal.legs
            animal_type = ""
            extra_data = ""
            if type(animal) is Lion:
                animal_type = "Lion"
                extra_data = animal.mane
            elif type(animal) is Tiger:
                animal_type = "Tiger"
                extra_data = animal.stripes

            single_row[fields[2]] = animal_type
            single_row[fields[3]] = extra_data
            all_row_data.append(single_row)

        csv_writer.writeheader()
        csv_writer.writerows(all_row_data)

def main():
    zoo = Zoo("Zoo")
    zoo.add_animal(Cat(name="Cat", legs=4))

    zoo.add_animal(Lion(name="Lion", legs=4, mane="mane"))
    zoo.add_animal(Tiger(name="Tiger", legs=4, stripes=10))

    print(zoo.animal_count)
    print(zoo.display_animals())
    zoo.save_data()

if __name__ == '__main__':
    main()