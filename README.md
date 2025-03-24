# PRED
Les éléves qui ont effectué ce PREDS sont:
Marwa Tabib et Colin Trève

Les tests de performance des modèles se trouvent dans `openpom/examples`.

- **Nettoyage et création de variantes du jeu de données** :
  - Géré par le notebook **`clean_dataset`**.

- **Évaluation des performances sur plusieurs dimensions** :
  - Réalisée dans le notebook **`eval_accross_dim`**, qui teste différentes dimensions ainsi que deux fonctions de **READOUT**.
  - Les autres tests sont également inclus dans ce notebook.

- **Présentation et rapport du projet** :
  - Disponibles dans la section **`rendu`**.

## Données utilisées  

Les modèles de prédiction des descripteurs d’odeurs utilisent des données issues du fichier suivant :

```bash
openpom/openpom/examples/Fichiers-Sources/OdorCAS.csv
```

Ce fichier contient **3 841 molécules distinctes** identifiées par leur code CAS.

### Préparation des données  

À partir de ce fichier, plusieurs sous-ensembles de données sont extraits et enregistrés dans : 

```bash
openpom/examples/
```

1. **Conversion des codes CAS en SMILES**
   - Les codes CAS sont convertis en codes **SMILES.
   - La correspondance entre CAS et SMILES est enregistrée dans le fichier :
```bash
     CAS_Smiles_Pubchem.json
```

2. **Filtrage des descripteurs d’odeurs**
   - Seuls les descripteurs d’odeurs apparaissant **au moins 30 fois** sont conservés.
   - Ce filtrage permet d’assurer la présence de chaque descripteur dans les ensembles d’entraînement et de test.
   - Le jeu de données ainsi obtenu est enregistré dans
```bash
     Mol_odeur.csv
```

3. **Suppression des doublons**
   - Les codes SMILES dupliqués sont supprimés.
   - Le fichier résultant est :
```bash
     Mol_odeur_sans_doublons.csv
```

4. **Élimination des molécules sans descripteurs d’odeurs**
   - Après suppression des descripteurs apparaissant moins de 30 fois, certaines molécules ne possèdent plus aucun descripteur.
   - Ces molécules sont retirées, générant un nouveau dataset :
```bash
     Mol_odeur_sans_zeros.csv
```

5. **Création de labels individuels avec hiérarchie des odeurs**
   - La hiérarchie des odeurs est basée sur [Sketchoscent](https://oniris-polytech.univ-nantes.io/sketchoscent/index.sos.html).
   - Seuls les **descripteurs individuels** sont conservés.
   - Deux versions du dataset sont créées :
     - **Avec toutes les molécules** :
```bash
       Individual_label.csv
```
     - **Sans les molécules sans descripteurs d’odeurs** :
```bash
       Individual_label_wtho_zeros.csv
```







## Fichiers Test
Les diagrammes des résultats des modèls sont présent dans
```bash
openpom/examples/precision
```


## Mise en place de l'environnement  

Pour configurer l'environnement d'exécution des modèles, suivez les instructions décrites dans le dépôt suivant :  
[https://github.com/BioMachineLearning/openpom](https://github.com/BioMachineLearning/openpom)  

### 1. Cloner le dépôt et entrer dans le répertoire  

```bash
git clone https://github.com/marwatabib/PRED
cd PRED
```

### 2. Créer et activer un environnement Conda  

```bash
conda create -n open_pom python=3.9
conda activate open_pom
```

### 3. Installer les bibliothèques nécessaires  

```bash
pip install .
python setup.py develop
pip install dgl==1.1.1 -f https://data.dgl.ai/wheels/cu117/repo.html
```

### 4. Installer Jupyter  

```bash
conda install jupyter
```





