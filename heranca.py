# HERANÇA (inheritance)

# classe mãe
class Animal:
    def __init__(self, age:int, height:int, weight:int, position:tuple):
        self.age = age
        self.height = height
        self.weight = weight
        self.position = position # position [position_x, position_y, position_z]

    def move_x(self):
        self.position[0] += 1

    def move_y(self):
        self.position[1] += 1

    def move_z(self):
        self.position[2] += 2


# classe filha
class Dog(Animal):
    def __init__(self, age:int, height:int, weight:int, position:tuple):
        Animal.__init__(self, age, height, weight, position)  # poderia ser super()__init__ também, questão de preferência e legibilidade

    def move_z(self):
        self.position[2] += 2  # dos métodos herdados a partir da classe mãe (Animal), este foi sob escrito (override).


# instanciando classe filha
astolfo = Dog(2, 1, 3, (1, 0, 0))
print(f'About Astolfo: his age is {astolfo.age}, his height is {astolfo.height}, weight {astolfo.weight}')
print(f'At this moment, his position is {astolfo.position}')
