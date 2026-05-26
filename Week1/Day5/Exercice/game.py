# game.py
import random

class Game:
    def get_user_item(self):
        """Demande à l'utilisateur de choisir pierre, feuille ou ciseaux."""
        choix_valides = ['pierre', 'feuille', 'ciseaux']
        while True:
            saisie = input("Choisissez un élément (pierre / feuille / ciseaux) : ").strip().lower()
            if saisie in choix_valides:
                return saisie
            print("⚠️ Choix invalide. Veuillez entrer 'pierre', 'feuille' ou 'ciseaux'.")

    def get_computer_item(self):
        """Sélectionne aléatoirement un élément pour l'ordinateur."""
        choix_valides = ['pierre', 'feuille', 'ciseaux']
        return random.choice(choix_valides)

    def get_game_result(self, user_item, computer_item):
        """Détermine le résultat de la partie du point de vue de l'utilisateur."""
        if user_item == computer_item:
            return "match nul"
            
        # Définition des règles de victoire
        regles_victoire = {
            'pierre': 'ciseaux',
            'feuille': 'pierre',
            'ciseaux': 'feuille'
        }
        
        if regles_victoire[user_item] == computer_item:
            return "victoire"
        else:
            return "défaite"

    def play(self):
        """Exécute un tour de jeu complet et renvoie le résultat."""
        print("\n--- Début du round ---")
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        resultat = self.get_game_result(user_item, computer_item)
        
        # Affichage du résultat convivial
        if resultat == "victoire":
            print(f"🎉 Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Vous avez gagné !")
        elif resultat == "défaite":
            print(f"😢 Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Vous avez perdu.")
        else:
            print(f"🤝 Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Match nul !")
            
        return resultat
