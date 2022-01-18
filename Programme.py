import numpy as np
import os

def trad(tab):
    if tab[6] == '[S],':
        tab[6]  = "SYN"
    elif tab[6] == '[P],':
        tab[6] = "PUSH"
    elif tab[6] == '[R],':
        tab[6] = "RST"
    elif tab[6] == "[.],":
        tab[6] = "ACK"
    elif tab[6] == '[P.],':
        tab[6] = "PUSH ACK"
    elif tab[6] == '[S.],':
        tab[6] = "SYN ACK"
    elif tab[6] == '[F.],':
        tab[6] = "FIN ACK"
    return tab

chemin="wireshark.txt"
def fnct(chemin: str):
    try:
        
        with open(chemin, encoding="utf8") as fh:
            res=fh.read()
    except:
        print("Le fichier n'existe pas %s", os.path.abspath(chemin))
    ress=res.split('\n')
    
    tableau_evenements=np.array([])  
    evenement_2=''
    evenement_3 = ''
    
    
    for event in ress:
        # Initialisation chaine de carcatere
        if event.startswith('11:42'):
            texte=event.split()
            print(texte)
            trad(texte)
            if texte[5] == "Flags":
                if "BP-Linux8" in texte[2]:
                    texte[2] = "BP-Linux8"
                if "BP-Linux8" in texte[4]:
                    texte[4] = "BP-Linux8"
                evenement='temps : '+texte[0]+';'+' Adresse Ip source : '+texte[2]+';'+' Adresse IP destinataire : '+texte[4]+';'+' flag : '+texte[6]+';'
                if texte[6] == "SYN":
                    evenement_3 = 'Protocole :' +texte[len(texte)-1]+';'
                    evenement_2 = 'Numéro de séquence : '+texte[8]+';'+' Taille de la fenêtre : '+texte[10]+';'+' Longueur du paquet : '+texte[len(texte)-2]+';'
                if texte[6] == "PUSH":
                    evenement_3 = ' '
                    evenement_2 = 'Numéro de séquence : '+texte[8]+';'+' Numéro accusé de réception : '+texte[10]+';'
                    
                if texte[6] == "ACK":
                    if texte[len(texte)-1] == "length 0":
                        evenement_2 = 'Numéro accusé de réception : '+texte[8]+';'+' Taille de la fenêtre : '+texte[10]+';'
                        evenement_3 = ' Longueur du paquet : '+texte[len(texte)-1]+';'
                    if texte[len(texte)-1] != "length 0":
                        evenement_2 = 'Numero de séquence :'+texte[8]+';'+'Numéro accusé de réception : '+texte[10]+';'
                        evenement_3 = ' Longueur du paquet : '+texte[len(texte)-1]+';'
                        
                if texte[6] == "SYN ACK":
                    evenement_2 = 'Numéro de séquence : '+texte[8]+';'+' Numéro accusé de réception : '+texte[10]+';'
                    evenement_3 = ' Longueur du paquet : '+texte[len(texte)-1]+';'
                if texte[6] == "PUSH ACK":
                    evenement_2 = 'Numéro de séquence : '+texte[8]+';'+' Numéro accusé de réception : '+texte[10]+';'
                    evenement_3 = ' Longueur du paquet : '+texte[len(texte)-1]+';'
                if texte[6] == "FIN ACK":
                    evenement_2 = 'Numero de séquence :'+texte[8]+';'+'Numéro accusé de réception : '+texte[10]+';'
                    evenement_3 = ' Longueur du paquet : '+texte[len(texte)-1]+';'
            if texte[5] == 'ICMP':
                evenement='temps : '+texte[0]+';'+' Adresse Ip source : '+texte[2]+';'+' Adresse IP destinataire : '+texte[4]+';'+' Protocole : '+texte[5]+';'+'Status :'+texte[6]+';'+'State :'+texte[7]+';'+'Id :'+texte[9]+';'
            
            with open('fichier.csv','a') as f:
                f.write(f"{evenement},{evenement_2},{evenement_3}\n")
    f.close()
    fh.close()
    print('reussit')
    
