
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

#### Algorithmes

J’ai d’abord implémenté plusieurs algorithmes heuristiques simples et les ai comparés avec les vraies solutions obtenues par **programmation linéaire**.

##### Formulation du problème de matching

Le problème d’appariement bipartite s’écrit comme un problème d’optimisation combinatoire sur une matrice de permutation :

$$
\min_{\pi \in \{0,1\}^{n \times n}} \sum_{i=1}^n \sum_{j=1}^n C_{ij} \pi_{ij}
$$

Sous contraintes :

$$
\sum_{j=1}^n \pi_{ij} = 1 \quad \forall i = 1,\dots,n
$$

$$
\sum_{i=1}^n \pi_{ij} = 1 \quad \forall j = 1,\dots,n
$$

où $C_{ij}$ représente le coût $\| x_i - y_j \|^p$ pour associer le point bleu $i$ au point rouge $j$, et $\pi_{ij} \in \{0,1\}$ indique si l’appariement est sélectionné.

##### Heuristiques simples utilisées

Les trois heuristiques simples utilisées sont **Greedy**, **Nearest Neighbour**, et **2-Improvement** :

- **Greedy** :  
  Associe itérativement les paires de points (bleu, rouge) de coût minimal, sans réutilisation de points.

  - À chaque étape, on choisit la paire $(i,j)$ non encore utilisée minimisant $C_{ij}$.
  - Complexité : $\mathcal{O}(n^2)$.

- **Nearest Neighbour** :  
  Pour chaque point bleu $i$, on choisit le point rouge $j$ le plus proche (non encore pris) :

  $$
  j = \arg\min_{j'} \| x_i - y_{j'} \|
  $$

  - Chaque point est traité dans l’ordre.
  - Complexité : $\mathcal{O}(n^2)$.

- **2-Improvement (2-opt)** :  
  À partir d’un matching initial, on cherche à améliorer localement la solution :

  - Parcours des paires $(i,j)$ et $(k,l)$.
  - Test si échanger les correspondances ($i \leftrightarrow l$, $k \leftrightarrow j$) réduit le coût total :

  $$
  \|x_i - y_j\|^p + \|x_k - y_l\|^p > \|x_i - y_l\|^p + \|x_k - y_j\|^p
  $$

  - Si oui, on effectue l’échange. Répété jusqu’à convergence.

---

**Résultats obtenus :**

![Comparaison des heuristiques](https://raw.githubusercontent.com/Klem404/images/97b668ddcd6965a9037142a1a671e4ff37dc6538/easy_heuristics.png)
