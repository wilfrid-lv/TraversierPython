from Personne import Personne
class Client(Personne):
    def __init__(self, nom: str, adresse: str, ville: str, province: str, codePostal: str, telephone: str, courriel: str,
                 numeroIdentification: int, sexe: str, dateNaissance: str):
        super().__init__(nom, adresse, ville, province, codePostal, telephone, courriel)
        self.numeroIdentification = numeroIdentification
        self.sexe = sexe
        self.dateNaissance = dateNaissance

    def get_numeroIdentification(self) -> int:
        return self.numeroIdentification

    def set_numeroIdentification(self, numeroIdentification: int) -> None:
        self.numeroIdentification = numeroIdentification

    def get_sexe(self) -> str:
        return self.sexe

    def set_sexe(self, sexe: str) -> None:
        self.sexe = sexe

    def get_dateNaissance(self) -> str:
        return self.dateNaissance

    def set_dateNaissance(self, dateNaissance: str) -> None:
        self.dateNaissance = dateNaissance

    def __str__(self) -> str:
        return super().__str__() +  f", {self.get_sexe()}, {self.get_numeroIdentification()}, {self.get_dateNaissance()}"

    def __hash__(self) -> int:
        return hash(self.get_numeroIdentification())

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Client):
            return False
        return self.get_numeroIdentification() == other.get_numeroIdentification()