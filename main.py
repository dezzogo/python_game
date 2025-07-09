# # 1. Definir uma classe e instanciando seu objeto no main
#
# class Dog:
#     def __init__(self):
#         pass
#
# # main
# astolfo = Dog()
# print(astolfo)

# -----
# # 2. Inserir atributos com valor fixo
# class Dog:
#     def __init__(self):
#         self.age = 5
#
# # main
# astolfo = Dog()
# caramelo = Dog()
# print(f"Astolfo's age is {astolfo.age} and Caramelo's age is {caramelo.age}")

# -----
# # 3. Inserir atributos com passagem de parâmetros no construtor da classe
# class Dog:
#     def __init__(self, age):
#         self.age = age
#
# # main
# astolfo = Dog(1)
# caramelo = Dog(2)
# print(f"Astolfo's age is {astolfo.age} and Caramelo's age is {caramelo.age}")

# # -----
# # 4. Atributo da classe
# class Dog:
#     family = 'Canidae'
#
#     def __init__(self, age):
#         self.age = age
#
# # main
# astolfo = Dog(1)
# caramelo = Dog(2)
# # atributo do objeto (astolfo):
# print(f"Astolfo's age is {astolfo.age}, belonging to {astolfo.family} family")
# # atributo da classe (Dog)
# print(f"All dogs belong to {Dog.family} family.")

# -----
# # 5. Definir o tipo de um atributo
# class Dog:
#     family = 'Canidae'
#
#     def __init__(self, age:int):
#         self.age:int = age
#
# # main
# astolfo = Dog(1)
# caramelo = Dog(2)
# # atributo do objeto (astolfo):
# print(f"Astolfo's age is {astolfo.age}, belonging to {astolfo.family} family")
# # atributo da classe (Dog)
# print(f"All dogs belong to {Dog.family} family.")

# # -----
# # 6. Atributos especiais __class__ e __name__
# class Dog:
#     family = 'Canidae'
#
#     def __init__(self, age:int):
#         self.age:int = age
#
# # main
# astolfo = Dog(1)
# caramelo = Dog(2)
# print(f"Astolfo's age is {astolfo.age}, belonging to {astolfo.family} family")
# print(f"All dogs belong to {Dog.family} family.")
# print(f"Astolfo is an object that belongs to {astolfo.__class__.__name__} class")

# -----
# # 7. Atributos protegidos
# class Dog:
#     family = 'Canidae'
#
#     def __init__(self, age, weight):
#         self._age = age # _ é uma dica que é um atributo privado e não deve ser alterado diretamente fora da classe.
#         self.__weight = weight # __ protegido, interpretador Python realiza "mangling", evitando colisão de nomes.
#
# # main
# astolfo = Dog(1, 3,2)
# caramelo = Dog(2, 4,5)
# print(f"Astolfo's age is {astolfo._age}, weight {astolfo.__weight} is belonging to {astolfo.family} family")
# # código acima dá erro devido proteção com __
# print(f"All dogs belong to {Dog.family} family.")
# print(f"Astolfo is an object that belongs to {astolfo.__class__.__name__} class")

# -----
# 8. Métodos (getters e setters que não são comuns de se usar na linguagem
class Dog:
    family = 'Canidae'

    def __init__(self, age):
        self._age = age # _ é uma dica que é um atributo privado e não deve ser alterado diretamente fora da classe.
        self.__weight = 0 # __ protegido, interpretador Python realiza "mangling", evitando colisão de nomes.

    def get_age(self) -> int: # pode se definir o dado de retorno
            return self._age

    def get_weight(self) -> int:
            return self.__weight

    def set_weight(self, weight:float):
            self.__weight = weight

# main
astolfo = Dog(1)
astolfo.set_weight(3.250)
print(f"Astolfo's age is {astolfo.get_age()}, weight {astolfo.get_weight()} kg, is belonging to {astolfo.family} family")
# código acima dá erro devido proteção com __
print(f"All dogs belong to {Dog.family} family.")
print(f"Astolfo is an object that belongs to {astolfo.__class__.__name__} class")
