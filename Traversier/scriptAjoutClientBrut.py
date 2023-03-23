import xml.etree.ElementTree as ET

tree = ET.parse("clients.xml")
root = tree.getroot()

client = ET.SubElement(root, "client")
client.set("id", "1")

nom = ET.SubElement(client, "nom")
nom.text = "Wilfrid Le Valegant"

adresse = ET.SubElement(client, "adresse")
adresse.text = "37 rue front."

ville = ET.SubElement(client, "ville")
ville.text = "Montreal"

province = ET.SubElement(client, "province")
province.text = "Quebec"

code_postal = ET.SubElement(client, "code_postal")
code_postal.text = "G5R 1X5"

telephone = ET.SubElement(client, "telephone")
telephone.text = "514-123-4567"

courriel = ET.SubElement(client, "courriel")
courriel.text = "wilfridlv@live.com"

numero_identification = ET.SubElement(client, "numero_identification")
numero_identification.text = "1234567890"

sexe = ET.SubElement(client, "sexe")
sexe.text = "Homme"

tree.write("clients.xml")
