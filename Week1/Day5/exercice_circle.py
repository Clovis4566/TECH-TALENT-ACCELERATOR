# Mini-Projet : Gestion géométrique des Cercles (Méthodes Dunder)
import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        """
        Initialise un cercle soit par son rayon, soit par son diamètre.
        Si les deux sont fournis, le rayon est prioritaire.
        """
        if radius is not None:
            self.radius = float(radius)
        elif diameter is not None:
            self.radius = float(diameter) / 2.0
        else:
            raise ValueError("Tu dois spécifier soit un rayon ('radius'), soit un diamètre ('diameter').")

    @property
    def diameter(self):
        """Décorateur Property pour interroger le diamètre dynamiquement."""
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        """Permet de modifier le diamètre, ce qui ajuste automatiquement le rayon."""
        self.radius = float(value) / 2.0

    @property
    def area(self):
        """Calcule et renvoie l'aire du cercle (A = pi * r²)."""
        return math.pi * (self.radius ** 2)

    # --- MÉTHODES DUNDER (MAGIQUES) ---

    def __str__(self):
        """Affichage lisible de l'objet (via print ou str)."""
        return f"🔴 Cercle - Rayon: {self.radius:.2f} | Diamètre: {self.diameter:.2f} | Aire: {self.area:.2f}"

    def __repr__(self):
        """Représentation officielle de l'objet dans une liste."""
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        """Additionne deux cercles et renvoie un nouveau cercle avec la somme des rayons."""
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __eq__(self, other):
        """Vérifie si deux cercles sont égaux (comparaison des rayons)."""
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False

    def __gt__(self, other):
        """Vérifie si le cercle actuel est strictement plus grand qu'un autre."""
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __lt__(self, other):
        """Vérifie si le cercle actuel est plus petit (indispensable pour la fonction sort())."""
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented
