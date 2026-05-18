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