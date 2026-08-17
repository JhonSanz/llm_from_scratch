**TEOREMA** Si $V$ es de dimensión finita, también lo es $T(V)$, y tenemos

$$dim N(T) + dim T(V) = dim V$$

Es importante recordar la definición de base y dimensión

> Un conjunto finito $S$ de elementos de un espacio lineal $V$ se llama base finita de $V$ si $S$ es independiente y genera $V$

> Si un espacio lineal $V$ tiene una base de $n$ elementos, el entero $n$ se llama dimensión de $V$. Escribimos $n = dimV$

y también debemos invocar este teorema

Sea $V$ un espacio lineal de dimensión finita con $\dim V = n$. Se tiene:

- Cualquier conjunto de elementos independiente de $V$ es un subconjunto de una cierta base para $V$.

- Cualquier conjunto de $n$ elementos independientes es una base para $V$.

[demostración de este teorema aqui](../04_espacios_lineales/demostracion17.md)

---


Para demostrar esto consideremos los siguientes elementos

- la dimensión $n = dimV$
- una base para $N(T)$ así: $\quad e_1, e_2, \dots, e_k$ donde $k = dim N(T) \leq n$

Segun el teormea anterior esos elementos $\quad e_1, e_2, \dots, e_k \quad$ **forman parte** de una cierta base de $V$:

$$e_1, e_2, \dots, e_k, e_{k+1}, \dots, e_{k+r}$$

ya que la base de $N(T)$ es un subconjunto de $V$ por la propia definición del núcleo, y a su vez al ser base es linealmente independiente

Veamos en esa base que $k+r=n$ ya que esa al ser una cierta base de $V$ su dimensión es exactamente $n$, y al mismo tiempo podemos decir que "a $k$ le faltan $r$ elementos para llegar a $n$", es decir, agregamos $r$ elementos a la base del núcleo de $k$ elementos

Entonces necesitamos demostrar que esos $r$ elementos forman una base de $T(V)$ y a su vez de mostrar que $dim T(V) = r$

Osea que, para que esos $r$ elementos sean base tienen que generar $T(V)$. Para comprobar esto tomemos un elemento $\quad y \in T(V) \quad$ este a su vez se puede escribir como $\quad y = T(x) \quad$ para un cierto $x$ particular de $V$

Ahora escribamos ese elemento $\quad x = c_1e_1 + \dots + c_{k+r}e_{k+r} \quad$ ya que estos elementos al ser una base podemos construir cualquier elemento de espacio mediante una combinación lineal

Y a su vez podemos reescribir esto así

$$y = T(x) = \sum_{i=1}^{k+r} c_iT(e_i) = \sum_{i=1}^{k} c_iT(e_i) \sum_{i=k+1}^{k+r} c_iT(e_i) $$

observemos que en $\sum_{i=1}^{k} c_iT(e_i) = O$  ya que esos son los elementos del núcleo! entonces nos queda solamente 

$$y = T(x) = \sum_{i=k+1}^{k+r} c_iT(e_i)$$

Como cualquier $y \in T(V)$ se expresa como combinación lineal de los $r$ elementos de (2.3), concluimos que estos generan $T(V)$

Perfecto, ahora falta demostrar que esos elenmentos son independientes. Supongamos que existen escalares  $\quad x = c_{k+1} + \dots + c_{k+r} \quad$ tales que

$$\sum_{i=k+1}^{k+r} c_iT(e_i) = O$$

Y por la linealidad de $T$ podemos escribir

$$T (\sum_{i=k+1}^{k+r} c_ie_i) = O$$

si hacemos eso, vemos que los elementos están en el núcleo, ya que la transformación llevó los elementos a la imagen en $O$


lo que significa que el elemento $x = c_{k+1}e_{k+1} + \dots + c_{k+r}e_{k+r}$ pertenece al núcleo $N(T)$, ya que $T(x) = O$.

Ahora bien, como $e_1, \dots, e_k$ es una **base de $N(T)$**, todo elemento del núcleo se puede escribir con ellos, entonces existen escalares $c_1, \dots, c_k$ tales que

$$x = c_1e_1 + \dots + c_ke_k$$

Pero también teníamos que $x = c_{k+1}e_{k+1} + \dots + c_{k+r}e_{k+r}$, es decir en este momento tenemos dos expresiones para $x$, entonces igualando ambas expresiones y restando obtenemos

$$c_1e_1 + \dots + c_ke_k - c_{k+1}e_{k+1} - \dots - c_{k+r}e_{k+r} = O$$

Como $e_1, \dots, e_{k+r}$ es una **base de $V$**, es linealmente independiente, por lo tanto la única forma de que esa combinación lineal sea igual a $O$ es que todos los escalares sean cero:

$$c_1 = \dots = c_k = 0 \quad \text{y} \quad c_{k+1} = \dots = c_{k+r} = 0$$

En particular $c_{k+1} = \dots = c_{k+r} = 0$, lo que demuestra que los elementos $T(e_{k+1}), \dots, T(e_{k+r})$ son **linealmente independientes**. $\blacksquare$