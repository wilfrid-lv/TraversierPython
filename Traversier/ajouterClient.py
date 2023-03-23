import xml.etree.ElementTree as ET
import Client

def ajouter_client(client: Client, xml_file: str):
    # Créer un élément XML pour le client
    client_elem = ET.Element("client")

    nom_elem = ET.SubElement(client_elem, "nom")
    nom_elem.text = client.nom

    adresse_elem = ET.SubElement(client_elem, "adresse")
    adresse_elem.text = client.adresse

    ville_elem = ET.SubElement(client_elem, "ville")
    ville_elem.text = client.ville

    province_elem = ET.SubElement(client_elem, "province")
    province_elem.text = client.province

    code_postal_elem = ET.SubElement(client_elem, "code_postal")
    code_postal_elem.text = client.code_postal

    telephone_elem = ET.SubElement(client_elem, "telephone")
    telephone_elem.text = client.telephone

    courriel_elem = ET.SubElement(client_elem, "courriel")
    courriel_elem.text = client.courriel

    numero_identification_elem = ET.SubElement(client_elem, "numero_identification")
    numero_identification_elem.text = str(client.numero_identification)

    sexe_elem = ET.SubElement(client_elem, "sexe")
    sexe_elem.text = client.sexe

    # Ajouter l'élément du client à l'arbre XML
    tree = ET.parse(xml_file)
    root = tree.getroot()
    root.append(client_elem)

    # Écrire l'arbre XML modifié dans le fichier XML
    tree.write(xml_file)
