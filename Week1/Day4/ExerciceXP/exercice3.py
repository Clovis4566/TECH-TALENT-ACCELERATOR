# Exercice 3 : Chiens domestiqués
import random
# Étape 1 : Importation de la classe Dog de l'exercice précédent
from exercice2 import Dog

# Étape 2 : Création de la classe PetDog
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
            choix = random.choice(tricks)
            print(f"✨ {self.name} {choix}")
        else:
            print(f"❌ {self.name} n'est pas encore dressé, il ne peut pas faire de tours.")

print("--- Étape 3 : Tests des méthodes PetDog ---")
my_dog = PetDog("Fido", 2, 10)
my_dog.do_a_trick() # Test avant dressage
my_dog.train()      # Dressage
my_dog.do_a_trick() # Test après dressage
my_dog.play("Buddy", "Max") # Séance de jeu
