# rock-paper-scissors.py
import sys
# On s'assure que le répertoire courant est dans le path d'importation
import os
sys.path.append(os.getcwd())

from game import Game

def get_user_menu_choice():
    """Affiche le menu principal et récupère le choix de l'utilisateur."""
    print("\n================ MENU PRINCIPAL ================")
    print(" 1. Jouer une nouvelle partie")
    print(" 2. Afficher les scores temporaires")
    print(" 3. Quitter le programme (ou tapez 'q' / 'x')")
    print("================================================")
    
    choix = input("Votre choix : ").strip().lower()
    return choix

def print_results(results):
    """Affiche le récapitulatif global des scores."""
    print("\n================================================")
    print("🏆 RÉCAPITULATIF FINAL DE VOS PARTIES")
    print("================================================")
    print(f"  - Nombre de victoires   : {results['win']}")
    print(f"  - Nombre de défaites    : {results['loss']}")
    print(f"  - Nombre de matchs nuls : {results['draw']}")
    print("================================================")
    print("👋 Merci beaucoup pour votre participation et à bientôt !")

def main():
    """Fonction principale pour orchestrer les menus et les scores."""
    # Initialisation du dictionnaire des scores
    scores = {'win': 0, 'loss': 0, 'draw': 0}
    
    while True:
        choix = get_user_menu_choice()
        
        if choix in ['1', 'jouer']:
            # Instanciation de la classe Game et lancement de la partie
            nouvelle_partie = Game()
            resultat_round = nouvelle_partie.play()
            
            # Mise à jour des scores
            if resultat_round == "victoire":
                scores['win'] += 1
            elif resultat_round == "défaite":
                scores['loss'] += 1
            elif resultat_round == "match nul":
                scores['draw'] += 1
                
        elif choix in ['2', 'scores']:
            print(f"\n📊 Scores actuels -> Victoires: {scores['win']} | Défaites: {scores['loss']} | Nuls: {scores['draw']}.")
            
        elif choix in ['3', 'quitter', 'q', 'x']:
            print_results(scores)
            break
            
        else:
            print("⚠️ Option invalide. Entrez un numéro du menu ou 'q' pour quitter.")

if __name__ == "__main__":
    main()
