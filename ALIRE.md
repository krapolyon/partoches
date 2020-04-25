Alors, petit tuto pour tester le convertisseur ! Fait chauffer la ligne de commande :P

# Déjà, il te faudra :

 - python en version 3.6 ou plus.

 - git

# Ensuite l'installation du bazar:

## Récupération du code

` git clone https://github.com/nvuaille/music21`

ça crée un dossier 'music21' avec tout le projet dedans (donc tous les fichiers avec tout l'historique). La beauté du truc c'est que l'historique est caché, donc quand tu navigue là dedans tu vois que la version courante (= dernier commit de la branche courante). Cela dit, la version par défaut n'est pas ma branche. Donc va dans le dossier music21 ainsi crée et entre:

`git checkout Noteworthy`

pour passer sur ma branche (quand on dit qu'on est sur une branche, par défaut on sous entend qu'on est sur le commit le plus récent de cette branche)

## Récupération du script

 - tu peux le télécharger ici : https://raw.githubusercontent.com/krapolyon/partoches/main/nwc2musicxml.py 

 - ou alors tu peux aussi faire `git clone https://github.com/krapolyon/partoches`(mais ça va aussi te prendre tout l'historique des partitions en musicxml)

# Utilisation

il va falloir que python trouve music21. Pour ça, un moyen est de faire:

`export PYTHONPATH=/chemin/complet/vers/music21`

ensuite, dans LE MÊME terminal:

`python chemin/vers/nwc2musicxml.py fichier-a-charger DOSSIER-destination`

par exemple:

`python ~/Documents/nico/NWCConverter/musicxml/nwc2musicxml.py "/home/nico/Documents/nico/NWCConverter/nwc/*.nwc" .`

on notera l'étoile qui veut dire n'importe quels caractères (on cherche ici tous les fichiers nwc du dossier) et le `.` qui veut dire `ici`


