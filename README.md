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
