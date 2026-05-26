# Exercice 1 : Animaux de compagnie

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Étape 1 : Création de la classe Siamese qui hérite de Cat
class Siamese(Cat):
    pass

print("--- Étape 4 : Promenade des chats ---")
# Étape 2 : Création des instances de chat
bengal_obj = Bengal("Simba", 3)
chartreux_obj = Chartreux("Mistigri", 5)
siamese_obj = Siamese("Luna", 2)
all_cats = [bengal_obj, chartreux_obj, siamese_obj]

# Étape 3 : Création de l'instance Pets
sara_pets = Pets(all_cats)

# Exécution de la méthode walk()
sara_pets.walk()
