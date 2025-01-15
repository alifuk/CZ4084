'''
class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __repr__(self):
        return f"Human(name={self.name},age={self.age},height={self.height})"
'''
from dataclasses import dataclass
@dataclass
class Human:
    name : str
    age : int
    heght : int

albert = Human("Albert", 30, 200)
print(albert)