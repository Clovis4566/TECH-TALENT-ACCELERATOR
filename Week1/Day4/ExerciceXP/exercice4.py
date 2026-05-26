# Exercice 4 : Cours en famille et par personne

print("--- Étape 1 : Création de la classe Person ---")
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


print("--- Étape 2 : Création de la classe Family ---")
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        nouvelle_personne = Person(first_name, age)
        nouvelle_personne.last_name = self.last_name
        self.members.append(nouvelle_personne)
        print(f"👶 Un enfant nommé {first_name} {self.last_name} ({age} ans) est né dans la famille !")

    def check_majority(self, first_name):
        personne_trouvee = None
        for membre in self.members:
            if membre.first_name == first_name:
                personne_trouvee = membre
                break
        
        if personne_trouvee:
            if personne_trouvee.is_18():
                # Utilisation de guillemets simples à l'extérieur pour éviter la SyntaxError
                print(f'"You are over 18, your parents Jane and John accept that you will go out with your friends"')
            else:
                print(f'"Sorry, you are not allowed to go out with your friends."')
        else:
            print(f"❌ Aucune personne avec le prénom '{first_name}' n'a été trouvée.")

    def family_presentation(self):
        print(f"\n👨‍👩‍👧‍👦 Présentation de la Famille {self.last_name} :")
        for membre in self.members:
            print(f"  - Prénom : {membre.first_name}, Âge : {membre.age} ans")


print("\n--- Étape 3 : Tests des classes Family et Person ---")

ma_famille = Family("Koffi")
ma_famille.born("Jean", 20)  
ma_famille.born("Marie", 15) 

ma_famille.family_presentation()

print("\n📢 Test des autorisations de sortie :")
print("Pour Jean : ", end="")
ma_famille.check_majority("Jean")

print("Pour Marie : ", end="")
ma_famille.check_majority("Marie")
