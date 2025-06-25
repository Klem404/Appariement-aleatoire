# Appariement-aleatoire
## Présentation
L'enjeu de ce projet a été d'aborder le problème d'appariment aléatoire bipartite (en anglais Random Euclidian Bipartite Matching Problem).

Soit $d \geq 1$ et considérons $2n \geq 1$ iid variables aléatoires.

$(X\_i)\_{i=1}^{n} (Y\_i)\_{i=1}^{n}$

telles que $P(X\_i \in A) = \left\|A\right\|$ pour tout $A \subseteq [0,1]^d$
Avec $|A|$ désigant la mesure de Lebesque (d-dimensionnelle) de A.

Le principe du problème d'appariment aléatoire bipartite est de chercher les connexions (ou les matching) entre les $X_i$ et les $Y_i$ telle que la somme des différents points connectés soit minimale. On a même une généralisation, dans laquelle on se penche plutôt sur une puissance de cette distance.

Formellement, on prend $\mathbb{S}_n$ l'ensemble des permutations de ${1,...,n}$, et $\left\| .\right\|$ la norme euclidienne,

$\left\| x\right\| = \sqrt{\sum\_{k=1}^d x\_k^2}$

Soit $p\in ]0,+\infty[$ . Le problème s'énonce comme suit

$B_{p,n} = min \_{\sigma\in \mathbb{S\_n}}\sum\_{i=1}^n\left\|X\_i-Y\_ \sigma (i)\right\| ^p$

Ce projet a été réalisé en binôme par Clément COURNIL-RABEUX Hugo TAILE MANIKOM sous sous la supervision de Monsieur Cyril Letrouit.


## Les tâches accomplies

Pour ce travail, nous nous somme appuyés sur le cours de Dario Trevisan intitulé "Notes on Random Euclidian Bipartite Matching Matching Problems".

Nous avons commencé par une lecture/compréhension du polycopié, des lemmes, théorèmes, démonstrations,etc.

Après quoi, nous avons commencé à etudié le problème de manière empirique, vulgarisé le problème et abrodé quelques applications en vif, afin de mieux le comprendre avant de l'étudier de manière plus formelle.

La première tâche qui nous a été confié par monsieur Letrouit a été de faire de nombreuses simulations en faisant varier de nombreux paramètres de notre problème. Nous avons également utilisés plusieurs types d'algorithmes et comparés les différentes complexités. Les comprortements des différentes courbes se justifiaient par des lemes dont on a été par la suite chargés de démontrer.

Clément s'est plus concentré sur la partie informatique, les simulations, tandis qu'Hugo a plutôt mis l'accent sur la partie mathématique du problème.

## Le travail

### Rapport Hugo

### Rapport Clément

#### Algorithmes 

Tout d'abord, j'ai commencé à implémenter différents algorithmes heuristiques simples et des les comparer avec les vrais solutions, calculées via programmation linéaire, dont l'encodage du problème est le suivant : 
\section{Formulation du problème de matching}

Le problème de matching biparti peut s’écrire comme un problème d’optimisation combinatoire sur une matrice de permutation :

\[
\min_{\pi \in \{0,1\}^{n \times n}} \sum_{i=1}^n \sum_{j=1}^n C_{ij} \pi_{ij}
\]

sous contraintes :

\[
\sum_{j=1}^n \pi_{ij} = 1 \quad \forall i = 1,\dots,n, \qquad
\sum_{i=1}^n \pi_{ij} = 1 \quad \forall j = 1,\dots,n
\]

où \( C_{ij} \) représente le coût (souvent la distance \( \| x_i - y_j \|^p \)) pour associer le point bleu \( i \) au point rouge \( j \), et \( \pi_{ij} \in \{0,1\} \) indique si l'appariement est choisi.


[ explications des heuristiques simples ]
Nous avons eu ces résultats. [results]
Ensuite,nous avons regardé deux algorithmes + complexes, l'algorithme hongrois, et l'algorithme sinkhorn , [explications des deux algos et calcul des complexité (et celle de prog lin)]
et nous avons eu ces résultats :  [results ].

Enfin, pour s'intéresser aux asymptotiques et de voir comment le résultat varie selon d et n, nous avons fait des simulations via l'algo hongrois (non heuristique et donc + efficace que lin prog) : [résultats] [observations]
