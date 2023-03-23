class Type:
    def __init__(self, nom, nombreRoue, prixTraverse):
        self.nom = nom
        self.nombreRoue = nombreRoue
        self.prixTraverse = prixTraverse

    def __str__(self): #retourner une chaîne de caractères qui représente l'objet de la classe
        return f"{self.nom} ({self.nombreRoue} roues) : {self.prixTraverse}$ par traverse"



