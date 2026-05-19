Sea $V$ un espacio lineal de dimensión finita con $\dim V = n$. Se tiene:

- Cualquier conjunto de elementos independiente de $V$ es un subconjunto de una cierta base para $V$.

- Cualquier conjunto de $n$ elementos independientes es una base para $V$.

veamos la primera parte:

Consideremos el **conjunto independiente** constituído por elementos de $V$

$$S = \lbrace x_1, \dots, x_n \rbrace$$

recordando que la envolvente lineal de una base nos genera el espacio $V$... Entonces si $L(S) = V$ entonces $S$ es una base.

Si $L(S) \neq V$, entonces hay algún elemento $y$ en $V$, **que no está en** $L(S)$ (de esa manera se garantiza no tomar objetos redundantes). Así que vamos a agregarlo a nuestro conjunto $S$, generando un nuevo conjunto $S'$ **presuntamente dependiente** (ya que esto es lo que queremos refutar), así:

$$S' = \lbrace x_1, \dots, x_n, y \rbrace$$

Multipliquemos los elementos de ese conjunto por escalares $c_1, \dots, c_{k+1}$

$$(\sum_{i=1}^{k} c_ix_i) + c_{k+1}y = O$$

siendo alguno de ellos diferente de cero (ya que estamos suponiendo en este momento que el conjunto es dependiente). Entonces despejemos $y$ así

$$y = - \frac{1}{c_{k+1}} \sum_{i=1}^{k} c_ix_i$$

con esto nos damos cuenta que $c_{k+1} \neq 0$ y además tiene sentido porque estamos bajo el supuesto de que el conjunto es dependiente, pero inicialmente era independiente osea que $c_1, \dots, c_i = 0$

Al realizar ese despeje vemos que podemos escribir $y$ como parte de la envolvente lineal

$$y = \sum_{i=1}^{k} ( - \frac{c_i}{c_{k+1}} ) x_i$$

osea que $y \in L(S)$, lo cual contradice la suposición que hicimos anteriormente. Es decir que el conjunto $S'$ es linealmente independiente y contiene $k+1$ elementos

Si $L(S') = V$ entonces $S'$ es una base y como $S$ es un subconjunto de $S'$ la parte **a.** queda demostrada

Si $S'$ no es una base podríamos realizar el mismo proceso de forma iterativa, agregando $k+2, k+3, \dots$ elementos, pero en un número finito de etapas y hasta $n$, ya que no podemos exceder la dimensión del espacio por el teorema de los $k+1$ elementos. Es decir, El Teorema 1.5 se aplica a $L(S)$, y cuando $L(S)=V$, el techo de $n$ elementos aplica a todo $V$. Por eso el proceso no puede continuar indefinidamente. 


La parte b del teorema se basa en que toda base de $V$ tiene el mismo número de elementos. 

Entonces, consideremos un conjunto independiente $S$ con $n$ elementos, en la parte anterior vimos que $S$ es un subconjunto de base $B$, entonces tiene exactamente $n$ elementos entonces $S=B$