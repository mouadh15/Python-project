Analyseur de Trames Wireshark

Ce projet Python permet d'analyser un fichier exporté depuis Wireshark au format .txt et de produire un fichier .csv contenant les informations essentielles classées, telles que les adresses IP source et destination, le protocole utilisé, les flags, les numéros de séquence, et plus encore.
Fonctionnalités: Extraction des trames depuis un fichier Wireshark au format .txt.


Classification des informations en colonnes :
        Temps
        Adresse IP source
        Adresse IP destination
        Protocole
        Flags
        Numéros de séquence et accusé de réception
        Taille de fenêtre et longueur du paquet
    Génération d'un fichier .csv structuré pour un traitement ultérieur ou une analyse.
    Visualisation des données avec un diagramme des occurrences d'adresses IP.
![image](https://github.com/user-attachments/assets/422ac32a-b9bb-47dd-86f7-f6bc7166520b)
Analyse des Défaillances ICMP

Le projet identifie également les anomalies dans le protocole ICMP (Internet Control Message Protocol). Les défaillances ICMP observées dans l’analyse montrent que 42% des erreurs proviennent de la machine BP-Linux8.ssh en tant qu'adresse IP source. Cela indique que ce dispositif est fortement impliqué dans les problèmes de connectivité réseau, ce qui pourrait être dû à une surcharge, une configuration incorrecte ou un problème matériel/logiciel. Ce type d’analyse permet d’identifier les points faibles du réseau pour une maintenance proactive.

![unknown(1)](https://github.com/user-attachments/assets/0b1a9740-0b2e-48f9-971e-5946e445e015)

