# Matrices

## Transformaciones lineales con valores asignados

Si $V$ es de dimensión finita, siempre podemos construir una transformación lineal $T: V \rightarrow W$ con valores asignados a los elementos base de $V$, como se explica en el teorema siguiente.

> **TEOREMA 2.12.** Sea $e_1, \dots, e_n$ una base para un espacio lineal $n$-dimensional $V$. Sean $u_1, \dots, u_n$, $n$ elementos arbitrarios de un espacio lineal $W$. Existe entonces una y sólo una transformación $T: V \rightarrow W$ tal que
> 
> $$(2.7) \quad T(e_k) = u_k \quad \text{para } k = 1, 2, \dots, n.$$

Esta transformación $T$ aplica un elemento cualquiera $x$ de $V$ del modo siguiente:

$$(2.8) \quad \text{Si } x = \sum_{k=1}^{n} x_k e_k, \text{ entonces } T(x) = \sum_{k=1}^{n} x_k u_k.$$

**Demostración.** Todo $x$ de $V$ puede expresarse en forma única como combinación lineal de $e_1, \dots, e_n$, siendo los multiplicadores $x_1, \dots, x_n$ los componentes de $x$ respecto a la base ordenada $(e_1, \dots, e_n)$. Si definimos $T$ mediante (2.8), conviene comprobar que $T$ es lineal. Si $x = e_k$ para un cierto $k$, entonces todos los componentes de $x$ son 0 excepto el $k$-ésimo, que es 1, con lo que (2.8) da $T(e_k) = u_k$, como queríamos.

Para demostrar que sólo existe una transformación lineal que satisface (2.7), sea $T'$ otra y calculemos $T'(x)$. Encontramos que

$$T'(x) = T' \left( \sum_{k=1}^{n} x_k e_k \right) = \sum_{k=1}^{n} x_k T'(e_k) = \sum_{k=1}^{n} x_k u_k = T(x).$$

Puesto que $T'(x) = T(x)$ para todo $x$ de $V$, tenemos $T' = T$, lo cual completa la demostración.



> Podría resumir todo esto con mis palabras así:
>
>Puedo asignarle valores arbitrarios del conjunto W a la aplicación de la transformación sobre los elementos de la base
>
>Y si un elemento x de V puede escribirse como una combinación lineal de los elementos de la base, la transformación de ese x se puede escribir como una como una combinación lineal de los valores asignados
>
**EJEMPLO 1** Definimos los valores en la base:

$$T(i)=2i \qquad T(j) = j$$
Eso es todo lo que necesitamos especificar. Para cualquier vector $x = x_1 i + x_2 j$:

$$T(x) = x_1 \cdot T(i) + x_2 \cdot T(j) = x_1(2i) + x_2(j) = (2x_1)i + (x_2)j$$

**EJEMPLO 2.** Determinar la transformación lineal $T: V_2 \rightarrow V_2$ que aplique los elementos base $i = (1, 0)$ y $j = (0, 1)$ del modo siguiente

$$T(i) = i + j, \quad T(j) = 2i - j.$$

**Solución.** Si $x = x_1 i + x_2 j$ es un elemento arbitrario de $V_2$, entonces $T(x)$ viene dado por

$$T(x) = x_1 T(i) + x_2 T(j) = x_1(i + j) + x_2(2i - j) = (x_1 + 2x_2)i + (x_1 - x_2)j.$$

## Representación matricial de las transformaciones lineales

Con el teorema de valores asignados pudimos ver que la transformación lineal $T: V \rightarrow W$ está determinada por su acción sobre un conjunto de elementos base $e_1, \dots, e_n$ mediante los valores asignados

Ahora supongamos que el espacio lineal $W$ es de dimensión finita y $dimW = m$ y tenemos una cierta base $w_1, \dots, w_m$ para $W$

> las dimensiones $n$ y $m$ pueden ser o no iguales

Como $T$ tiene los valores en $W$ podemos expresar los valores asignados de la siguiente manera 


$$T(e_k) = \sum_{i = 1}^{m} t_{ik}w_{i}$$


esto es una combinación lineal de los elementos de la base $w_1, \dots, w_m$  de $W$ con los escalares $t_{1k}, \dots, t_{mk}$

por ejemplo

$T(e_1) = t_{11}w_1 + t_{21}w_2 + \dots + t_{m1}w_m$

$T(e_2) = t_{12}w_1 + t_{22}w_2 + \dots + t_{m2}w_m$

cada uno de estos valores asignados se puede representar como un vector columna, de la siguiente manera:


ejemplo para $T(e_1)$

$$T(e_1) = \begin{pmatrix}
t_{11} \\
t_{21} \\
\vdots \\
t_{m1}
\end{pmatrix}$$

vemos que el primer subindice cambia, y es importante cuando escribimos todos los valores asignados $T(e_k)$ uno junto al otro

$$
\begin{pmatrix}
t_{11} & t_{12} & \cdots & t_{1n} \\
t_{21} & t_{22} & \cdots & t_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
t_{m1} & t_{m2} & \cdots & t_{mn}
\end{pmatrix}
$$

vemos que el primer subindice indica la fila y el segundo la columna. También vemos que en la diagonal los subíndices son iguales.

Por lo tanto esto es una matriz de $m \times n$, $m$ filas y $n$ columnas

También podemos hacer referencia a un elemento directo de la matriz así: $t_{ik}$

#### Ejemplo informal pero poderoso

Aun sin ver la definición formal podemos intuir que, como en el ejemplo anterior, podemos armar una matriz con **dos espacios lineales $V$ y $W$** y con los valores asignados que vimos anteriormente. Por lo tanto, podemos tomar cualquier tipo de elementos que cumplan las caracteristicas que nos piden

Ya sabemos que tanto vectores como polinomios de grado $\leq n$ son espacios lienales, entonces armemos una transformación lineal y una matriz 

$T: V \to W$ con $V = \mathbb{R^2}$ y $W = P_3$ Y tenemos que definir las bases para cada conjunto y los valores asignados para cada elemento de la base de $V$, entonces:

- Base de $V$: $\lbrace (1,0), (0,1) \rbrace$
- Base de $W$: $\lbrace 1,x,x^2,x^3 \rbrace$

Y ahora definimos los valores asignados, PERO OJO 👀, si vemos el teorema de mas arriba no nos exige ni siquiera saber la base de $V$, solo necesitamos escribir los valores asignados para cada elemento así:

- $T(e_1)$ = $1 + x$
- $T(e_2)$ = $x^2 + x^3$

observemos que los valores asignados están en términos de los elementos de $W$, y ahora podemos armar la matriz ya que:

- $T(e_1)$ = $1 + x$ = $1 \cdot 1 + 1x + 0x^2 + 0x^3 \quad$ es decir, estamos encotrando los coeficientes para cada elemento de la base de $W$ después de establecer los valores asignados.

- $T(e_2)$ = $x^2 + x^3$ = $0 \cdot 1 + 0x + 1x^2 + 1x^3$

osea

$$T(e_1) = \begin{pmatrix}
1 \\
1\\
0 \\
0
\end{pmatrix}$$

$$T(e_2) = \begin{pmatrix}
0 \\
0\\
1 \\
1
\end{pmatrix}$$

entonces ya podemos armar la matriz

$$
\begin{pmatrix}
1 & 0 \\
1 & 0 \\
0 & 1 \\
0 & 1
\end{pmatrix}
$$

ahora calculemos un elemento puntual usando la transformación, recordando lo que vimos anteriormente, cualquier elemento de $V$ se puede escribir como $x = x_1e_1 + x_2e_2$, y por la linealidad terminaremos aplicando los valores asignados, entonces:

$$T((3,2)) = 3T(e_1) + 2T(e_2)$$
$$T((3,2)) = 3(1 + x) + 2(x^2 + x^3)$$

donde

$$T((3,2)) = 3 + 3x + 2x^2 + 2x^3$$

Lo cual nos da como resultado un polinomio de grado 3, pero eso no es lo mas sorprendente. Simplemente pudimos haber usado la matriz para calcular esto así:

```math
\begin{pmatrix} 1 & 0 \\ 1 & 0 \\ 0 & 1 \\ 0 & 1 \end{pmatrix}
\begin{pmatrix} 3 \\ 2 \end{pmatrix}
=
\begin{pmatrix} 3 \\ 3 \\ 2 \\ 2 \end{pmatrix}
```

Se que en este punto no conocemos el producto de matrices, pero veamos que esa operacion equivale al polinomio $3 + 3x + 2x^2 + 2x^3$

#### Sutilezas 

Antes de la definición formal podemos encontrar varios puntos sutiles

Como vimos anteriormente para armar la matriz introdujimos los valores asignados de $V$ como una combinación lineal de los valores de W, pero estos **no aparecen por ningún lado en la matriz resultante**. Y esto lo podemos interpretar de la siguiente manera 

recordando la forma en que se escriben los vectores, siempre hay una base canónica "por debajo", así:

$$3(1,0,0) + 2(0,1,0) + 4(0,0,1) = (3,2,4)$$

Pero podemos simplemente escribir el vector $(3,2,4)$ y obviar la base...

Lo mismo pasa con las matrices, solo vamos a encontrar los coeficientes en la matriz, pero debajo está la base. Y esto es muy importante porque la base es la que nos da el "orden" de como van a aparecer los elementos en la matriz. No es igual formarla tomando los valores asignados primero por el último elemento de la base de $V$ que por el primero.


También vale la pena resaltar que en el ejemplo anterior solamente puede exitir una transformación que actúe sobre los valores asignados de esta manera 

- $T(e_1)$ = $1 + x$
- $T(e_2)$ = $x^2 + x^3$

tal y como lo menciona el teorema de valores asignados.

---


"Así pues, toda transformación lineal $T$ de un espacio $n$-dimensional $V$ 
en un espacio $m$-dimensional $W$ da origen a una matriz $m \times n$ 
$(t_{ik})$ cuyas columnas son los componentes de $T(e_1), \ldots, T(e_n)$ 
relativos a la base $(w_1, \ldots, w_m)$. La llamamos **representación 
matricial** de $T$ relativa a unas bases ordenadas $(e_1, \ldots, e_n)$ de $V$ 
y $(w_1, \ldots, w_m)$ para $W$. 

Una vez conocida la matriz $(t_{ik})$, los 
componentes de un elemento cualquiera $T(x)$ con relación a la base 
$(w_1, \ldots, w_m)$ pueden determinarse como se explica en el teorema 
que sigue." - Cálculo Tom M. Apostol Vol 2 pag. 57


![alt text](img/matrix_t1.png)

---

Ahora bien, el recíproco también es cierto. Podemos partir desde una disposición de $mn$ escalares que formen una matriz rectangular $t_{ik}$ y elegimos un par de bases ordenadas para $V$ y $W$ existe una transformación lineal que tiene esa representación matricial.

#### Por ejemplo

Construcción de una transformación lineal a partir de una matriz dada. Supongamos que disponemos de la matriz $2 \times 3$

```math
\begin{pmatrix} 3 & 1 & -2 \\ 1 & 0 & 4 \end{pmatrix}
```

Elijamos las bases usuales de vectores coordenados unitarios para $V_2$ y $V_3$. Entonces la matriz dada representa una transformación lineal $T: V_3 \to V_2$. que aplica un vector cualquiera $(x_1, x_2, x_3)$ de $V_3$ en el vector $(y_1, y_2)$ de $V_2$ de acuerdo con
las ecuaciones lineales:

$$y_1 = 3x_1 + x_2 - 2x_3$$

$$y_2 = x_1 + 0x_2 + 4x_3$$

Analicemos:

El texto nos propone esa matriz. Ya sabemos que cada columna fue producto de un valor asignado, y podemos ver que hay tres columnas entonces estamos hablando de una base de un espacio lineal de $dimV = 3$

Es muy importante recalcar la frase "**Elijamos las bases usuales**" ya que en otras palabras está diciendo que los valores asignados son solamente una combinación lineal así:

- $T(e_1) = 3(w_1) + 1(w_2)$
- $T(e_2) = 1(w_1) + 0(w_2)$
- $T(e_3) = -2(w_1) + 4(w_2)$

Donde $w_1 = (1,0) \quad w_2 = (0,1)$, osea que obtenemos los mismos vectores y armamos de nuevo la matriz.

Entonces para un vector cualquiera $x = (x_1, x_2, x_3)$ si aplicamos la transformación lo hacemos teniendo en cuenta la base, osea que escribimos el vector así

$$T(x_1e_1 + x_2e_2 + x_3e_3)$$

Y aplicamos la linealidad de la transformación

$$T(x_1e_1 + x_2e_2 + x_3e_3) = x_1T(e_1) + x_2T(e_2) + x_3T(e_3)$$

y finalmente reemplazamos los valores asignados

$T(x_1e_1 + x_2e_2 + x_3e_3) = x_1(3(w_1) + 1(w_2)) + x_2(1(w_1) + 0(w_2)) + x_3(-2(w_1) + 4(w_2))$

$T(x_1e_1 + x_2e_2 + x_3e_3) = x_1(3(1,0) + 1(0,1)) + x_2(1(1,0) + 0(0,1)) + x_3(-2(1,0) + 4(0,1))$

$T(x_1e_1 + x_2e_2 + x_3e_3) = x_1(3,1) + x_2(1,0) + x_3(-2, 4)$

$T(x_1e_1 + x_2e_2 + x_3e_3) = (3x_1 + x_2 - 2x_3, x_1 + 0x_2 + 4x_3)$


si tomamos ese ultimo resultado por cada componente obtenemos lo mismo de arriba

$$y_1 = 3x_1 + x_2 - 2x_3$$

$$y_2 = x_1 + 0x_2 + 4x_3$$

esto lo utilizaremsos mas adelante

#### Ejemplo 2

Ahora el texto nos propone un ejercicio muy interesante, tenemos:

- El espacio lineal $V$ con todos los polinomios reales $p(x)$ de grado $\leq 3$ de dimensión $4$, con la base $(1,x,x^2,x^3)$
- El operador $D$ de derivación que aplica cada polinomio $p(x)$ de $V$ en su derivada $p'(x)$. Podemos considerar $D$ como una transformación lineal de $V$ en $W$ 
- Por lo tanto el espacio lineal $W$ es el espacio lineal de todos los polinomios de grado $\leq 2$
- En $W$ exigimos la base $(1,x,x^2)$

Entonces, para encontrar la representación matricial de $D$ realitva a esas bases, transformamos (derivamos) cada elemento base de $V$ y lo representamos como una combinación lineal de los elemnetos de $W$


- $D(1) = 0 \cdot 1 + 0x + 0x^2$ 
- $D(x) = 1 \cdot 1 + 0x + 0x^2$ 
- $D(x^2) = 0 \cdot 1 + 2x + 0x^2$ 
- $D(x^3) = 0 \cdot 1 + 0x + 3x^2$ 


Como vimos anteriormente los coeficientes de (en este caso) cada polinimio representan los elementos de la matriz $3 \times 4$

```math
\begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \end{pmatrix}
```

¿para qué nos puede servir esta matriz? personalmente me pareció interesante lo siguiente:

Si hacemos el desarrollo para un elemento de $V$ cualquiera por ejemplo $x = 0 \cdot 1 + 0x + \frac{5}{3}x^2 + 7x^3$ y aplicamos la transformación obtenemos

$D(\frac{5}{3}x^2 + 7x^3) = \frac{5}{3}D(x^2) + 7D(x^3)$ y usamos los valores asignados

$D(\frac{5}{3}x^2 + 7x^3) = \frac{5}{3}(2x) + 7(3x^2)$ 

$D(\frac{5}{3}x^2 + 7x^3) = \frac{10}{3}x + 21x^2$ 

y vemos que obviamente vamos a obtener la derivada, ya que por la linealidad de la tranformación la aplicamos directamente en los valores asignados

ahora, si hacemos esta multiplicación matriz-vector

```math
\begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \end{pmatrix} \begin{pmatrix} 0 \\ 0 \\ 5/3 \\ 7\end{pmatrix} = \begin{pmatrix} 0 \\ 10/3 \\ 21\end{pmatrix}
```

lo cual corresponde con la derivada, ya que el resultado vive en $W$ y corresponde a la base $\lbrace 1, x, x^2 \rbrace$ de la siguiente manera

$$0 \cdot 1 + \frac{10}{3}x + 21x^2$$

Ahora para dejar en evidencia como la base es importante aunque no aparezca en el resultado visible de la matriz, invirtamos el orden de la base $(x^2,x,1)$ y generemosla 

- $D(1) = 0x^2 + 0x + 0 \cdot 1$
- $D(x) = 0x^2 + 0x + 1 \cdot 1 $
- $D(x^2) = 0x^2 + 2x + 0 \cdot 1$ 
- $D(x^3) = 3x^2 + 0x + 0 \cdot 1$ 


```math
\begin{pmatrix} 0 & 0 & 0 & 3 \\ 0 & 0 & 2 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix}
```

vemos que el resultado de la matriz también aparece en ornden inverso. Y si hacemos la multiplicación como antes 


```math
\begin{pmatrix} 0 & 0 & 0 & 3 \\ 0 & 0 & 2 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} 0 \\ 0 \\ 5/3 \\ 7\end{pmatrix} = \begin{pmatrix} 21 \\ 10/3 \\ 0\end{pmatrix}
```

obtenemos el orden inverso, y eso está bien ya que la base también se invirtió entonces los escalares del resultado corresponden correctamente a la base. Es muy importante tener en cuenta que lo que cambió fue la base de $W$ pero no la de $V$ por eso el argumento sigue siendo el mismo.

#### Ejemplo 3 — una tercera representación de $D$ (ahora la base de $V$ no es canónica)

Ahora el texto nos propone calcular una **tercera** representación matricial del operador derivación $D$, pero con un una base diferente para $V$, tenemos entonces:

- El espacio lineal $V$ con todos los polinomios reales de grado $\leq 3$, pero ahora con la base $(1,\ 1+x,\ 1+x+x^2,\ 1+x+x^2+x^3)$
- El espacio lineal $W$ de los polinomios de grado $\leq 2$, con la base usual $(1, x, x^2)$
- El operador $D$ que aplica cada polinomio en su derivada

Llamemos a los elementos de la base de $V$ así:

- $e_1 = 1$
- $e_2 = 1+x$
- $e_3 = 1+x+x^2$
- $e_4 = 1+x+x^2+x^3$

Entonces, igual que antes, transformamos (derivamos) cada elemento base de $V$ y lo escribimos como combinación lineal de los elementos de $W$:

- $D(e_1) = D(1) = 0 = 0 \cdot 1 + 0x + 0x^2$
- $D(e_2) = D(1+x) = 1 = 1 \cdot 1 + 0x + 0x^2$
- $D(e_3) = D(1+x+x^2) = 1 + 2x = 1 \cdot 1 + 2x + 0x^2$
- $D(e_4) = D(1+x+x^2+x^3) = 1 + 2x + 3x^2 = 1 \cdot 1 + 2x + 3x^2$

Cada uno de estos valores asignados es un vector columna respecto a la base $(1, x, x^2)$ de $W$:

$$D(e_1) = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \quad
D(e_2) = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \quad
D(e_3) = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix} \quad
D(e_4) = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$$

Y poniendo las columnas una junto a la otra armamos la matriz $3 \times 4$:

```math
\begin{pmatrix} 0 & 1 & 1 & 1 \\ 0 & 0 & 2 & 2 \\ 0 & 0 & 0 & 3 \end{pmatrix}
```

que es exactamente la que muestra el libro.

> Comparemos con la representación canónica del Ejemplo 2:
> ```math
> \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \end{pmatrix}
> ```
> Es la **misma transformación $D$**, pero la matriz cambió solo por haber cambiado la base de $V$. Esto refuerza lo que hemos visto durante este capítulo: la matriz no es "la transformación", es la transformación **vista a través de un par de bases**.

#### Verificación con un elemento concreto

Tomemos un polinomio cualquiera de $V$, por ejemplo:

$$p(x) = 5 + 4x + 2x^2 + x^3$$

Calculemos primero su derivada "a mano", que es lo que debería darnos al final:

$$D(p) = 4 + 4x + 3x^2$$

Ahora quiero obtener esto mismo con la multiplicación matriz-vector. Y aquí está **lo importante**: el vector columna que metemos NO son los coeficientes de los monomios de $p(x)$. Son las componentes de $p(x)$ **respecto a la base de $V$**, que ya no es canónica.

Es decir, tengo que encontrar los $c_1, c_2, c_3, c_4$ tales que:

$$p(x) = c_1 e_1 + c_2 e_2 + c_3 e_3 + c_4 e_4$$

Obtenemos esto 

$$p(x) = c_1(1) + c_2(1+x) + c_3(1+x+x^2) + c_4(1+x+x^2+x^3)$$

$$p(x) = (c_1 + c_2 + c_3 + c_4) + (c_2 + c_3 + c_4)x + (c_3 + c_4)x^2 + c_4 x^3$$

después tenemos que encontrar esas constantes igualando coeficiente a coeficiente con $p(x) = 5 + 4x + 2x^2 + x^3$, lo resolvemos "de arriba hacia abajo" empezando por el grado más alto:

- $x^3$: $c_4 = 1$
- $x^2$: $c_3 + c_4 = 2 \Rightarrow c_3 = 1$
- $x^1$: $c_2 + c_3 + c_4 = 4 \Rightarrow c_2 = 2$
- $x^0$: $c_1 + c_2 + c_3 + c_4 = 5 \Rightarrow c_1 = 1$

Entonces las componentes de $p(x)$ en la base de $V$ son $(1, 2, 1, 1)$, y **ese** es el vector que va en la columna:

```math
\begin{pmatrix} 0 & 1 & 1 & 1 \\ 0 & 0 & 2 & 2 \\ 0 & 0 & 0 & 3 \end{pmatrix}
\begin{pmatrix} 1 \\ 2 \\ 1 \\ 1 \end{pmatrix}
=
\begin{pmatrix} 4 \\ 4 \\ 3 \end{pmatrix}
```

El resultado vive en $W$ con la base $(1, x, x^2)$, así que se interpreta como:

$$4 \cdot 1 + 4x + 3x^2 = 4 + 4x + 3x^2$$

que coincide exactamente con la derivada que calculamos a mano. 🎯

#### La trampa (por qué la base de $V$ sí importa)

Aprovechando el mismo ejemplo donde antes mostré que la base de $W$ ordena el resultado, ahora la base de $V$ nos enseña otra cosa: **ordena la entrada**.

¿Qué hubiera pasado si, por descuido, hubiera metido los coeficientes de los monomios de $p(x) = 5 + 4x + 2x^2 + x^3$, o sea $(5, 4, 2, 1)$, como si la base de $V$ fuera la canónica?

```math
\begin{pmatrix} 0 & 1 & 1 & 1 \\ 0 & 0 & 2 & 2 \\ 0 & 0 & 0 & 3 \end{pmatrix}
\begin{pmatrix} 5 \\ 4 \\ 2 \\ 1 \end{pmatrix}
=
\begin{pmatrix} 7 \\ 6 \\ 3 \end{pmatrix}
\;\Rightarrow\; 7 + 6x + 3x^2
```

Eso **no es la derivada de $p(x)$**. Es un resultado completamente equivocado, porque le estoy dando a la matriz componentes que están en una base distinta a la que la matriz "espera".

Y esto cierra simétricamente la idea de los apuntes anteriores:

- La base de $W$ no aparece en la matriz, pero **ordena cómo se lee la salida**.
- La base de $V$ tampoco aparece en la matriz, pero **ordena cómo se debe escribir la entrada**.

La matriz es solo la tabla de coeficientes "desnuda". Las dos bases están por debajo, invisibles, una a cada lado, y son las que le dan sentido tanto a lo que entra como a lo que sale.
