# Fichier Source obtenue après extraction de tgsc et fichier source issu de l'équipe Flaveur

### Description du dossier

- [*graphe.ttl*](./graph_odor.ttl) : Fichier au format rdf donnant l'ensemble des odeurs, de leur traduction, de leur(s) parent(s), et de leur synonyme qui seront utilisées par la suite dans l'outil
- [*croisement_sos_tgsc.csv*](./croisement_sos_tgsc.csv) : Fichier contenant deux colonnes, tgsc et ttl. **tgsc** contient les odeurs auxquelles on doit prêter attention lors de l'extraction des odeurs dans tgsc. **ttl**, s'il est vide alors l'odeur dans tgsc doit être ignoré sinon l'odeur dans tgsc fait référence à l'odeur indiqué qui se trouve dans [graph_odor.ttl](./graph_odor.ttl)
- [*ProduitsCAS.csv*](./ProduitsCAS.zip) (à extraire mais très lourd ~+100Mo) : matrice entre produit et molécule utilisée par les scripts python
- [*OdorCAS.csv*](./OdorCAS.csv) : matrice entre odeur et molécule utilisée par les scripts python
- [*textSOS.csv*](./textSOS.csv) : Ensemble des textes de l'outil ( attention le séparateur est un $ )