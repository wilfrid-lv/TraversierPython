import tkinter as tk
from tkinter import ttk
from typing import List
from xml.etree import ElementTree as ET
import Client


class ClientApp:
    def __init__(self, master):
        self.master = master
        master.title("Ajouter un client")

        self.label_nom = ttk.Label(self.master, text="Nom :")
        self.label_nom.grid(row=0, column=0, sticky=tk.W)

        self.nom = tk.StringVar()
        self.entry_nom = ttk.Entry(self.master, textvariable=self.nom)
        self.entry_nom.grid(row=0, column=1)

        self.label_adresse = ttk.Label(self.master, text="Adresse :")
        self.label_adresse.grid(row=1, column=0, sticky=tk.W)

        self.adresse = tk.StringVar()
        self.entry_adresse = ttk.Entry(self.master, textvariable=self.adresse)
        self.entry_adresse.grid(row=1, column=1)

        self.label_ville = ttk.Label(self.master, text="Ville :")
        self.label_ville.grid(row=2, column=0, sticky=tk.W)

        self.ville = tk.StringVar()
        self.entry_ville = ttk.Entry(self.master, textvariable=self.ville)
        self.entry_ville.grid(row=2, column=1)

        self.label_province = ttk.Label(self.master, text="Province :")
        self.label_province.grid(row=3, column=0, sticky=tk.W)

        self.province = tk.StringVar()
        self.entry_province = ttk.Entry(self.master, textvariable=self.province)
        self.entry_province.grid(row=3, column=1)

        self.label_code_postal = ttk.Label(self.master, text="Code postal :")
        self.label_code_postal.grid(row=4, column=0, sticky=tk.W)

        self.code_postal = tk.StringVar()
        self.entry_code_postal = ttk.Entry(self.master, textvariable=self.code_postal)
        self.entry_code_postal.grid(row=4, column=1)

        self.label_telephone = ttk.Label(self.master, text="T�l�phone :")
        self.label_telephone.grid(row=5, column=0, sticky=tk.W)

        self.telephone = tk.StringVar()
        self.entry_telephone = ttk.Entry(self.master, textvariable=self.telephone)
        self.entry_telephone.grid(row=5, column=1)

        self.label_courriel = ttk.Label(self.master, text="Courriel :")
        self.label_courriel.grid(row=6, column=0, sticky=tk.W)

        self.courriel = tk.StringVar()
        self.entry_courriel = ttk.Entry(self.master, textvariable=self.courriel)
        self.entry_courriel.grid(row=6, column=1)

        self.label_numero_identification = ttk.Label(self.master, text="Num�ro d'identification :")
        self.label_numero_identification.grid(row=7, column=0, sticky=tk.W)

        self.numero_identification = tk.IntVar()
        self.entry_numero_identification = ttk.Entry(self.master, textvariable=self.numero_identification)
        self.entry_numero_identification.grid(row=7, column=1)

        self.label_sexe = ttk.Label(self.master, text="Sexe :")
        self.label_sexe.grid(row=8, column=0, sticky=tk.W)

        self.sexe = tk.StringVar()
        self.combo_sexe = ttk.Combobox(self.master, textvariable=self.sexe, values=["Homme", "Femme", "Autre"]

        self.button_ajouter = ttk.Button(self.master, text="Ajouter", command=self.ajouter_client)
        self.button_ajouter.grid(row=9, column=0)

    def ajouter_client(self):
        # Cr�er une instance de la classe Client avec les valeurs entr�es dans les champs
        nouveau_client = Client(self.nom.get(), self.adresse.get(), self.ville.get(), self.province.get(), 
                                self.code_postal.get(), self.telephone.get(), self.courriel.get(),
                                self.numero_identification.get(), self.sexe.get())
    
        # Ajouter le nouveau client � la liste de clients
        clients = self.lire_clients()
        clients.append(nouveau_client)
    
        # �crire la liste de clients mise � jour dans le fichier XML
        self.ecrire_clients(clients)

        # Afficher un message de confirmation
        tk.messagebox.showinfo("Confirmation", "Le client a �t� ajout� avec succ�s.")

    def lire_clients(self) -> List[Client]:
        tree = ET.parse('clients.xml')
        root = tree.getroot()
        clients = []
        for element in root.findall('client'):
            nom = element.find('nom').text
            adresse = element.find('adresse').text
            ville = element.find('ville').text
            province = element.find('province').text
            code_postal = element.find('code_postal').text
            telephone = element.find('telephone').text
            courriel = element.find('courriel').text
            numero_identification = int(element.find('numero_identification').text)
            sexe = element.find('sexe').text
            client = Client(nom, adresse, ville, province, code_postal, telephone, courriel, numero_identification, sexe)
            clients.append(client)
        return clients

    def ecrire_clients(self, clients: List[Client]):
        root = ET.Element('clients')
        for client in clients:
            element_client = ET.SubElement(root, 'client')
            element_nom = ET.SubElement(element_client, 'nom')
            element_nom.text = client.nom
            element_adresse = ET.SubElement(element_client, 'adresse')
            element_adresse.text = client.adresse
            element_ville = ET.SubElement(element_client, 'ville')
            element_ville.text = client.ville
            element_province = ET.SubElement(element_client, 'province')
            element_province.text = client.province
            element_code_postal = ET.SubElement(element_client, 'code_postal')
            element_code_postal.text = client.code_postal
            element_telephone = ET.SubElement(element_client, 'telephone')
            element_telephone.text = client.telephone
            element_courriel = ET.SubElement(element_client, 'courriel')
            element_courriel.text = client.courriel
            element_numero_identification = ET.SubElement(element_client, 'numero_identification')
            element_numero_identification.text = str(client.numero_identification)
            element_sexe = ET.SubElement(element_client, 'sexe')
            element_sexe.text = client.sexe
        tree = ET.ElementTree(root)
        tree.write('clients.xml')

