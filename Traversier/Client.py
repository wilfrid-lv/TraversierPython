import Personne

class Client(Personne):
    def __init__(self, nom, adresse, ville, province, code_postal, telephone, courriel, numeroIdentification, sexe, dateNaissance):
        super().__init__(nom, adresse, ville, province, code_postal, telephone, courriel)
        self.numeroIdentification = numeroIdentification
        self.sexe = sexe
        self.dateNaissance = dateNaissance

    def ToString(self) -> str:
        return f"Client - Nom: {self.nom}, Numero Identification: {self.numeroIdentification}"

    def Equals(self, other: object) -> bool:
        if not isinstance(other, Client):
            return False
        return self.numeroIdentification == other.numeroIdentification

    def GetHashCode(self) -> int:
        return hash(self.numeroIdentification)