from employe import Employe
from vehicule import Vehicule
from client import Client
from datetime import datetime

class Traverse:
    def __init__(self, noTraverse: int, dateHeure: datetime, villeDepart: str, employeInscription: Employe, listeVehicule: list[Vehicule], listeClient: list[Client]):
        self.noTraverse = noTraverse
        self.dateHeure = dateHeure
        self.villeDepart = villeDepart
        self.employeInscription = employeInscription
        self.listeVehicule = listeVehicule
        self.listeClient = listeClient


    def __str__(self) -> str:
        return f"No de traverse: {self.noTraverse}, Date et heure: {self.dateHeure}, Ville de départ: {self.villeDepart}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Traverse):
            return False
        return self.noTraverse == other.noTraverse

    def __hash__(self) -> int:
        return hash(self.noTraverse)

    def calculerRevenuTraverse(self):
        revenu = 0
        for vehicule in self.listeVehicule:
            revenu += vehicule.type.prixTraverse
        for client in self.listeClient:
            revenu += client.prixTraverse
        return revenu

    def listeClient(self):
        return [client.nom for client in self.listeClient]

    def listeVehicule(self):
        return [vehicule.immatriculation for vehicule in self.listeVehicule]
