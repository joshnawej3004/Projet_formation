import calcul

resultat = calcul.racine_carre(25)
print("Le resultat vaut", resultat)

class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        
    def afficher(self):
        print(f"{self.titre} par {self.auteur} publie en {self.annee}")
        
livre1 = Livre("Le petit chose", "Josh", 1867)
livre1.afficher()
# print(livre1)