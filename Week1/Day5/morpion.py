# Mini-Projet 1 : Jeu de Morpion (Tic-Tac-Toe)

def afficher_plateau(plateau):
    """Affiche le plateau de jeu de manière lisible."""
    print(f"\n {plateau[0]} | {plateau[1]} | {plateau[2]} ")
    print("---|---|---")
    print(f" {plateau[3]} | {plateau[4]} | {plateau[5]} ")
    print("---|---|---")
    print(f" {plateau[6]} | {plateau[7]} | {plateau[8]} \n")

def verifier_gagnant(plateau, joueur):
    """Vérifie si le joueur actuel a aligné 3 symboles."""
    combinaisons_gagnantes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Colonnes
        [0, 4, 8], [2, 4, 6]             # Diagonales
    ]
    for combo in combinaisons_gagnantes:
        if plateau[combo[0]] == plateau[combo[1]] == plateau[combo[2]] == joueur:
            return True
    return False

def plateau_plein(plateau):
    """Vérifie s'il reste des cases vides."""
    return all(case in ['X', 'O'] for case in plateau)

def jouer_morpion():
    """Fonction principale pour lancer et gérer la partie."""
    print("❌=====================================⭕")
    print("       BIENVENUE AU JEU DU MORPION !      ")
    print("❌=====================================⭕")
    print("Les cases sont numérotées de 1 à 9 comme suit :")
    afficher_plateau([str(i) for i in range(1, 10)])
    
    # Initialisation du plateau avec des espaces vides
    plateau = [" " for _ in range(9)]
    joueur_actuel = "X"
    partie_en_cours = True

    while partie_en_cours:
        afficher_plateau(plateau)
        print(f"👉 Tour du joueur ({joueur_actuel})")
        
        # Gestion de la saisie utilisateur avec contrôle des erreurs
        try:
            choix = int(input("Choisis une case vide (1-9) : ")) - 1
            if choix < 0 or choix > 8:
                print("❌ Nombre invalide ! Reste entre 1 et 9.")
                continue
            if plateau[choix] in ['X', 'O']:
                print("⚠️ Cette case est déjà occupée ! Réessaie.")
                continue
        except ValueError:
            print("❌ Saisie incorrecte. Tu dois entrer un nombre entier.")
            continue

        # Enregistrement du coup
        plateau[choix] = joueur_actuel

        # Vérification des conditions de fin de partie
        if verifier_gagnant(plateau, joueur_actuel):
            afficher_plateau(plateau)
            print(f"🎉 FÉLICITATIONS ! Le joueur '{joueur_actuel}' a gagné la partie ! 🏆")
            partie_en_cours = False
        elif plateau_plein(plateau):
            afficher_plateau(plateau)
            print("🤝 Match nul ! Le plateau est complet.")
            partie_en_cours = False
        else:
            # Changement de joueur
            joueur_actuel = "O" if joueur_actuel == "X" else "X"

# Lancement automatique si exécuté directement
if __name__ == "__main__":
    jouer_morpion()
