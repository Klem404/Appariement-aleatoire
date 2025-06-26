
# Appariement-aléatoire

---

**Présentation**

L'enjeu de ce projet a été d'aborder le problème d’appariement aléatoire bipartite (en anglais *Random Euclidean Bipartite Matching Problem*).

Soit $d \geq 1$ et considérons $2n \geq 1$ variables aléatoires iid :  
$(X\_i)\_{i=1}^{n}, (Y\_i)\_{i=1}^{n}$  
telles que $P(X\_i \in A) = \|A\|$ pour tout $A \subseteq [0,1]^d$,  
avec $\|A\|$ désignant la mesure de Lebesgue (d-dimensionnelle) de $A$.

Le principe du problème d’appariement bipartite est de chercher une correspondance entre les $X\_i$ et les $Y\_i$ de manière à **minimiser la somme** des distances entre les paires associées.  
Ce problème peut aussi être généralisé en considérant une **puissance $p$** de cette distance.

Formellement, soit $\mathbb{S}\_n$ l'ensemble des permutations de {1, ..., n}, et $\| \cdot \|$ la norme euclidienne :

$\left \| x \right \| = \sqrt{\sum\_{k=1}^d x\_k^2}$


Soit $p \in ]0,+\infty[$. Le problème s’énonce alors :

$
B\_{p,n} = min\_{\sigma \in \mathbb{S}\_n} \sum\_{i=1}^n \left \|X\_i - Y\_{\sigma(i)}\right \| ^p
$

Ce projet a été réalisé en binôme par Clément COURNIL--RABEUX et Hugo TAILE MANIKOM, sous la supervision de Monsieur Cyril LETROUIT.

---

**Les tâches accomplies**

Nous nous sommes appuyés sur le cours de Dario Trevisan intitulé *Notes on Random Euclidean Bipartite Matching Problems*.

Nous avons d’abord lu et compris le polycopié (lemmes, théorèmes, démonstrations…). Ensuite, nous avons étudié le problème de manière empirique, vulgarisé son contenu et envisagé quelques applications afin d’en approfondir notre compréhension avant l’étude formelle.

La première tâche confiée par Monsieur Letrouit a été de réaliser de nombreuses simulations en faisant varier différents paramètres.  
Nous avons utilisé plusieurs types d’algorithmes et comparé leurs complexités respectives. Les comportements observés dans les résultats ont pu être justifiés à l’aide de lemmes que nous avons ensuite démontrés.

---

**Le travail**

### Partie Mathématiques

La partie maths compte le résultat de la résolution du problème, en dmension d=1, puis en dimension quelconque, ainsi que de deux lemmes.

#### Résolution du problème

d'un point de vue heuristique, on sait que les $(X\_ i)$ et les $(Y\_j)$ sont uniformément distribués sur $[0.1]^d$ il serait naturel de penser à une configuration telle que pour chaque $X\_i$ on puisse lui trouver un $Y\_j$ à une distance d'approximativement $1/n^{1/d}$. La conjecture immédiate est donc la suivante:

$B\_{p,n}\underset{n\to \infty}{\sim}n.\frac{1}{n^{p/d}} = n^{1-p/d}$

#### Cas d=1
[...]

#### Deux lemmes utiles

Lors des simulations, on remarquera divers comportement des courbes représentatives des résultats qui seront justifiés par les lemmes suivants:

$\textbf{Lemme1.}$ Soit $\lambda> 0$ et $X=(X\_i)\_{i=1}^{N_x}$ un processus de $Poisson$ d'intensité $\lambda$ sur $[0.1]^d$. $\forall U \subseteq [0,1]^d$ un Borelien avec $\left \| U \right\|>0$, la variable aléatoire

$n(X;U)=Card(\mathcal{I}(X;U))$

suit une loi de $Poission$ de paramètre $\lambda\left \| U \right\|$ et, conitionnellement à l'évènement {$n(X;U)=k$} les $k$ variables aléatoires $(X\_i)_{i\in \mathcal{I} (X;U)}$ sont $iid$ sur $U$ (i.e., de densité $\frac{1}{\left \| U \right\|}$ sur $U$).

[...]

Afin de démontrer le prochain lemme, on va utiliser le résultat suivant: 

$\textbf{Resultat.}$ Pour tout intervalle ouvert $]a,b[ \subseteq \mathbb{R}$, l'union $U\_{m=1}^{+\infty}]ma;mb[$ contient la demi-droite ]A,+\infty[ pour A > 0.

Il suffit de remarquer que $\]ma,mb\[ \cap \](m+1)a, (m+1)b\[\neq \emptyset$ pour $mb\geq (m+1)a$ ce qui est vrai pour $m\geq a/b-a$.

$\textbf{Lemme2.}$ Soit $\alpha>0, c\geq 0, f:[1,+\infty[\to [0,+\infty[$ continues telles que $\forall m \geq 1$ entier, $\lambda \geq 1$ réel,

$f(m\lambda)\leq f(\lambda)+c\lambda^{-\alpha}$

alors $\underset{n\to +\infty}{lim}f(\lambda)$ existe.

$\textbf{Preuve.}$ L'idée de la preuve est de commencer par borner $f(m\lambda$) sur $[1,2]$ grâce à l'expression de l'hypothèse, et par continuité. On utilsie ensuite le résultat précédent pour borner $f$ sur $\[ 1,+\infty\[$.

Il reste à montrer que $\underset{\lambda\to +\infty}{lim sup} f(\lambda)\leq \underset{\lambda\to +\infty}{lim inf} f(\lambda)$. 

Pour cela, on va poser un epsilon bien choisi afin de majorer $f(x)$ par $\underset{\lambda\to +\infty}{lim inf} f(\lambda)$ grâce à la continuité de $f$ ainsi que grâce au résultat établi précédemment.

Finalement comme on obtient une majoration vrai pour tout $x \in ]A,+\infty[$, avec A>0, en particulier on a l'inégalité qu'on voulait démontrer

### Partie Informatique

---

## 1. Algorithmes

---

J’ai d’abord implémenté plusieurs algorithmes heuristiques simples et les ai comparés avec les vraies solutions obtenues par **programmation linéaire**. 
Ensuite, j'ai regardé des algorithmes plus complexes comme le **sinkhorn** ou encore **l'algorithme hongrois**. 
Enfin, j'ai pris le "meilleur" algorithme, pour finalement lancer les simulations sur de grands nombres de points

###  1.1 Programmation linéaire (solution exacte)

Pour obtenir une solution optimale, nous avons formulé le problème d’appariement bipartite comme un problème d’optimisation linéaire sur une matrice de permutation.

#### 🔸 Encodage du problème

Le problème peut s’écrire :

$$
\min_{\pi \in \{0,1\}^{n \times n}} \sum_{i=1}^n \sum_{j=1}^n C_{ij} \pi_{ij}
$$

avec les contraintes suivantes :

$$
\sum_{j=1}^n \pi_{ij} = 1 \quad \forall i = 1,\dots,n \\
\sum_{i=1}^n \pi_{ij} = 1 \quad \forall j = 1,\dots,n
$$

où $C_{ij} = \| x_i - y_j \|^p$ est le coût pour associer le point bleu $x_i$ au point rouge $y_j$,  
et $\pi_{ij} \in \{0,1\}$ est une variable binaire indiquant si l’appariement est sélectionné.

Cette solution est utilisée comme **référence optimale** pour comparer les heuristiques simples, car elle est simple à encoder, et trouve la solution optimale .

---

###  1.2 Heuristiques simples

Nous avons ensuite implémenté trois algorithmes heuristiques classiques, afin de comparer leur efficacité à celle de la programmation linéaire.

#### 🔹 Greedy

- Associe à chaque étape la paire $(i,j)$ de coût minimal, en évitant les doublons.
- Complexité : $\mathcal{O}(n^2)$.

#### 🔹 Nearest Neighbour

- Pour chaque point bleu $x_i$, on choisit le point rouge $y_j$ le plus proche (non encore pris) :

$$
j = \arg\min_{j'} \| x_i - y_{j'} \|
$$

- Complexité : $\mathcal{O}(n^2)$.

#### 🔹 2-Improvement (2-opt)

- À partir d’un matching initial, on teste localement si on peut améliorer la solution en échangeant deux appariements :

$$
\|x_i - y_j\|^p + \|x_k - y_l\|^p > \|x_i - y_l\|^p + \|x_k - y_j\|^p
$$

- Si c’est le cas, on effectue l’échange. Répété jusqu’à convergence.

---

###  1.3 Résultats comparatifs

Voici les résultats obtenus par les heuristiques comparées à la solution optimale donnée par la programmation linéaire :

![Comparaison des heuristiques](https://raw.githubusercontent.com/Klem404/images/97b668ddcd6965a9037142a1a671e4ff37dc6538/easy_heuristics.png)

### 1.4 Algorithmes plus complexes (et + efficaces ?)
