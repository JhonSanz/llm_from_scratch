# Espacio vectorial de todas las n-plas de números reales

Sea $V = V_n$, el espacio vectorial de todas las n-plas de números reales, con la adición y la multiplicación por escalares definidas en la forma ordinaria en función de los componentes.

Primero dejemos claro el escenario: estamos en $V_n$, el conjunto de todas las n-plas de números reales, con las operaciones:

$$x + y = (x_1 + y_1, \, x_2 + y_2, \, \ldots, \, x_n + y_n)$$
$$ax = (ax_1, \, ax_2, \, \ldots, \, ax_n)$$

donde $x = (x_1, \ldots, x_n)$, $y = (y_1, \ldots, y_n)$ y $a \in \mathbb{R}$.

## Axioma 1 — Clausura respecto de la adición

Dados $x, y \in V_n$, su suma es $(x_1 + y_1, \ldots, x_n + y_n)$. Como cada $x_i, y_i \in \mathbb{R}$ y los reales son cerrados bajo la suma, cada componente $x_i + y_i \in \mathbb{R}$, por lo tanto $x + y \in V_n$. La unicidad viene de que la suma de reales es única.

## Axioma 2 — Clausura respecto de la multiplicación por escalar

Dado $x \in V_n$ y $a \in \mathbb{R}$, el producto es $(ax_1, \ldots, ax_n)$. Como cada $ax_i \in \mathbb{R}$, el resultado pertenece a $V_n$.

## Axioma 3 — Ley conmutativa

$$x + y = (x_i + y_i) = (y_i + x_i) = y + x$$

donde usamos que la suma de números reales es conmutativa componente a componente.

## Axioma 4 — Ley asociativa de la adición

$$(x + y) + z = ((x_i + y_i) + z_i) = (x_i + (y_i + z_i)) = x + (y + z)$$

usando asociatividad de $\mathbb{R}$ en cada componente.

## Axioma 5 — Existencia del elemento cero

El elemento cero es $O = (0, 0, \ldots, 0)$. Entonces:

$$x + O = (x_i + 0) = (x_i) = x$$

## Axioma 6 — Existencia de opuestos

Para cada $x \in V_n$, tomamos $(-1)x = (-x_1, \ldots, -x_n)$. Entonces:

$$x + (-1)x = (x_i + (-x_i)) = (0, \ldots, 0) = O$$

## Axioma 7 — Ley asociativa de la multiplicación por escalares

$$a(bx) = a(bx_i) = (abx_i) = (ab)x$$

usando asociatividad de la multiplicación en $\mathbb{R}$.

## Axioma 8 — Ley distributiva respecto de la adición en $V$

$$a(x + y) = a(x_i + y_i) = (ax_i + ay_i) = ax + ay$$

usando distributividad en $\mathbb{R}$.

## Axioma 9 — Ley distributiva respecto de la adición de escalares

$$(a + b)x = ((a+b)x_i) = (ax_i + bx_i) = ax + bx$$

## Axioma 10 — Existencia del elemento idéntico

$$1 \cdot x = (1 \cdot x_i) = (x_i) = x$$
