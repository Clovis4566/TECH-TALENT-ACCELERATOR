# =====================================================================
# EXERCICE 1 : Animaux de compagnie
# =====================================================================
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

class Siamese(Cat):
    pass

print("--- Résultat Exercice 1 : Promenade ---")
bengal_obj = Bengal("Simba", 3)
chartreux_obj = Chartreux("Mistigri", 5)
siamese_obj = Siamese("Luna", 2)
all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets = Pets(all_cats)
sara_pets.walk()
print("-" * 50 + "\n")


# =====================================================================
# EXERCICE 2 : Chiens
# =====================================================================
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} aboie !"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        force_self = self.run_speed() * self.weight
        force_other = other_dog.run_speed() * other_dog.weight
        print(f"⚔️ Combat : {self.name} (Force: {force_self:.1f}) vs {other_dog.name} (Force: {force_other:.1f})...")
        if force_self > force_other:
            return f"🏆 {self.name} a gagné !"
        elif force_other > force_self:
            return f"🏆 {other_dog.name} a gagné !"
        else:
            return "🤝 Égalité !"

print("--- Résultat Exercice 2 : Chiens ---")
dog1 = Dog("Rex", 4, 25)
dog2 = Dog("Max", 2, 35)
dog3 = Dog("Rocky", 6, 18)

print(dog1.bark())
print(f"Vitesse de {dog1.name} : {dog1.run_speed():.2f} km/h")
print(dog1.fight(dog2))
print(dog1.fight(dog3))
print("-" * 50 + "\n")


# =====================================================================
# EXERCICE 3 : Chiens domestiqués
# =====================================================================
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(super().bark())
        self.trained = True
        print(f"🎓 {self.name} est maintenant dressé !")

    def play(self, *args):
        noms_chiens = [self.name]
        for chien in args:
            if hasattr(chien, 'name'):
                noms_chiens.append(chien.name)
            else:
                noms_chiens.append(str(chien))
        liste_noms = ", ".join(noms_chiens[:-1]) + " et " + noms_chiens[-1]
        print(f"🐕 {liste_noms} jouent tous ensemble !")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"✨ {self.name} {random.choice(tricks)}")
        else:
            print(f"❌ {self.name} n'est pas encore dressé pour les tours.")

print("--- Résultat Exercice 3 : Chien Dressé ---")
my_dog = PetDog("Fido", 2, 10)
my_dog.do_a_trick()
my_dog.train()
my_dog.do_a_trick()
my_dog.play("Buddy", "Max")
print("-" * 50 + "\n")


# =====================================================================
# EXERCICE 4 : Cours en famille
# =====================================================================
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""
    def is_18(self):
        return self.age >= 18

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        nouvelle_personne = Person(first_name, age)
        nouvelle_personne.last_name = self.last_name
        self.members.append(nouvelle_personne)
        print(f"👶 Naissance : {first_name} {self.last_name} ({age} ans)")

    def check_majority(self, first_name):
        personne_trouvee = None
        for membre in self.members:
            if membre.first_name == first_name:
                personne_trouvee = membre
                break
        if personne_trouvee:
            if personne_trouvee.is_18():
                print(f'"You are over 18, your parents Jane and John accept that you will go out with your friends"')
            else:
                print(f'"Sorry, you are not allowed to go out with your friends."')
        else:
            print(f"❌ Prénom '{first_name}' introuvable.")

    def family_presentation(self):
        print(f"\n👨‍👩‍👧‍👦 Famille {self.last_name} :")
        for membre in self.members:
            print(f"  - {membre.first_name}, {membre.age} ans")

print("--- Résultat Exercice 4 : Famille ---")
ma_famille = Family("Koffi")
ma_famille.born("Jean", 20)  
ma_famille.born("Marie", 15) 
ma_famille.family_presentation()
print("\n📢 Tests Majorité :")
print("Jean : ", end="")
ma_famille.check_majority("Jean")
print("Marie : ", end="")
ma_famille.check_majority("Marie")
