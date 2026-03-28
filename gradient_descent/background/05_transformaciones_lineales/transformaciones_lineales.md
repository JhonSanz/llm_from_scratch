# Transformaciones lineales y matrices

Las transformaciones, aplicaciones y operadores son funciones cuyos dominios y recorridos son subconjuntos de espacios lineales. Aqui vamos a ver los ejemplos mas sencillos llamados transformaciones lineales

La notación que utilizamos mas comunmente para funciones cualquiera es 

$$T: V \to W$$

Entonces:

- T es una funcion
- V es el dominio
- W es la imagen

Para cada $x$ de $V$ el elemento $T(x)$ de $W$ se llama **imagen de $x$ a través de $T$**, y decimos que "$T$ aplica $x$ en $T(x)$"

Hasta aquí es lo que conocemos de toda la vida, tomar un $x$ pasarlo a través de una "máquina" y obtener un resultado. Sin embargo, nos estamos fijando mas en los conjuntos, veamos este gráfico

![alt text](img/tl_1.png)

Podemos tener un subconjunto $A$ del dominio $V$, cuyas imágenes $T(x)$ para $x$ de $A$ están en $T(A)$. Podríamos tener que $A = V$ en ese caso $T(A) = T(V)$ la imagen del dominio $V$ es el "rango" o "recorrido" de $T$

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

$$T(x + x') = T(x) + T(x') \quad \checkmark$$

---

## Propiedad b): $T(cx) = cT(x)$

Sea $c$ un escalar y $x = (x_1, \ldots, x_n)$ un vector de $V_n$.

Entonces:

$$cx = (cx_1, \ldots, cx_n)$$

La componente $i$-ésima de $T(cx)$ es:

$$[T(cx)]_i = \sum_{k=1}^{n} a_{ik}(cx_k)$$

Sacamos $c$ de la sumatoria (es constante respecto a $k$):

$$= c \cdot \sum_{k=1}^{n} a_{ik} x_k$$

$$= c \cdot [T(x)]_i$$

Como vale para todo $i = 1, \ldots, m$, concluimos:

$$T(cx) = cT(x) \quad \checkmark$$

---

## Conclusión

Ambas propiedades se cumplen, por lo tanto $T$ es una **transformación lineal**.

La verificación se reduce a dos propiedades básicas de las sumatorias:

1. Se pueden separar en partes: $\sum (a + b) = \sum a + \sum b$
2. Una constante se puede sacar afuera: $\sum ca = c \sum a$