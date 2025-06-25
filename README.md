
# Appariement-aléatoire

---

**Présentation**

L'enjeu de ce projet a été d'aborder le problème d’appariement aléatoire bipartite (en anglais *Random Euclidean Bipartite Matching Problem*).

Soit $d \geq 1$ et considérons $2n \geq 1$ variables aléatoires iid :  
$(X_i)_{i=1}^{n}, (Y_i)_{i=1}^{n}$  
telles que $P(X_i \in A) = \|A\|$ pour tout $A \subseteq [0,1]^d$,  
avec $\|A\|$ désignant la mesure de Lebesgue (d-dimensionnelle) de $A$.

Le principe du problème d’appariement bipartite est de chercher une correspondance entre les $X_i$ et les $Y_i$ de manière à **minimiser la somme** des distances entre les paires associées.  
Ce problème peut aussi être généralisé en considérant une **puissance $p$** de cette distance.

Formellement, soit $\mathbb{S}_n$ l'ensemble des permutations de $\{1, ..., n\}$, et $\| \cdot \|$ la norme euclidienne :

$$
\|x\| = \sqrt{\sum_{k=1}^d x_k^2}
$$

Soit $p \in ]0,+\infty[$. Le problème s’énonce alors :

$$
B_{p,n} = \min_{\sigma \in \mathbb{S}_n} \sum_{i=1}^n \|X_i - Y_{\sigma(i)}\|^p
$$

Ce projet a été réalisé en binôme par Clément COURNIL--RABEUX et Hugo TAILE MANIKOM, sous la supervision de Monsieur Cyril LETROUIT.

---

**Les tâches accomplies**

Nous nous sommes appuyés sur le cours de Dario Trevisan intitulé *Notes on Random Euclidean Bipartite Matching Problems*.

Nous avons d’abord lu et compris le polycopié (lemmes, théorèmes, démonstrations…). Ensuite, nous avons étudié le problème de manière empirique, vulgarisé son contenu et envisagé quelques applications afin d’en approfondir notre compréhension avant l’étude formelle.

La première tâche confiée par Monsieur Letrouit a été de réaliser de nombreuses simulations en faisant varier différents paramètres.  
Nous avons utilisé plusieurs types d’algorithmes et comparé leurs complexités respectives. Les comportements observés dans les résultats ont pu être justifiés à l’aide de lemmes que nous avons ensuite démontrés.

Clément s’est concentré sur la partie informatique (simulations), tandis qu’Hugo a approfondi les aspects mathématiques du problème.

---

**Le travail**

### Rapport Hugo





### Rapport Clément

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
