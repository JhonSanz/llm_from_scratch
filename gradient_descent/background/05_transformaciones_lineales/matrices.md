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

Con el teorema de valores asignados 