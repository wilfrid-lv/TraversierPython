from tkinter import *
from tkinter import ttk
#from InterfaceMenu import InterfaceMenu

#mettre les def là
def click():
    id = noTraverse.get()
    date = dateHeure.get()
    villeD = villeDepart.get()
    employe = employeInscription.get()
    print(id)
    print(date)
    print(villeD)
    print(employe)

#def sellectionner():
    #doit mettre une liste deroulante qui recupere les employés

root = Tk()
root.title("Traverse")

#faire la frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Info de la traverse").grid(column=1, row=1)

noTraverse = ttk.Entry(mainframe, width=7)
noTraverse.grid(column=2, row=2, sticky=(W, E))
dateHeure = ttk.Entry(mainframe, width=7)
dateHeure.grid(column=2, row=3, sticky=(W, E))
villeDepart = ttk.Entry(mainframe, width=7)
villeDepart.grid(column=2, row=4, sticky=(W, E))
employeInscription = ttk.Entry(mainframe, width=7)
employeInscription.grid(column=2, row=5, sticky=(W, E))
#listeVehicule = ttk.Entry(mainframe, width=7)
#listeVehicule.grid(column=2, row=6, sticky=(W, E))
#listeClient = ttk.Entry(mainframe, width=7)
#listeClient.grid(column=2, row=6, sticky=(W, E))

# Liste déroulante pour listeVehicule
listeVehicule = ttk.Combobox(mainframe, width=7, values=["Vehicule 1", "Vehicule 2", "Vehicule 3"])
listeVehicule.grid(column=2, row=6, sticky=(W, E))

# Liste déroulante pour listeEmploye
listeEmploye = ttk.Combobox(mainframe, width=7, values=["Employe 1", "Employe 2", "Employe 3"])
listeEmploye.grid(column=2, row=7, sticky=(W, E))


ttk.Button(mainframe, text="Enregistrer", command=click).grid(column=3, row=10, sticky=W)
#ttk.Button(mainframe, text="Sel. Employe", command=selectionner).grid(column=3, row=7, sticky=W)

ttk.Label(mainframe, text="noTraverse").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="dateHeure").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="villeDepart").grid(column=1, row=4, sticky=E)
ttk.Label(mainframe, text="employeInscription").grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, text="listeVehicule").grid(column=1, row=6, sticky=E)
ttk.Label(mainframe, text="listeClient").grid(column=1, row=7, sticky=E)

