# Appariement-aleatoire
## Présentation
L'enjeu de ce projet a été d'aborder le problème d'appariment aléatoire bipartite (en anglais Random Euclidian Bipartite Matching Problem).

Soit $d \geq 1$ et considérons $2n \geq 1$ iid variables aléatoires.
$(X_i)_{i=1}^{n}$ ***Quand j'écris les Yi, le code est recopié dans la preview au lieu d'étre affiché comme une formule mathématique***
telles que $P(X_i \in A) = |A| pour tout $A \subseteq [0,1]^d$
Avec $|A|$ désigant la mesure de Lebesque (d-dimensionnelle) de A.

Le principe du problème d'appariment aléatoire bipartite est de chercher les connexions (ou les matching) entre les $X_i$ et les $Y_i$ telle que la somme des différents points connectés soit minimale. On a même une généralisation, dans laquelle on se penche plutôt sur une puissance de cette distance.

Formellement, on prend $\mathbb{S}_n$ l'ensemble des permutations de ${1,...,n}$, et $|.|$ la norme euclidienne:
$|x| = sqrt{\sum_{k=1}^d x_k^2}$
