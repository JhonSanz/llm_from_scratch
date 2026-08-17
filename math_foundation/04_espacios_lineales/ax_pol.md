# Espacio lineal de todos los polinomios

Sea $V = \mathbb{R}[t]$, el conjunto de todos los polinomios con coeficientes reales. Un elemento típico es:

$$p(t) = a_0 + a_1 t + a_2 t^2 + \cdots + a_n t^n$$

donde $n$ puede ser cualquier entero no negativo y $a_i \in \mathbb{R}$.

Definimos las operaciones:

**Adición:** Si $p(t) = \sum_{i=0}^{n} a_i t^i$ y $q(t) = \sum_{i=0}^{m} b_i t^i$, entonces

$$(p + q)(t) = \sum_{i=0}^{\max(n,m)} (a_i + b_i) t^i$$

donde completamos con ceros los coeficientes faltantes.

**Multiplicación por escalar:** $(\alpha p)(t) = \sum_{i=0}^{n} (\alpha a_i) t^i$

---

## Axioma 1 — Clausura respecto de la adición

Dados $p, q \in V$, la suma $(p+q)(t) = \sum (a_i + b_i)t^i$ tiene coeficientes $a_i + b_i \in \mathbb{R}$, y es un polinomio (suma finita de términos), por lo tanto $p + q \in V$. La unicidad se sigue de la unicidad de la suma en $\mathbb{R}$.

## Axioma 2 — Clausura respecto de la multiplicación por escalar

Dado $p \in V$ y $\alpha \in \mathbb{R}$, el producto $(\alpha p)(t) = \sum \alpha a_i t^i$ tiene coeficientes $\alpha a_i \in \mathbb{R}$ y sigue siendo un polinomio, así que $\alpha p \in V$.

## Axioma 3 — Ley conmutativa

$$(p + q)(t) = \sum (a_i + b_i)t^i = \sum (b_i + a_i)t^i = (q + p)(t)$$

por conmutatividad de la suma en $\mathbb{R}$.

## Axioma 4 — Ley asociativa de la adición

$$((p+q)+r)(t) = \sum ((a_i + b_i) + c_i)t^i = \sum (a_i + (b_i + c_i))t^i = (p+(q+r))(t)$$

por asociatividad en $\mathbb{R}$.

## Axioma 5 — Existencia del elemento cero

Sea $O(t) = 0$ (el polinomio cuyos coeficientes son todos cero). Entonces:

$$(p + O)(t) = \sum (a_i + 0)t^i = \sum a_i t^i = p(t)$$

## Axioma 6 — Existencia de opuestos

Para $p \in V$, tomamos $(-1)p(t) = \sum (-a_i)t^i$. Entonces:

$$(p + (-1)p)(t) = \sum (a_i + (-a_i))t^i = \sum 0 \cdot t^i = O(t)$$

## Axioma 7 — Ley asociativa de la multiplicación por escalares

$$(\alpha(\beta p))(t) = \alpha \sum (\beta a_i)t^i = \sum (\alpha \beta a_i)t^i = ((\alpha\beta)p)(t)$$

por asociatividad de la multiplicación en $\mathbb{R}$.

## Axioma 8 — Distributiva respecto de la adición en $V$

$$(\alpha(p+q))(t) = \alpha \sum (a_i + b_i)t^i = \sum (\alpha a_i + \alpha b_i)t^i = (\alpha p + \alpha q)(t)$$

por distributividad en $\mathbb{R}$.

## Axioma 9 — Distributiva respecto de la adición de escalares

$$((\alpha + \beta)p)(t) = \sum (\alpha + \beta)a_i t^i = \sum (\alpha a_i + \beta a_i)t^i = (\alpha p + \beta p)(t)$$

## Axioma 10 — Existencia del elemento idéntico

$$(1 \cdot p)(t) = \sum (1 \cdot a_i)t^i = \sum a_i t^i = p(t)$$

---

> **Nota:** La lógica es la misma de nuevo: las operaciones se definen **coeficiente a coeficiente**, así que cada axioma se reduce a verificar la propiedad correspondiente en $\mathbb{R}$. Es el mismo patrón que en $V_n$ (componente a componente) y en $\mathcal{F}(I)$ (punto a punto).