Ce TD, réalisé dans le cadre du cours GLCS de Génie logiciel pour le Calcul Scientifique, a pour objectif d’évaluer les performances de la programmation avec XcalableMP – une extension directive du langage permettant de développer aisément des programmes parallèles pour des systèmes à mémoire distribuée et d’optimiser leur performance grâce à une syntaxe minimale.

Pour cette expérience, nous avons comparé deux programmes : l’un combinant XMP et MPI, et l’autre utilisant OpenMP intégré à gcc. Ces deux programmes sont exécutés dans un environnement Docker, que l’on peut lancer depuis le répertoire courant avec la commande suivante :

```
docker compose up
```

L’image Docker déployée démarre un nœud principal (mpihead) ainsi que trois nœuds de calcul (mpinodes), et fournit également un environnement de compilation adapté à notre expérimentation. Il est toutefois à noter que cette image contient d’autres services qui devront être ajustés en fonction de vos besoins spécifiques.

Le fonctionnement des programmes est le suivant : un fichier en entrée, généré par « scamblegenerator », permet de créer une distribution de données, laquelle est ensuite utilisée pour générer un histogramme via Python (generation_image.py) à partir du fichier de sortie.

Dans le cadre de l’expérience réalisée dans l’environnement Docker, nous avons évalué la performance du programme combinant XMP et MPI ainsi que celle du programme OpenMP. Par ailleurs, une expérimentation complémentaire avec OpenMP a été effectuée en dehors de l’image Docker afin d’analyser l’impact de Docker sur nos résultats.

Voici nos résultats :

*joli graphique*

On constate que l’utilisation de Docker a un impact modéré sur les performances, tandis que la combinaison XMP et MPI influence significativement les résultats. Cependant, l’effet dissipatif potentiel lié à l’utilisation de Docker pour le programme XMP/MPI n’a pas été pris en compte, et pourrait constituer un point intéressant à approfondir ultérieurement.