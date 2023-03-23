class Personne:
    def __init__(self, nom: str, adresse: str, ville: str, province: str, codePostal: str, telephone: str, courriel: str):
        self.nom = nom
        self.adresse = adresse
        self.ville = ville
        self.province = province
        self.codePostal = codePostal
        self.telephone = telephone
        self.courriel = courriel

    def get_nom(self) -> str:
        return self.nom

    def set_nom(self, nom: str) -> None:
        self.nom = nom

    def get_adresse(self) -> str:
        return self.adresse

    def set_adresse(self, adresse: str) -> None:
        self.adresse = adresse

    def get_ville(self) -> str:
        return self.ville

    def set_ville(self, ville: str) -> None:
        self.ville = ville

    def get_province(self) -> str:
        return self.province

    def set_province(self, province: str) -> None:
        self.province = province

    def get_codePostal(self) -> str:
        return self.codePostal

    def set_codePostal(self, codePostal: str) -> None:
        self.codePostal = codePostal

    def get_telephone(self) -> str:
        return self.telephone

    def set_telephone(self, telephone: str) -> None:
        self.telephone = telephone

    def get_courriel(self) -> str:
        return self.courriel

    def set_courriel(self, courriel: str) -> None:
        self.courriel = courriel

    def __str__(self):
        return f"{self.nom}, {self.adresse}, {self.ville}, {self.province}, {self.codePostal}, {self.telephone}, {self.courriel}"