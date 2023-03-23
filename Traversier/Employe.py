import Personne

class Employe(Personne):
    def __init__(self, nom, adresse, ville, province, code_postal, telephone, courriel, noEmploye, nAS, dateEmbauche, dateArret):
        super().__init__(nom, adresse, ville, province, code_postal, telephone, courriel)
        self.noEmploye = noEmploye
        self.nAS = nAS
        self.dateEmbauche = dateEmbauche
        self.dateArret = dateArret

    def ToString(self) -> str:
        return f"Employé: {self.nom}, {self.adresse}, {self.ville}, {self.province}, {self.codePostal}, {self.telephone}, {self.courriel}, {self.noEmploye}, {self.nAS}, {self.dateEmbauche}, {self.dateArret}"
    
    def Equals(self, obj: object) -> bool:
        if isinstance(obj, Employe):
            return self.noEmploye == obj.noEmploye
        else:
            return False
    
    def GetHashCode(self) -> int:
        return hash((self.noEmploye,))


