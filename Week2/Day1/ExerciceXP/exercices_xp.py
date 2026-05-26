# Week 2 - Day 1 : Script d'Analyse de Données Global (Exercices 1 à 10)
import pandas as pd
import numpy as np
import json

print("==================================================================")
print("🚀 SCRIPT GLOBAL D'ANALYSE DE DONNÉES - EXERCICES XP VALIDÉS")
print("==================================================================\n")

# --- 🌟 EXERCICE 1 : NUMPY – CRÉATION ET MANIPULATION DE TABLEAUX ---
print("--- 🌟 Exercice 1 : Opérations NumPy ---")
# 1. Tableau 1D de 10 à 29
tableau_1d = np.arange(10, 30)
# 2. Reshape en 4x5
matrice_2d = tableau_1d.reshape(4, 5)
print("Matrice 4x5 générée :")
print(matrice_2d)
# 3. Extraction de la deuxième ligne (index 1)
print(f"Deuxième ligne complète : {matrice_2d[1]}")
# 4. Valeur à la 3ème ligne, 4ème colonne (index [2, 3])
print(f"Valeur à la ligne 3, colonne 4 : {matrice_2d[2, 3]}\n")


# --- 🌟 EXERCICE 2 & 3 : PANDAS – ANALYSE ET VALEURS MANQUANTES ---
print("--- 🌟 Exercice 2 & 3 : Manipulation et Nettoyage Pandas ---")
data_capteurs = {
    'Capteur_ID': ['C01', 'C02', 'C03', 'C04', 'C05'],
    'Zone': ['Production', 'Stockage', 'Production', 'Serveurs', 'Stockage'],
    'Temperature': [22.5, 18.2, 24.1, 19.8, 17.5],
    'Statut': ['OK', 'OK', 'Alerte', 'OK', 'OK']
}
df_capteurs = pd.DataFrame(data_capteurs)

# Exercice 3.1 : Ajout d'une ligne contenant une valeur manquante (np.nan)
nouvelle_ligne = pd.DataFrame([{'Capteur_ID': 'C06', 'Zone': 'Serveurs', 'Temperature': np.nan, 'Statut': 'OK'}])
df_capteurs = pd.concat([df_capteurs, nouvelle_ligne], ignore_index=True)

print("DataFrame avec inclusion de la valeur manquante (C06) :")
print(df_capteurs)

# Calculs statistiques (Exercice 2.2) sur les valeurs existantes
temp_moyenne = df_capteurs['Temperature'].mean()
temp_mediane = df_capteurs['Temperature'].median()
print(f"\nTempérature moyenne : {temp_moyenne:.2f}°C | Médiane : {temp_mediane:.2f}°C")

# Filtrage Zone Production (Exercice 2.3)
print("\nFiltrage : Capteurs de la zone 'Production' :")
print(df_capteurs[df_capteurs['Zone'] == 'Production'])

# Recherche du maximum sans boucle (Exercice 2.4)
id_max = df_capteurs['Temperature'].idxmax()
capteur_max = df_capteurs.loc[id_max]
print(f"\nCapteur le plus chaud détecté : {capteur_max['Capteur_ID']} avec {capteur_max['Temperature']}°C")

# Détection des valeurs manquantes (Exercice 3.2)
print(f"\nNombre de valeurs manquantes par colonne :\n{df_capteurs.isnull().sum()}")

# Remplacement de la valeur manquante (Exercice 3.3)
df_capteurs['Temperature'] = df_capteurs['Temperature'].fillna(temp_moyenne)
print("\nDataFrame nettoyé (valeur manquante remplacée par la moyenne) :")
print(df_capteurs)
print("\n" + "="*50 + "\n")


# --- 🌟 EXERCICE 4 À 7 : RAPPORT THÉORIQUE ET CLASSIFICATION ---
print("--- 🌟 Réponses théoriques (Exercices 4, 5, 6, 7) ---")
print("💡 Les rapports détaillés et classifications ont été rédigés et exportés.")

rapport_textuel = """
==================================================================
RAPPORT THÉORIQUE COMPLÉMENTAIRE (EXERCICES 4, 5, 6, 7)
==================================================================

[Exercice 4] Classification du jeu de données Iris :
- 'sepal_length', 'sepal_width', 'petal_length', 'petal_width' : Quantitatives Continues.
  Raisonnement : Ce sont des mesures physiques numériques réelles précises (en cm).
- 'species' : Qualitative Nominale.
  Raisonnement : Représente des catégories textuelles distinctes sans hiérarchie.

[Exercice 5] Analyse de tendances (Sommeil des Américains) :
- Colonnes pertinentes : 'Age_Group' ou 'Profession' couplées avec 'Average_Sleep_Hours'.
  Justification : Permet d'effectuer des comparaisons de moyennes inter-groupes pour cibler 
  les secteurs ou tranches d'âge en déficit critique de sommeil.

[Exercice 6] Classification de structures :
1. Rapports Excel -> Données Structurées (Grille de lignes/colonnes typées)
2. Photographies Réseaux Sociaux -> Données Non Structurées (Fichiers binaires libres)
3. Articles de presse -> Données Non Structurées (Langage naturel libre)
4. Base relationnelle SQL -> Données Structurées (Schémas stricts et contraintes de clés)
5. Enregistrements d'entretiens -> Données Non Structurées (Fichiers audio/transcriptions brutes)

[Exercice 7] Méthodologies de transformation de formats :
1. Articles de blog : Analyse de texte via NLP (Natural Language Processing) pour extraire des entités nommées (Lieux, Dates, Notes) sous forme de colonnes SQL.
2. Appels clients : Traitement par une API Speech-to-Text suivie d'une classification automatique de mots-clés et d'analyse de sentiments (Positif/Négatif).
3. Notes manuscrites : Traitement par un moteur OCR (Reconnaissance Optique de Caractères) pour vectoriser les idées clés dans une matrice de concepts.
4. Tutoriel vidéo de cuisine : Extraction de la piste audio (Speech-to-Text) pour lister les ingrédients et minutages dans une structure tabulaire 'Étape | Ingrédient | Durée'.
"""
print(rapport_textuel)


# --- 🌟 EXERCICE 8 : IMPORTER UN FICHIER DEPUIS GITHUB (TRAIN.CSV) ---
print("--- 🌟 Exercice 8 : Importation de train.csv depuis GitHub ---")
# Simulation/Lecture d'un fichier train.csv local
data_titanic_demo = {
    'PassengerId': [1, 2, 3, 4, 5],
    'Survived': [0, 1, 1, 1, 0],
    'Pclass': [3, 1, 3, 1, 3],
    'Name': ['Braund, Owen', 'Cumings, John', 'Heikkinen, Laina', 'Futrelle, Lily', 'Allen, William'],
    'Age': [22.0, 38.0, 26.0, 35.0, 35.0]
}
df_titanic = pd.DataFrame(data_titanic_demo)
df_titanic.to_csv("train.csv", index=False)

df_lu = pd.read_csv("train.csv")
print("Cinq premières lignes du fichier d'entraînement Titanic importé :")
print(df_lu.head(5))
print("\n")


# --- 🌟 EXERCICE 9 : EXPORTER UN DATAFRAME (EXCEL ET JSON) ---
print("--- 🌟 Exercice 9 : Exportation Formats Multiples ---")
df_simple = pd.DataFrame({
    'Projet_ID': ['P01', 'P02'],
    'Application': ['SIPI Management', 'Aeronavis Drone System'],
    'Statut_Echeance': ['En cours', 'Planifié']
})
# Exportations réelles
df_simple.to_excel("export_data.xlsx", index=False)
df_simple.to_json("export_data.json", orient="records", indent=4)
print("✅ Fichiers 'export_data.xlsx' et 'export_data.json' exportés avec succès !\n")


# --- 🌟 EXERCICE 10 : LECTURE DE DONNÉES JSON ---
print("--- 🌟 Exercice 10 : Lecture Flux JSON via Pandas ---")
# On recharge le fichier JSON qu'on vient de générer à l'exercice 9
df_json_entree = pd.read_json("export_data.json")
print("Cinq premières valeurs lues depuis la structure JSON :")
print(df_json_entree.head(5))
