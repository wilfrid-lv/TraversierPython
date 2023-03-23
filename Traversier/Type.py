class Type:
    def __init__(self, nom: str, nombreRoue: int, prixTraverse: float):
        self.nom = nom
        self.nombreRoue = nombreRoue
        self.prixTraverse = prixTraverse

    def get_nom(self) -> str:
        return self.nom

    def set_nom(self, nom: str) -> None:
        self.nom = nom

    def get_nombreRoue(self) -> int:
        return self.nombreRoue

    def set_nombreRoue(self, nombreRoue: int) -> None:
        self.nombreRoue = nombreRoue

    def get_prixTraverse(self) -> float:
        return self.prixTraverse

    def set_prixTraverse(self, prixTraverse: float) -> None:
        self.prixTraverse = prixTraverse

    def __str__(self) -> str:
        return f"{self.get_nom()}, {self.get_nombreRoue()} roues, {self.get_prixTraverse()} $ par traversee"

    def __hash__(self) -> int:
        return hash((self.get_nom(), self.get_nombreRoue(), self.get_prixTraverse()))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Type):
            return False
        return (self.get_nom(), self.get_nombreRoue(), self.get_prixTraverse()) == (other.get_nom(), other.get_nombreRoue(), other.get_prixTraverse())