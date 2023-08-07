Alors, petit tuto pour tester le convertisseur ! Fait chauffer la ligne de commande :P

# Prérequis
Tout passe par le module python [music21](https://web.mit.edu/music21/doc/usersGuide/usersGuide_01_installing.html).

Ce module permet de lire et d'écrire différents formats de fichiers. Le constat étant qu'il gère très mal Noteworthy.
J'ai fait des modifs pour améliorer ça, mais des problème subsistent.

**! Mes modifs ont été faites après la 9.1 !**
Tant qu'une nouvelle version n'a pas été publiée, faut utiliser la branche master du projet et non le paquet pip...

# Résumé d'utilisation
Des détails pour néophytes sont donnés dans les points suivants, n'ai pas peur !

Le code minimal qui va bien:
```python
from music21 import converter
score = converter.parse("GoodOldScore.nwc")
score.write(fmt="musicxml", fp=new_file)
```

Un script de conversion (pour le fun): <https://raw.githubusercontent.com/krapolyon/partoches/main/nwc2musicxml.py>. Usage :
```
python nwc2musicxml.py sources dest
```
- `sources` une regex/repertoire/fichier (passé à glob.glob pour obtenir une liste)
- `dest` un dossier de destination (existant)

Fonctionne avec python 3.10 ou plus. Pour les autres dépendances, voir la doc de music21.

# Détails
## Préparation de l'environnement
Le plus simple pour avoir l'environnement qui va bien, c'est encore d'installer le module music21 de base en suivant ces instructions (avec des vrais morceaux d'anglais dedans): <http://web.mit.edu/music21/doc/usersGuide/usersGuide_01_installing.html>

Typiquement, dans une console :
`> pip3 install –upgrade music21`

Si c'est une version après la 9.1, tout est installé, tu peux lancer le script ! (voir plus bas).

## Version spécifique
Si c'est la version 9.1 qui est installée, il faut récupérer du code en plus.
Va sur cette page : <https://github.com/cuthbertLab/music21>

Tu y trouveras un bouton `clone or Download` qui te permettras de récupérer un zip.

Il va falloir que python trouve cette version de music21. Pour ça, un moyen est
d'ouvrir une console et de faire:
```
export PYTHONPATH=/chemin/complet/vers/music21
```
*(sous windows, le format de chemin est de type C:\dossier\...)*

ensuite, dans LA MÊME console, lancer le script.

## Lancer le script
Tu peux le télécharger ici : <https://raw.githubusercontent.com/krapolyon/partoches/main/nwc2musicxml.py>

`python chemin/vers/nwc2musicxml.py fichier-a-charger dossier-destination`

par exemple:

`python /home/nico/Documents/nico/NWCConverter/musicxml/nwc2musicxml.py "/home/nico/Documents/nico/NWCConverter/nwc/*.nwc" .`

on notera l'étoile qui veut dire n'importe quels caractères (on cherche ici tous les fichiers nwc du dossier) et le `.` qui veut dire `ici`.
On obtient donc les musicxml à côté des nwc.

## Problèmes connus
La batterie est déclarée en 'Grand Piano'. Lors de l'import dans musescore, il faut simplement changer l'instru de cette portée.
