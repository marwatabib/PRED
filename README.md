# PRED
Les éléves qui ont effectué ce PREDS sont:
Marwa Tabib et Colin Trève

Les tests sur les performances des modèles se situent dans openpom/examples.

Pour nettoyer le jeu de données et crée des variantes c'est le notebook clean_dataset qui est en charge

Pour les tests sur plusieurs dimensions et avec les deux fonctions de READOUT différent c'est le notebook eval_accross_dim

le reste des tests se situe dans ce dernier notebook

La présentation ainsi que le rapport du projet se trouve dans la partie rendu.

## Donnée
Les données utilisées proviennent

## Mise en place de l'environnement

Pour mettre en place l'environnement d'exécution des modèles il faut suivre ce qui est décrit sur le git suivant : https://github.com/BioMachineLearning/openpom 


il faut cloner le repository puis entrer dedans
```bash
git clone https://github.com/marwatabib/PRED
cd PRED
```

puis on crée un environnement et on l'active
``` bash
conda create -n open_pom python=3.9
conda activate open_pom
```

Pour installer les bibliotéque nécessaire il faut utilier les commande
```bash
pip install .
python setup.py develop
pip install dgl==1.1.1 -f https://data.dgl.ai/wheels/cu117/repo.html

```

suite à cela il faut installer jupyter
```bash
conda install jupyter
```





