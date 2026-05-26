# Exercice 2 : Chiens

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
        
        print(f"⚔️ Combat entre {self.name} (Force: {force_self:.1f}) et {other_dog.name} (Force: {force_other:.1f})...")
        
        if force_self > force_other:
            return f"🏆 {self.name} a gagné le combat !"
        elif force_other > force_self:
            return f"🏆 {other_dog.name} a gagné le combat !"
        else:
            return "🤝 Égalité parfaite !"

print("--- Étape 3 : Tests des méthodes des chiens ---")
# Étape 2 : Création des instances de chiens
dog1 = Dog("Rex", 4, 25)
dog2 = Dog("Max", 2, 35)
dog3 = Dog("Rocky", 6, 18)

# Exécution et affichage des tests
print(dog1.bark())
print(f"Vitesse de {dog1.name} : {dog1.run_speed():.2f} km/h")
print(dog1.fight(dog2))
print(dog1.fight(dog3))
