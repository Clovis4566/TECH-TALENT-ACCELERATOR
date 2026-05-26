# Daily Challenge : Système de Pagination
import math

class Pagination:
    # Étape 1 & 2 : Initialisation de la classe
    def __init__(self, items=None, page_size=10):
        # Si items est None, on l'initialise comme une liste vide
        self.items = items if items is not None else []
        
        # Conversion explicite en entier au cas où un float ou une chaîne soit passé
        self.page_size = int(page_size)
        
        # Index interne de la page actuelle (commence à 0)
        self.current_idx = 0
        
        # Calcul du nombre total de pages (minimum 1 page, même si la liste est vide)
        self.total_pages = math.ceil(len(self.items) / self.page_size)
        if self.total_pages == 0:
            self.total_pages = 1

    # Étape 3 : Récupération des éléments visibles
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # Étape 4 : Méthodes de navigation
    def go_to_page(self, page_num):
        # Conversion en entier
        page_num = int(page_num)
        
        # Les entrées utilisateur commencent à 1, donc hors limites si < 1 ou > total_pages
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Erreur : La page {page_num} n'existe pas. Total pages : {self.total_pages}")
        
        # Ajustement de l'index interne (base 0)
        self.current_idx = page_num - 1
        return self  # Permet le chaînage

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        # On passe à la page suivante uniquement si on n'est pas déjà sur la dernière
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        # On recule uniquement si on n'est pas déjà sur la première page
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    # Étape 5 (Prime) : Affichage personnalisé (__str__)
    def __str__(self):
        elements_visibles = self.get_visible_items()
        # Joint chaque élément par un saut de ligne
        return "\n".join(str(item) for item in elements_visibles)


# =====================================================================
# Étape 6 : Zone de Tests obligatoires
# =====================================================================
print("--- Début des tests du Daily Challenge ---")
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print("\n1. Éléments visibles de la première page :")
print(p.get_visible_items())  # Attendé: ['a', 'b', 'c', 'd']

print("\n2. Test de la méthode magique __str__ :")
print(str(p))

print("\n3. Passage à la page suivante (next_page) :")
p.next_page()
print(p.get_visible_items())  # Attendé: ['e', 'f', 'g', 'h']

print("\n4. Aller à la dernière page (last_page) :")
p.last_page()
print(p.get_visible_items())  # Attendé: ['y', 'z']

# Bonus : Chaînage de méthodes (le fait de chaîner .next_page() ou .previous_page())
print("\n5. Test Bonus - Chaînage de méthodes :")
# On revient d'abord à la première page
p.first_page()
# Chaînage de 3 pages à la suite
resultat_chainage = p.next_page().next_page().next_page().get_visible_items()
print(f"Après 3 next_page() consécutifs : {resultat_chainage}")  # Attendé: ['m', 'n', 'o', 'p']

print("\n6. Tests de gestion des erreurs (Exceptions) :")
try:
    p.go_to_page(10)
except ValueError as e:
    print(f"🔥 Erreur capturée avec succès (page 10) : {e}")

try:
    p.go_to_page(0)
except ValueError as e:
    print(f"🔥 Erreur capturée avec succès (page 0) : {e}")
