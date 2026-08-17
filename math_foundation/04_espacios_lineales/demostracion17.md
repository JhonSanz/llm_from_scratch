Sea $V$ un espacio lineal de dimensión finita con $\dim V = n$. Se tiene:

- Cualquier conjunto de elementos independiente de $V$ es un subconjunto de una cierta base para $V$.

- Cualquier conjunto de $n$ elementos independientes es una base para $V$.

## Parte a)

Consideremos el **conjunto independiente** constituído por elementos de $V$

$$S = \lbrace x_1, \dots, x_k \rbrace$$

recordando que la envolvente lineal de una base nos genera el espacio $V$... Entonces si $L(S) = V$ entonces $S$ es una base.

Si $L(S) \neq V$, entonces hay algún elemento $y$ en $V$, **que no está en** $L(S)$ (es decir, $y$ no puede escribirse como combinación lineal de los elementos de $S$). Así que vamos a agregarlo a nuestro conjunto $S$, generando un nuevo conjunto $S'$ **presuntamente dependiente** (ya que esto es lo que queremos refutar):

$$S' = \lbrace x_1, \dots, x_k, y \rbrace$$

Multipliquemos los elementos de ese conjunto por escalares $c_1, \dots, c_{k+1}$, siendo alguno diferente de cero (suposición de dependencia):

$$\left(\sum_{i=1}^{k} c_ix_i\right) + c_{k+1}y = O$$

Primero veamos que necesariamente $c_{k+1} \neq 0$: si fuera $c_{k+1} = 0$, tendríamos $\sum_{i=1}^{k} c_i x_i = O$ con algún $c_i \neq 0$, lo cual contradice que $S$ es independiente. Luego $c_{k+1} \neq 0$, y podemos despejar $y$:

$$y = -\frac{1}{c_{k+1}} \sum_{i=1}^{k} c_ix_i = \sum_{i=1}^{k} \left(-\frac{c_i}{c_{k+1}}\right) x_i$$

Pero esto dice que $y \in L(S)$, lo cual **contradice** la suposición de que $y \notin L(S)$. Por lo tanto $S'$ es linealmente independiente y contiene $k+1$ elementos.

Si $L(S') = V$ entonces $S'$ es una base, y como $S \subset S'$, la parte **a)** queda demostrada.

Si $L(S') \neq V$, repetimos el proceso agregando un nuevo elemento, obteniendo conjuntos independientes de $k+2, k+3, \dots$ elementos. Este proceso debe terminar en un número finito de pasos, pues ningún conjunto independiente en $V$ puede tener más de $n$ elementos. Cuando el proceso para, el conjunto obtenido es una base que contiene a $S$.

## Parte b)

Toda base de $V$ tiene exactamente $n$ elementos. Si $S$ es un conjunto independiente con $n$ elementos, por la parte **a)** existe una base $B$ tal que $S \subseteq B$. Como $B$ también tiene $n$ elementos, concluimos que $S = B$, es decir, $S$ es una base.

---

## Ejemplo: Extensión de un conjunto independiente a una base

Sea $V = \mathbb{R}^3$ (dimensión $n = 3$) y el conjunto independiente inicial $S = \{(1,0,0)\}$.

### Paso 1

$L(S) = \{(a,0,0)\}$ (eje $x$), luego $L(S) \neq V$. Se toma $y = (0,1,0) \notin L(S)$ y se forma:

$$S' = \{(1,0,0),\ (0,1,0)\} \quad \text{independiente, 2 elementos}$$

### Paso 2

$L(S') = \{(a,b,0)\}$ (plano $xy$), luego $L(S') \neq V$. Se toma $y' = (0,0,1) \notin L(S')$ y se forma:

$$S'' = \{(1,0,0),\ (0,1,0),\ (0,0,1)\} \quad \text{independiente, 3 elementos}$$

### Paso 3

$L(S'') = \mathbb{R}^3 = V$. El proceso para: $S''$ es una base.

### ¿Por qué no puede continuar?

Cualquier $y'' \in V$ ya pertenece a $L(S'') = V$, por lo que $S''' = S'' \cup \{y''\}$ sería dependiente. Ningún conjunto independiente en $\mathbb{R}^3$ puede tener más de $n = 3$ elementos.

### Resumen del proceso

$$\{(1,0,0)\} \xrightarrow{+(0,1,0)} \{(1,0,0),(0,1,0)\} \xrightarrow{+(0,0,1)} \underbrace{\{(1,0,0),(0,1,0),(0,0,1)\}}_{\text{base de } \mathbb{R}^3}$$