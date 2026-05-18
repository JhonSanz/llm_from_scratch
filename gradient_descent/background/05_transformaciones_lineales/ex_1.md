## Algunos ejemplos 


$T: \mathbb{R} → \mathbb{R}$, donde $T(x) = 3x$

Sean $V = \mathbb{R}$ y $W = \mathbb{R}$. $T$ aplica cada elemento $x$ de $\mathbb{R}$ en el elemento $y = 3x$ de $\mathbb{R}$. Es el Ejemplo 3 de Apostol con escalar fijo $c = 3$.

$$T(x+x') = 3(x+x') = 3x + 3x' = T(x) + T(x') \checkmark$$

$$T(cx) = 3(cx) = c(3x) = cT(x) \checkmark$$

---

$T: \mathbb{R} → \mathbb{R}³$ donde $T(x) = (x, 2x, 3x)$

Sean $V = \mathbb{R}$ y $W = \mathbb{R}^3$. $T$ toma un número real y produce un vector de 3 componentes. La imagen de $T$ es una recta en $\mathbb{R}^3$ que pasa por el origen en dirección $(1, 2, 3)$.

$$T(x+x') = (x+x',\ 2(x+x'),\ 3(x+x')) = T(x) + T(x') \checkmark$$

$$T(cx) = (cx, 2cx, 3cx) = cT(x) \checkmark$$

---

$T: \mathbb{R}^3 → P_2$ donde $T(a, b, c) = a + bx + cx^2$

Sean $V = \mathbb{R}^3$ y $W = P_2$ (polinomios de grado $\leq 2$). $T$ toma un vector de $\mathbb{R}^3$ y produce un polinomio. Ilustra que $V$ y $W$ pueden ser de **naturaleza completamente distinta**.

$$T(a+a',\ b+b',\ c+c') = (a+a') + (b+b')x + (c+c')x^2 = T(a,b,c) + T(a',b',c') \checkmark$$

$$T(\lambda a,\ \lambda b,\ \lambda c) = \lambda a + \lambda bx + \lambda cx^2 = \lambda\, T(a,b,c) \checkmark$$


## Ejemplo 4 de Apostol — Ecuaciones lineales

Sean $V = V_n$ y $W = V_m$. Dados mn números reales $a_{ik}$, con $i = 1, 2, \ldots, m$ y $k = 1, 2, \ldots, n$, definimos $T: V_n \to V_m$ como sigue: T aplica cada vector $x = (x_1, \ldots, x_n)$ de $V_n$ en el vector $y = (y_1, \ldots, y_m)$ de $V_m$ de acuerdo con las ecuaciones:

$$y_i = \sum_{k=1}^{n} a_{ik} x_k \quad \text{para } i = 1, 2, \ldots, m$$


Los coeficientes $a_{ik}$ en este punto del libro son simplemente **números organizados por dos índices** — el concepto de matriz se introduce más adelante, motivado precisamente por este ejemplo.

Los coeficientes se pueden visaulizar de esta manera

$$A = \begin{pmatrix} 
a_{11} & a_{12} & \cdots & a_{1n} \\ 
a_{21} & a_{22} & \cdots & a_{2n} \\ 
\vdots & \vdots & \ddots & \vdots \\ 
a_{m1} & a_{m2} & \cdots & a_{mn} 
\end{pmatrix}$$

$T$ toma un vector de entrada:

$x = (x_1, x_2, ..., x_n)  \in  V_n$

para producir un vector de salida:

$y = (y_1, y_2, ..., y_m)  \in  V_m$

donde **cada componente del vector $y$ se calcula así**:

$y_i = a_{i1}x_1 + a_{i2}x_2 + ... + a_{in}x_n$

como se menciona en el enunciado. Es decir, escribiendo completo el desarrollo del ejercicio tenemos lo siguiente

$y_1 = a_{11}x_1 + a_{12}x_2 + ... + a_{1n}x_n$

$y_2 = a_{21}x_1 + a_{22}x_2 + ... + a_{2n}x_n$

$\vdots$

$y_m = a_{m1}x_1 + a_{m2}x_2 + ... + a_{mn}x_n$

formando el vector resultante.

### Ahora bien, queremos verificar que $T$ es una transformación lineal, es decir, que cumple:

- **a.** $T(x + x') = T(x) + T(x')$
- **b.** $T(cx) = cT(x)$


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


### Caso especial — todos los coeficientes iguales a 1

Cada $y_i$ se convierte en la suma de todas las componentes de x:

$$y_i = x_1 + x_2 + \cdots + x_n = S$$

El vector de salida es $y = (S, S, \ldots, S)$. Esto significa que vectores muy distintos pueden producir la misma salida — la transformación pierde información.

---

## 4. El poder de las transformaciones lineales

$T$ puede mapear entre espacios de cualquier naturaleza, no solo vectores en $\mathbb{R}^n$:

$\mathbb{R} \to \mathbb{R}^3$       (expande)

$\mathbb{R}^3 \to \mathbb{R}$        (colapsa)

$\mathbb{R}^n \to \mathbb{R}^m$       (caso general)

$\mathbb{R}^3 \to P_2$ (vector → polinomio)

$P \to P$ (polinomio → polinomio)

$C[a,b] → $\mathbb{R}$        (función → número)


### Dos casos especialmente importantes

**Derivada:** $T(p) = p'$ es una transformación lineal de polinomios en polinomios.

**Integral:** $T(f) = \int_a^b f(x)\, dx$ es una transformación lineal de funciones continuas en \mathbb{R}.

$$\int_a^b [f(x) + g(x)]\, dx = \int_a^b f(x)\, dx + \int_a^b g(x)\, dx \checkmark$$

$$\int_a^b cf(x)\, dx = c\int_a^b f(x)\, dx \checkmark$$

Esto revela que **las operaciones del cálculo son transformaciones lineales** — el álgebra lineal abstracta es el lenguaje que unifica el cálculo, el análisis y la física.

---

## 5. Por qué V y W deben ser espacios lineales

Las propiedades de aditividad y homogeneidad requieren que la suma y la multiplicación por escalar existan y estén bien definidas en V y W. Si alguno de los dos no cumple los 10 axiomas, la definición de transformación lineal **no se puede ni siquiera escribir**.

### Ejemplo del colapso — polinomios de grado exactamente 2

Tomando $p = x^2 + 3x + 1$ y $q = -x^2 + 2x + 4$, ambos de grado exactamente 2:

$p + q = 5x + 5$ ← grado 1, sale del conjunto


$T(p + q)$ no se puede calcular porque $p + q$ ya no pertenece a V. El problema es que este conjunto **no es espacio lineal** — falla el axioma de clausura bajo la suma.

---

## Idea central

> Los 10 axiomas del espacio lineal no son arbitrarios — son exactamente las propiedades mínimas que necesitas para que el concepto de transformación lineal tenga coherencia. Por eso Apostol construye todo en ese orden: axiomas → espacios lineales → transformaciones lineales → todo lo demás.


---

![alt text](img/ex_producto_interior.png)


La pregunta es: **¿por qué $T$ es una transformación lineal?**

La respuesta está completamente contenida en los axiomas del producto interior.

Un espacio lineal real $V$ tiene producto interior si a cada par $x, y \in V$ corresponde un número real $(x, y)$ que satisface:

1. $(x, y) = (y, x)$ — *conmutatividad o simetría*
2. $(x, y + z) = (x, y) + (x, z)$ — *distributividad o linealidad*
3. $c(x, y) = (cx, y)$ — *homogeneidad escalar*; si $c = 0$ entonces $(0, y) = 0$
4. $(x, x) > 0$ si $x \neq 0$ — *positividad*

### Por qué $T$ es lineal con $z$ fijo

Verificación de aditividad

$$T(x + y) = (x + y,\ z) \overset{\text{axioma 2}}{=} (x, z) + (y, z) = T(x) + T(y) \quad \checkmark$$

El axioma 2 hace exactamente el trabajo — la distributividad en el primer argumento es la aditividad de $T$.

Verificación de homogeneidad

$$T(cx) = (cx,\ z) \overset{\text{axioma 3}}{=} c \cdot (x, z) = c \cdot T(x) \quad \checkmark$$

El axioma 3 hace exactamente el trabajo — la homogeneidad escalar en el primer argumento es la homogeneidad de $T$.

### ¿Por qué $z$ fijo es crucial?

Los axiomas 2 y 3 actúan sobre el **primer argumento**. Con $z$ constante, $T$ solo mueve ese primer argumento, y ese movimiento es exactamente lineal. Si $z$ no fuera fijo, $T$ no sería ni siquiera una función bien definida de $V$ a $\mathbb{R}$.

## ¿Por qué el producto interior no es lineal en ambas variables?

El producto interior sí es una función de dos variables, $B: V \times V \to \mathbb{R}$ con $B(x, y) = (x, y)$. Pero **no es lineal como función del par $(x, y)$**.

La demostración es por contradicción. Si $B$ fuera lineal, debería cumplir $B(c \cdot (x, y)) = c \cdot B(x, y)$, es decir:

$$B(cx, cy) = c \cdot B(x, y)$$

Calculando el lado izquierdo y aplicando el axioma 3 **dos veces** (una por cada argumento):

$$(cx, cy) \overset{\text{axioma 3}}{=} c(x, cy) \overset{\text{axioma 3}}{=} c^2(x, y)$$

Pero el lado derecho es $c \cdot (x, y)$. Entonces tendría que cumplirse:

$$c^2 (x, y) = c \cdot (x, y) \quad \text{para todo } c \text{ y todo } x, y$$

Por ejemplo, en $\mathbb{R}^2$ con el producto punto estándar $(x, y) = x_1 y_1 + x_2 y_2$,
tomando $x = y = (1, 0)$ y $c = 3$:

- Lado izquierdo: $B(cx, cy) = ((3,0),\ (3,0)) = 3\cdot3 + 0\cdot0 = 9$
- Lado derecho: $c \cdot B(x, y) = 3\cdot((1,0),\ (1,0)) = 3\cdot(1\cdot1 + 0\cdot0) = 3$

$9 \neq 3$. Contradicción.