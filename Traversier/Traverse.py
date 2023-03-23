from typing import List
from datetime import datetime
from Client import Client
from Employe import Employe
from Traversier import Traversier
from Vehicule import Vehicule

class Traverse:
    def __init__(self, no_traverse: int, date_heure_depart: str, ville_depart: str, employe_inscription: Employe, liste_vehicule: List[Vehicule],
                 liste_client: List[Client], la_traversier: Traversier):
        self._no_traverse = no_traverse
        self._date_heure_depart = date_heure_depart
        self._ville_depart = ville_depart
        self._employe_inscription = employe_inscription
        self._liste_vehicule = liste_vehicule
        self._liste_client = liste_client
        self._la_traversier = la_traversier

    def get_no_traverse(self) -> int:
        return self._no_traverse

    def set_no_traverse(self, no_traverse: int):
        self._no_traverse = no_traverse

    def get_date_heure_depart(self) -> str:
        return self._date_heure_depart

    def set_date_heure_depart(self, date_heure_depart: str):
        self._date_heure_depart = date_heure_depart
    
    def get_ville_depart(self) -> str:
        return self._ville_depart

    def set_ville_depart(self, ville_depart: str):
        self._ville_depart = ville_depart

    def get_employe_inscription(self) -> Employe:
        return self._employe_inscription

    def set_employe_inscription(self, employe_inscription: Employe):
        self._employe_inscription = employe_inscription

    def get_liste_vehicule(self) -> List[Vehicule]:
        return self._liste_vehicule

    def set_liste_vehicule(self, liste_vehicule: List[Vehicule]):
        self._liste_vehicule = liste_vehicule

    def get_liste_client(self) -> List[Client]:
        return self._liste_client

    def set_liste_client(self, liste_client: List[Client]):
        self._liste_client = liste_client

    def get_la_traversier(self) -> Traversier:
        return self._la_traversier

    def set_la_traversier(self, la_traversier: Traversier):
        self._la_traversier = la_traversier

    def calculer_revenu_traversee(self) -> float:
        revenu_total = 0
        for vehicule in self._liste_vehicule:
            revenu_total += vehicule.get_le_type().get_prix_traverse()
        return revenu_total

    def ToStringListeClients(self):
        if len(self._liste_client) == 0:
            return "Aucun clients associe a cette traverse."
        else:
            result = ""
            for client in self._liste_client:
                result += client.__str__() + "\n"
            return result

    def ToStringListeVehicules(self):
        if len(self._liste_vehicule) == 0:
            return "Aucun vehicules associe a cette traverse."
        else:
            result = ""
            for vehicule in self._liste_vehicule:
                result += vehicule.__str__() + "\n"
            return result

    def __str__(self):
        return f"No. Traversier: {self._no_traverse}\n" \
                f"Date et Heure de depart: {self._date_heure_depart}\n"  \
                f"Ville de depart: {self._ville_depart}\n" \
                f"Employe responsable de l'inscription: {self._employe_inscription.__str__()}\n" \
                f"Liste des vehicules:\n{self.ToStringListeVehicules()}\n" \
                f"Liste des clients:\n{self.ToStringListeClients()}\n" \
                f"{self._la_traversier.__str__()}"

    def __hash__(self):
        return hash(self._no_traverse)

    def __eq__(self, other):
        if not isinstance(other, Traverse):
            return False
        return self._no_traverse == other._no_traverse
