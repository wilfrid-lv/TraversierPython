from datetime import datetime
from typing import List

class Traversier:
    def __init__(self, nom: str, capaciteVehicule: int, capacitePersonne: int, anneeFabrication: int, dateMiseService: datetime, listeEmploye: List[Employe]):
        self.nom = nom
        self.capaciteVehicule = capaciteVehicule
        self.capacitePersonne = capacitePersonne
        self.anneeFabrication = anneeFabrication
        self.dateMiseService = dateMiseService
        self.listeEmploye = listeEmploye


        #def ajouterEmploye(self, employe):
        #self.listeEmploye.append(employe)
    
    def ToString(self) -> str:
        return f"Nom: {self.nom}, Capacité véhicule: {self.capaciteVehicule}, Capacité personne: {self.capacitePersonne}, Année de fabrication: {self.anneFabrication}, Date de mise en service: {self.dateMiseService}"
    
    def Equals(self, other) -> bool:
        if isinstance(other, Traversier):
            return self.nom == other.nom and self.capaciteVehicule == other.capaciteVehicule and self.capacitePersonne == other.capacitePersonne and self.anneFabrication == other.anneFabrication and self.dateMiseService == other.dateMiseService
        else:
            return False
    
    def GetHashCode(self) -> int:
        return hash((self.nom, self.capaciteVehicule, self.capacitePersonne, self.anneFabrication, self.dateMiseService, tuple(self.listeEmploye)))