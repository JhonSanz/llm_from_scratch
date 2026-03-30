# Transformaciones lineales y matrices

Las transformaciones, aplicaciones y operadores son funciones cuyos dominios y recorridos son subconjuntos de espacios lineales. Aqui vamos a ver los ejemplos mas sencillos llamados transformaciones lineales

La notación que utilizamos mas comunmente para funciones cualquiera es 

$$T: V \to W$$

Entonces:

- T es una funcion
- V es el dominio
- W es la imagen

Para cada $x$ de $V$ el elemento $T(x)$ de $W$ se llama **imagen de $x$ a través de $T$**, y decimos que $T$ aplica $x$ en $T(x)$

Hasta aquí es lo que conocemos de toda la vida, tomar un $x$ pasarlo a través de una "máquina" y obtener un resultado. Sin embargo, nos estamos fijando mas en los conjuntos, veamos este gráfico

![alt text](img/tl_1.png)

Podemos tener un subconjunto $A$ del dominio $V$, cuyas imágenes $T(x)$ para $x$ de $A$ están en $T(A)$. Podríamos tener que $A = V$ en ese caso $T(A) = T(V)$ la imagen del dominio $V$ es el recorrido de $T$

Para definir la transformación lineal el texto nos propone trabajar con el **mismo conjunto numérico de escalares** en ambos $V$ y $W$, por ejemplo $\mathbb{R}$ en ambos o complejos en ambos

**DEFINICIÓN**: Si $V$ y $W$ son dos espacios lineales, una función $T: V \to W$ se llama transformación lineal de $V$ en $W$, si tiene las propiedades siguientes

- $T(x + y) = T(x) + T(y)$ para cualquier $x$ y $y$ de $V$
- $T(cx) = cT(x)$ para todo $x$ de $V$ y cualquier escalar $c$

esto quiere decir que $T$ conserva la suma y la multiplicación por escalares. Podríamos combinar todo en una única fórmula

$$T(ax + by) = aT(x) + bT(y)$$

o lo que es lo mismo, escrito con sumas

$$T(\sum_{i=1}^{n} a_ix_i) = \sum_{i=1}^{n} a_iT(x_i)$$

para $n$ elementos cualesquiera $x_1, \dots, x_n$ de $V$, y $n$ escalares cualquiera $a_1, \dots, a_n$

#### Ejemplos


Sean $V = V_n$ y $W = V_m$. Dados $mn$ números reales $a_{ik}$, con $i = 1, 2, \ldots, m$ y $k = 1, 2, \ldots, n$, definimos $T: V_n \to V_m$ como:

$$y_i = \sum_{k=1}^{n} a_{ik} x_k \quad \text{para } i = 1, 2, \ldots, m$$

Queremos verificar que $T$ es una transformación lineal, es decir, que cumple:

- **a)** $T(x + x') = T(x) + T(x')$
- **b)** $T(cx) = cT(x)$

Para esto me parece importante resaltar que lo realmente importante aquí es ver si la transformación cumple con la definición, a través de su operación misma. Si bien la operación retorna un resultado, este no es tan relevante porque en este ejemplo es la sumatoria la que nos dice si se cumplen las propiedades, no el resultado de ella

Sean $x = (x_1, \ldots, x_n)$ y $x' = (x'_1, \ldots, x'_n)$ dos vectores de $V_n$.

Entonces:

$$x + x' = (x_1 + x'_1, \ldots, x_n + x'_n)$$

Aplicamos $T$ a la suma. La componente $i$-ésima del resultado es:

$$[T(x + x')]_i = \sum_{k=1}^{n} a_{ik}(x_k + x'_k)$$

Distribuimos $a_{ik}$:

$$= \sum_{k=1}^{n} (a_{ik} x_k + a_{ik} x'_k)$$

Separamos la sumatoria en dos:

$$= \sum_{k=1}^{n} a_{ik} x_k + \sum_{k=1}^{n} a_{ik} x'_k$$

$$= [T(x)]_i + [T(x')]_i$$

Como esto vale para todo $i = 1, \ldots, m$, concluimos:

$$T(x + x') = T(x) + T(x')$$

Ahora, sea $c$ un escalar y $x = (x_1, \ldots, x_n)$ un vector de $V_n$.

Entonces:

$$cx = (cx_1, \ldots, cx_n)$$

La componente $i$-ésima de $T(cx)$ es:

$$[T(cx)]_i = \sum_{k=1}^{n} a_{ik}(cx_k)$$

Sacamos $c$ de la sumatoria (es constante respecto a $k$):

$$= c \cdot \sum_{k=1}^{n} a_{ik} x_k$$

$$= c \cdot [T(x)]_i$$

Como vale para todo $i = 1, \ldots, m$, concluimos:

$$T(cx) = cT(x)$$

Ambas propiedades se cumplen, por lo tanto $T$ es una **transformación lineal**.

---

¿Por qué $f(x) = x^2$ no es una transformación lineal?


$$f(x + y) = (x + y)^2 = x^2 + 2xy + y^2$$

$$f(x) + f(y) = x^2 + y^2$$

El término $2xy$ que sobra hace que no sean iguales.

**Ejemplo numérico:** con $x = 2$, $y = 3$:

$$f(2 + 3) = f(5) = 25$$

$$f(2) + f(3) = 4 + 9 = 13$$

$$25 \neq 13 \quad \boldsymbol{\times}$$


Ahora cumple $f(cx) = cf(x)$?

$$f(cx) = (cx)^2 = c^2 x^2$$

$$cf(x) = cx^2$$

En general, $c^2 \neq c$.

**Ejemplo numérico:** con $c = 3$, $x = 2$:

$$f(3 \cdot 2) = f(6) = 36$$

$$3 \cdot f(2) = 3 \cdot 4 = 12$$

$$36 \neq 12 \quad \boldsymbol{\times}$$

Este es exactamente el mismo problema que ocurre con $T(x) = (x, x)$ (producto interior con $z = x$, no fijo).

![alt text](img/ex_producto_interior.png)

Cuando la entrada aparece **dos veces** en la operación, escalar por $c$ produce $c^2$ en lugar de $c$. Fijar $z$ elimina esa duplicación: $z$ ya no depende de la entrada, así que $c$ solo entra una vez.

| Función | $f(cx)$ | $cf(x)$ | ¿Lineal? |
|---------|---------|---------|----------|
| $f(x) = x^2$ | $c^2 x^2$ | $cx^2$ | No |
| $T(x) = (x, x)$ | $c^2(x,x)$ | $c(x,x)$ | No |
| $T(x) = (x, z)$ con $z$ fijo | $c(x,z)$ | $c(x,z)$ | **Sí** |

---

Sea $V$ el espacio lineal de todas las funciones reales $f$ derivables en un intervalo abierto $(a, b)$.

Definimos el operador derivación $D: V \to W$ como:

$$D(f) = f'$$

donde $W$ contiene todas las derivadas $f'$.

$$D(f + g) = (f + g)'$$

Por la regla de la suma de derivadas:

$$= f' + g'$$

Ahora verifiquemos la multiplicacion por escalar

$$= D(f) + D(g) \quad \checkmark$$


$$D(cf) = (cf)'$$

Por la regla de la constante multiplicativa en derivadas:

$$= cf'$$

$$= cD(f) \quad \checkmark$$


El operador derivación $D$ es una **transformación lineal**.

La linealidad se deduce directamente de las reglas de derivación del cálculo:

- La derivada de una suma es la suma de las derivadas.
- La derivada de una constante por una función es la constante por la derivada.


## Núcleo y recorrido

Como vimos en el dibujo anterior $T(V)$ (recorrido de $T$) es un subconjunto de $W$. Veamos si es un subespacio, y si además $T$ aplica el elemento cero de $V$ en el de $W$

Recordando nuestra definición de subespacio, necesitamos que el subconjunto cumpla con los axiomas de clausura (suma y multiplicación por escalar). Entonces como hicimos en el tutorial de espacios lineales necesitamos tomar dos elementos $T(x)$ $T(y)$ del conjunto y ver si el resultado está también en el conjunto

$$T(x) + T(y) = T(x + y)$$

Esto porque ya definimos que la transformación lineal tiene la propiedad de la suma de esta manera. Entonces se cumple y el resultado está en $T(V)$

Lo mismo para cualquier escalar $c$, tenemos que $T(cx) = cT(x)$ porque así se define la transformación lineal, y el resultado también está en $T(V)$. Finalmente si tomamos $c = 0$ encontramos que $T(O) = O$

Ahora, el **núcleo** es el conjunto de todos los $V$ que $T$ aplica a $O$ se llama núcleo de $T$ y se designa por $N(T)$, osea

$$N(T) = \lbrace x | x \in V \quad \text{ y } \quad T(x) = O \rbrace$$

El **núcleo también es un subespacio de** $V$ ya que son los mismo valores que toma la transformación de $V$, y la demostración es similar

#### Ejemplos

Sea $T: \mathbb{R}^2 \to \mathbb{R}$ definida por:

$$T(x_1, x_2) = x_1 + x_2$$

Primero verificamos que es una transformación lineal:

**Suma:** Sean $x = (x_1, x_2)$ y $y = (y_1, y_2)$

$$T(x + y) = T(x_1 + y_1, x_2 + y_2) = (x_1 + y_1) + (x_2 + y_2) = (x_1 + x_2) + (y_1 + y_2) = T(x) + T(y) \quad \checkmark$$

**Multiplicación por escalar:** Sea $c$ un escalar

$$T(cx) = T(cx_1, cx_2) = cx_1 + cx_2 = c(x_1 + x_2) = cT(x) \quad \checkmark$$

Ahora hallamos el **núcleo**. Necesitamos todos los $(x_1, x_2)$ tales que $T(x_1, x_2) = 0$:

$$x_1 + x_2 = 0 \implies x_2 = -x_1$$

$$N(T) = \lbrace (x_1, -x_1) \mid x_1 \in \mathbb{R} \rbrace$$

Geométricamente es la recta $x_2 = -x_1$ en $\mathbb{R}^2$, y es un subespacio porque:

- $(x_1, -x_1) + (y_1, -y_1) = (x_1 + y_1, -(x_1 + y_1)) \in N(T) \quad \checkmark$
- $c(x_1, -x_1) = (cx_1, -cx_1) \in N(T) \quad \checkmark$

---

**Operador derivación**. El núcleo está formado por todas las funciones constantes en el intervalo dado.

---

Para resumir visualmente, el núcleo lo podemos entender de esta manera 

![alt text](img/nucleo.png)

## Dimensión del núcleo y rango de la transformación

Nos interesa la relación entre las dimensiones de $V$, del núcleo $N(T)$ y del recorrido $T(V)$. Si $V$ es de dimensión finita, el núcleo también lo será por ser un subespacio de $V$

La dimensión de $T(V)$ se llama **rango** de $T$

**TEOREMA** Si $V$ es de dimensión finita, también lo es $T(V)$, y tenemos

$$dim N(T) + dim T(V) = dim V$$

Dicho de otro modo, la dimensión del núcleo más el rango de una transformación lineal es igual a la dimensión de su dominio.

Ver la Demostración en Cálculo de Tom Apostol Vol 2 Pág 43


## Operaciones algebráicas con transformaciones lineales

"Las funciones cuyos valores pertenecen a un espacio lineal dado $W$ pueden sumarse unas con otras y pueden multiplicarse por escalares de $W$ de acuerdo con la definición siguiente.

**DEFINICIÓN**. Sean $S:V \to W$ y $T: V \to W$ dos funciones con un dominio común $V$ y con valores pertenecientes a un espacio lineal $W$. Si e es un escalar cualquiera de W, definimos la suma S + $T$ y el producto $cT$ por las ecuaciones 


$$(S + T)(x) = S(x) + T(x) , (cT)(x) = cT(x)$$

para todo $x$ de $V$"


Verifiquemos con la fórmula combinada de linealidad:

$$(S + T)(ax + by) = S(ax + by) + T(ax + by)$$

Como $S$ y $T$ son lineales, cada una respeta la combinación lineal:

$$= aS(x) + bS(y) + aT(x) + bT(y)$$

Reagrupamos por escalar:

$$= a[S(x) + T(x)] + b[S(y) + T(y)]$$

$$= a(S + T)(x) + b(S + T)(y) \quad \checkmark$$

¿$cT$ sigue siendo lineal?

$$(cT)(ax + by) = cT(ax + by)$$

Como $T$ es lineal:

$$= c[aT(x) + bT(y)]$$

$$= a \cdot cT(x) + b \cdot cT(y)$$

$$= a(cT)(x) + b(cT)(y) \quad \checkmark$$


El conjunto $\mathscr{L}(V, W)$ de todas las transformaciones lineales de $V$ en $W$, es un espacio lineal con las operaciones de adición y multiplicación por escalar

Es decir, este conjunto que contiene todas las transformaciones lineales de $V$ en $W$, cumple los 10 axiomas, la mayoría de ellos con las operaciones con lo que acabamos de definir, y particularmente:

- El **elemento cero** es la transformación cero: $T_0(x) = O$ para todo $x$
- La **opuesta** de $T$ es $(-1)T$, es decir, $(-T)(x) = -T(x)$

Para resumir, nos armamos un conjunto con transformaciones lineales que cumplen los 10 axiomas, por lo tanto ese conjunto $\mathscr{L}(V, W)$ es un espacio lineal

### Composición de transformaciones lineales

Vamos a ver como se comporta la **composición o multiplicación** entre transformaciones lineales

- Supongamos tres conjuntos $U, V, W$
- $T: U \to V$ una función con dominio en $U$ y valores en $V$
- $S: V \to W$ otra función con dominio en $V$ y valores en $W$

La función compuesta $ST: U \to W$ está definida por:

$$(ST)(x) = S[T(x)] \quad \text{ para todo } x \text{ en } U$$

![alt text](img/composicion.png)

En el dibujo se ve bien, aplicamos primero $x$ mediante $T$ y luego $T(x)$ mediante $S$. 

Ahora, ¿qué pasa con el resultado de la composición? veamos varias cosas interesantes

#### La composición no es conmutativa

Veamos contraejemplo. Sean $T, S: \mathbb{R}^2 \to \mathbb{R}^2$ definidas por:

$$T(x_1, x_2) = (x_1 + x_2, \; 0) \qquad S(x_1, x_2) = (0, \; x_1)$$

Ambas son lineales (se verifica directamente con la definición). Para $x = (1, 1)$:

$$(ST)(1,1) = S(T(1,1)) = S(2, 0) = (0, 2)$$

$$(TS)(1,1) = T(S(1,1)) = T(0, 1) = (1, 0)$$

Como $(0, 2) \neq (1, 0)$, se tiene $ST \neq TS$. $\blacksquare$

#### Satisface la ley asociativa

Supongamos tres funciones 

- $T: U \to V$
- $S: V \to W$
- $R: W \to X$

y tenemos

$$R(ST) = (RS)T$$

Ambos lados de la ecuación tienen dominio $U$ y valores en $X$ (osea al hacer la "operación" para cualquier lado de la igualdad recorren de la misma manera el caminito en los conjuntos así como vimos en la imagen)

$$(R(ST))(x) = R((ST)(x)) = R(S(T(x)))$$

$$((RS)T)(x) = (RS)(T(x)) = R(S(T(x)))$$

como vemos nos da el mismo resultado. Se puede pensar de esta manera

$$x \xrightarrow{T} T(x) \xrightarrow{S} S[T(x)] \xrightarrow{R} R[S[T(x)]]$$

$$U \xrightarrow{T} V \xrightarrow{S} W \xrightarrow{R} X$$

osea, practicamente se toma la definicion de la composición, la cual se lee de izquierda a derecha y reescribimos de forma "desenrollada". EL orden es importante, el orden en que evaluamos no cambia por la posición de los paréntesis en la notación.

**DEFINICIÓN.** Sea $T: V \to V$ una función que aplica $V$ en sí mismo. Definimos inductivamente las potencias enteras de $T$ como sigue:

$$T^0 = I, \qquad T^n = TT^{n-1} \quad \text{para } n \geq 1.$$

Aquí $I$ representa la transformación idéntica. El lector puede comprobar que la ley asociativa implica la ley de exponentes $T^m T^n = T^{m+n}$ para todos los enteros no negativos $m$ y $n$.

