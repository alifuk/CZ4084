class Animals:
    def __init__(self, weight, age):
        self.weight = weight
        self.age = age

    def look(self):
        print("Looking")

    def breath(self):
        print("im breathing")

class Fish(Animals):
    def swim(self):
        print("swim")

class Mammal(Animals):
    def run(self):
        print("run")

class Bird(Animals):
    def fly(self):
        print("fly")

class DomesticDog(Mammal):
    def __init__(self,weight, age, breed, coat_color):
        self.breed = breed
        self.coat_color = coat_color
        super().__init__(weight,age)

    def bark(self):
        print("Haf")

    def retrieve(self):
        print("fetching")

    def __repr__(self):
        return f"DomesticDog Breed: {self.breed}, color {self.coat_color}, {self.weight} kg {self.age} let"

hafan = DomesticDog(30, 2, "Husky", "White")
print(hafan)
cap = Bird(30, 2)
cap.look()