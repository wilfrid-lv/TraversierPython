from typing import List
from datetime import datetime
from Employe import Employe

class Traversier:
    def __init__(self, nom: str, capaciteVehicule: int, capacitePersonne: int, anneeFabrication: datetime, dateMiseService: datetime, listeEmploye: List[Employe]):
        self.nom = nom
        self.capaciteVehicule = capaciteVehicule
        self.capacitePersonne = capacitePersonne
        self.anneeFabrication = anneeFabrication
        self.dateMiseService = dateMiseService
        self.listeEmploye = listeEmploye

    def get_nom(self) -> str:
        return self.nom

    def set_nom(self, nom: str):
        self.nom = nom

    def get_capaciteVehicule(self) -> int:
        return self.capaciteVehicule

    def set_capaciteVehicule(self, capaciteVehicule: int):
        self.capaciteVehicule = capaciteVehicule

    def get_capacitePersonne(self) -> int:
        return self.capacitePersonne

    def set_capacitePersonne(self, capacitePersonne: int):
        self.capacitePersonne = capacitePersonne

    def get_anneeFabrication(self) -> datetime:
        return self.anneeFabrication

    def set_anneeFabrication(self, anneeFabrication: datetime):
        self.anneeFabrication = anneeFabrication

    def get_dateMiseService(self) -> datetime:
        return self.dateMiseService

    def set_dateMiseService(self, dateMiseService: datetime):
        self.dateMiseService = dateMiseService
    
    def get_listeEmploye(self) -> List[Employe]:
        return self.listeEmploye
    
    def set_listeEmploye(self, listeEmploye: List[Employe]):
        self.listeEmploye = listeEmploye

    def __str__(self):
        return f"Nom du traversier: {self.nom}\nCapacite en vehicules: {self.capaciteVehicule}\nCapacite en personnes: {self.capacitePersonne}\nAnnee de fabrication: {self.anneeFabrication}\nDate de mise en service: {self.dateMiseService}\n\nListe des employes:\n{self.ToStringListeEmploye()}"

    def ToStringListeEmploye(self):
        if len(self.listeEmploye) == 0:
            return "Aucun employe associe a ce traversier."
        else:
            employes = ""
            for employe in self.listeEmploye:
                employes += f"{employe.__str__()}\n"
            return employes

    def __hash__(self) -> int:
        return hash((self.nom, self.anneeFabrication))

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Traversier):
            return self.nom == obj.nom and self.anneeFabrication == obj.anneeFabrication
            return False
    
    def GetHashCode(self) -> int:
        return hash((self.nom, self.capaciteVehicule, self.capacitePersonne, self.anneFabrication, self.dateMiseService, tuple(self.listeEmploye)))