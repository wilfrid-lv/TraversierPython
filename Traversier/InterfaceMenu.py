#from asyncore import loop
#from struct import pack
#import tkinter as tk
#from tkinter import *
#from tkinter import ttk

#window = tk.Tk()
#window.title('Interface Traversier')
#window.geometry('400x400')


#mainframe = ttk.Frame(window, padding="3 3 12 12")
#mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#window.columnconfigure(0, weight=1)
#window.rowconfigure(0, weight=1)


#hello = ttk.Label(mainframe, #window, 
#                 textvariable='Interface Traversier',
#                 #bg='#000000',
#                 #fg='#FFFFFF',
#                 #font=('Arial', 20),
#                 #height=10,
#                 #width=20
#                 )
#hello.grid(row=1, sticky=(W, E))

#frame = tk.Frame(window, 
#                 width=20,
#                 height=5
#                 ).grid(row=2)

#entry = ttk.Entry(mainframe, #window,  
#                 width=20
#                 ).grid(row=3)
#def click():
#    nom = entry.get()
#    hello.config()
#    print(nom)

#button = tk.Button(window,
#                  text='Enregistrer',
#                  bg='blue',
#                  fg='white',
#                  height=5,
#                  width=10,
#                  command=click
#                  ).grid(row=4)

##hello.grid(row=0, column=1 )
##entry.grid(row=1, column=1 )
##button.grid(row=2, column=1 )

##hello.pack()#permet de l'ajouter a la fenetre
##frame.pack()
##entry.pack()
##button.pack()
##window.mainloop()

##on ne peut utiliser que pack ou que grid sur une page.


from tkinter import *
from tkinter import ttk
import InterfaceTraverse 

#mettre la classe pour naviguer entre les vue
class windowclass():
    def __init__(self, master):
        master = master
        btn = ttk.Button(master, text="Button", command=self.command)
        btn.grid(column=1, row=3)

    def command(master):
        if master.winfo_exists():
            master.withdraw()
            toplevel = ttk.Toplevel(master)
            toplevel.geometry("350x350")
            app = InterfaceTraverse(toplevel)
    
    #def command2(self):
    #    self.master.withdraw()
    #    toplevel = tk.Toplevel(self.master)
    #    toplevel.geometry("350x350")
    #    app = Demo3(toplevel)



#mettre les def là
#def click():
#    traverse = entryTraverse.get()
#    traversier = entryTraversier.get()
#    client = entryClient.get()
#    vehicule = entryVehicule.get()
#    employe = entryEmploye.get()
#    print(traverse)
#    print(traversier)
#    print(client)
#    print(vehicule)
#    print(employe)

#def redirect():
#    window = Toplevel(root)
#    window.title("InterfaceTraverse")


#def sellectionner():
    #doit mettre une liste deroulante qui recupere les employés

root = Tk()
root.title("Traversier")

#faire la frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Info de la traverse").grid(column=1, row=1)

entryTraverse = ttk.Entry(mainframe, width=7)
entryTraverse.grid(column=2, row=2, sticky=(W, E))
entryTraversier = ttk.Entry(mainframe, width=7)
entryTraversier.grid(column=2, row=3, sticky=(W, E))
entryClient = ttk.Entry(mainframe, width=7)
entryClient.grid(column=2, row=4, sticky=(W, E))
entryVehicule = ttk.Entry(mainframe, width=7)
entryVehicule.grid(column=2, row=5, sticky=(W, E))
entryEmploye = ttk.Entry(mainframe, width=7)
entryEmploye.grid(column=2, row=6, sticky=(W, E))


ttk.Button(mainframe, text="Info Traverse", command=windowclass(root).command).grid(column=3, row=8, sticky=W)
#ttk.Button(mainframe, text="Enregistrer", command=click).grid(column=3, row=7, sticky=W)
#ttk.Button(mainframe, text="Sel. Employe", command=selectionner).grid(column=3, row=7, sticky=W)

ttk.Label(mainframe, text="Traverse").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Traversier").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="Client").grid(column=1, row=4, sticky=E)
ttk.Label(mainframe, text="Vehicule").grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, text="Employe").grid(column=1, row=6, sticky=E)

root.mainloop()