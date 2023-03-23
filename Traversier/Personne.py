class Personne:
    def __init__(self, nom, adresse, ville, province, code_postal, telephone, courriel):
        self.nom = nom
        self.adresse = adresse
        self.ville = ville
        self.province = province
        self.code_postal = code_postal
        self.telephone = telephone
        self.courriel = courriel

    def __str__(self):
        return f"{self.nom} ({self.telephone})"
    
    def __eq__(self, other):
        if not isinstance(other, Personne):
            return False
        return self.nom == other.nom and self.adresse == other.adresse and \
            self.ville == other.ville and self.province == other.province and \
            self.codePostal == other.codePostal and self.telephone == other.telephone and \
            self.courriel == other.courriel
    
    def __hash__(self):
        return hash((self.nom, self.adresse, self.ville, self.province, self.codePostal, 
                     self.telephone, self.courriel))

