Alors, petit tuto pour tester le convertisseur ! Fait chauffer la ligne de commande :P

# Résumé pour les connaisseurs

des détails pour néophytes sont donnés dans les points suivants, n'hésites pas à passer celui là !

le module utilisé (note la branche !) : https://github.com/nvuaille/music21/tree/Noteworthy

Le code minimal qui va bien:
```python
from music21 import converter
score = converter.parse("GoodOldScore.nwc")
score.write(fmt="musicxml", fp=new_file)
```
un script de conversion (pour le fun): https://raw.githubusercontent.com/krapolyon/partoches/main/nwc2musicxml.py. Usage :
```
nwc2musicxml sources dest
```
- `sources` une regex/repertoire/fichier (passé à glob.glob pour obtenir une liste )
- `dest` un dossier de destination (existant)

Fonctionne avec python 3.6 ou plus. Pour les autres dépendances, voir la doc de music21.

# Détails pour les moins connaisseurs

## Environnement
Le plus simple pour avoir l'environnement qui va bien, c'est encore d'installer le module music21 de base en suivant ces instructions (avec des vrais morceaux d'anglais dedans): http://web.mit.edu/music21/doc/usersGuide/usersGuide_01_installing.html

Cette version ne contient ni le petit script qui facilite l'usage ni (pour l'instant) les pléthores de modif que j'ai faite.

## Version spécifique
Pour avoir ma version, va sur cette page : https://github.com/nvuaille/music21/tree/Noteworthy.

Tu y trouveras un bouton `clone or Download` qui te permettras de récupérer un zip. Ou le git si tu te sens : ça peut te permettre de suivre plus facilement mes potentiels changements futurs ... (voir le tuto git plus bas)

## Script QVB

Tu peux le télécharger ici : https://raw.githubusercontent.com/krapolyon/partoches/main/nwc2musicxml.py 

Il va falloir que python trouve ma version de music21. Pour ça, un moyen est de faire:

`export PYTHONPATH=/chemin/complet/vers/music21`

ensuite, dans LE MÊME terminal:

`python chemin/vers/nwc2musicxml.py fichier-a-charger DOSSIER-destination`

par exemple:

`python ~/Documents/nico/NWCConverter/musicxml/nwc2musicxml.py "/home/nico/Documents/nico/NWCConverter/nwc/*.nwc" .`

on notera l'étoile qui veut dire n'importe quels caractères (on cherche ici tous les fichiers nwc du dossier) et le `.` qui veut dire `ici`.


# Tuto Git

git (https://git-scm.com/) c'est un gestionnaire de version, c'est la base quand on code des trucs. Utiliser git au lieu de télécharger un zip permet de mieux suivre les différentes versions. C'est donc conseillé si tu souhaites suivre au plus proches les évolutions du projet, mais pas nécessaire pour être utilisateur.

## Récupérer un projet

C'est la commande `clone`:

` git clone https://github.com/nvuaille/music21`

ça crée un dossier 'music21' avec tout le projet dedans (donc tous les fichiers avec tout l'historique). La beauté du truc c'est que l'historique est caché, donc quand tu navigue là dedans tu vois que la version courante (= dernier commit de la branche courante). Cela dit, la version par défaut n'est pas ma branche.

## Changer de branche (= de version)

Va dans le dossier music21 ainsi crée et entre:

`git switch Noteworthy`

pour passer sur ma branche (quand on dit qu'on est sur une branche, par défaut on sous entend qu'on est sur le commit le plus récent de cette branche)

## Mettre à jour

Dans le dossier suivi par git:

`git pull`

Attention, ne fonctionne pas si tu as modifié manuellement des fichiers ! (sans le dire à git) Ni si j'ai mis à jour suite à une évolution du projet de base...

Version *brute* (écrase tout changement local)
`git fetch origin`
`git reset --hard origin/Noteworthy`

