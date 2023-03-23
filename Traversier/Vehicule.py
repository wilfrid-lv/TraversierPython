from Type import Type
class Vehicule:
    def __init__(self, noIdentification: int, marque: str, modele: str, couleur: str, annee: int, immatriculation: str, leType: Type):
        self.noIdentification = noIdentification
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.annee = annee
        self.immatriculation = immatriculation
        self.leType = leType

    def get_noIdentification(self) -> int:
        return self.noIdentification

    def set_noIdentification(self, noIdentification: int) -> None:
        self.noIdentification = noIdentification

    def get_marque(self) -> str:
        return self.marque

    def set_marque(self, marque: str) -> None:
        self.marque = marque

    def get_modele(self) -> str:
        return self.modele

    def set_modele(self, modele: str) -> None:
        self.modele = modele

    def get_couleur(self) -> str:
        return self.couleur

    def set_couleur(self, couleur: str) -> None:
        self.couleur = couleur

    def get_annee(self) -> int:
        return self.annee

    def set_annee(self, annee: int) -> None:
        self.annee = annee

    def get_immatriculation(self) -> str:
        return self.immatriculation

    def set_immatriculation(self, immatriculation: str) -> None:
        self.immatriculation = immatriculation

    def get_leType(self) -> Type:
        return self.leType

    def set_leType(self, leType: Type) -> None:
        self.leType = leType

    def __str__(self) -> str:
        return f"{self.get_marque()} {self.get_modele()} ({self.get_annee()}) de couleur {self.get_couleur()} avec immatriculation {self.get_immatriculation()}, identifiant {self.get_noIdentification()} et de type {self.get_leType().__str__()}"

    def __hash__(self) -> int:
        return hash((self.get_noIdentification(), self.get_marque(), self.get_modele(), self.get_couleur(), self.get_annee(), self.get_immatriculation(), self.get_leType()))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vehicule):
            return False
        return (self.get_noIdentification(), self.get_marque(), self.get_modele(), self.get_couleur(), self.get_annee(), self.get_immatriculation(), self.get_leType()) == (other.get_noIdentification(), other.get_marque(), other.get_modele(), other.get_couleur(), other.get_annee(), other.get_immatriculation(), other.get_leType())