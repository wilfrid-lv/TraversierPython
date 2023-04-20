from Personne import Personne
class Employe(Personne):
    def __init__(self, nom: str, adresse: str, ville: str, province: str, codePostal: str, telephone: str, courriel: str,
                 noEmploye: int, nAS: int, dateEmbauche: str, dateArret: str = None):
        super().__init__(nom, adresse, ville, province, codePostal, telephone, courriel)
        self.noEmploye = noEmploye
        self.nAS = nAS
        self.dateEmbauche = dateEmbauche
        self.dateArret = dateArret

    def get_noEmploye(self) -> int:
        return self.noEmploye

    def set_noEmploye(self, noEmploye: int) -> None:
        self.noEmploye = noEmploye

    def get_nAS(self) -> int:
        return self.nAS

    def set_nAS(self, nAS: int) -> None:
        self.nAS = nAS

    def get_dateEmbauche(self) -> str:
        return self.dateEmbauche

    def set_dateEmbauche(self, dateEmbauche: str) -> None:
        self.dateEmbauche = dateEmbauche

    def get_dateArret(self) -> str:
        return self.dateArret
    
    def set_dateArret(self, dateArret: str) -> None:
        self.dateArret = dateArret

    def __str__(self) -> str:
        if self.get_dateArret() is None:
            return  super().__str__() + f", {self.get_nom()}, {self.get_noEmploye()}, {self.get_nAS()}, {self.get_dateEmbauche()}, en poste"
        else:
            return  super().__str__() + f", {self.get_nom()}, {self.get_noEmploye()}, {self.get_nAS()}, {self.get_dateEmbauche()}, {self.get_dateArret()}"

    def __hash__(self) -> int:
        return hash(self.get_noEmploye())

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Employe):
            return False
        return self.get_noEmploye() == other.get_noEmploye()