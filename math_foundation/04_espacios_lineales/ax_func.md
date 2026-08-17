
# Espacio lineal de funciones en un intervalo

Sea $V = \mathcal{F}(I)$ el conjunto de todas las funciones $f: I \to \mathbb{R}$, donde $I$ es un intervalo dado. Definimos las operaciones así:

**Adición:** $(f + g)(t) = f(t) + g(t)$ para todo $t \in I$

**Multiplicación por escalar:** $(af)(t) = a \cdot f(t)$ para todo $t \in I$, $a \in \mathbb{R}$

La clave es la misma idea que con $V_n$: las operaciones se definen **punto a punto**, así que heredamos las propiedades de $\mathbb{R}$. Solo que ahora en vez de $n$ componentes finitas, tienes una "componente" por cada $t \in I$.

---

## Axioma 1 — Clausura respecto de la adición

Dados $f, g \in V$, definimos $(f+g)(t) = f(t) + g(t)$. Como $f(t), g(t) \in \mathbb{R}$ y los reales son cerrados bajo la suma, $f(t) + g(t) \in \mathbb{R}$ para todo $t \in I$. Entonces $f + g$ es una función de $I$ a $\mathbb{R}$, es decir, $f + g \in V$. La unicidad viene de que la suma en $\mathbb{R}$ es única.

## Axioma 2 — Clausura respecto de la multiplicación por escalar

Dado $f \in V$ y $a \in \mathbb{R}$, definimos $(af)(t) = a \cdot f(t)$. Como $a \cdot f(t) \in \mathbb{R}$ para todo $t \in I$, entonces $af \in V$.

## Axioma 3 — Ley conmutativa

$$(f + g)(t) = f(t) + g(t) = g(t) + f(t) = (g + f)(t)$$

por conmutatividad en $\mathbb{R}$, para todo $t \in I$. Como coinciden en todo punto, $f + g = g + f$.

## Axioma 4 — Ley asociativa de la adición

$$((f+g)+h)(t) = (f(t)+g(t))+h(t) = f(t)+(g(t)+h(t)) = (f+(g+h))(t)$$

por asociatividad en $\mathbb{R}$.

## Axioma 5 — Existencia del elemento cero

Sea $O: I \to \mathbb{R}$ la función definida por $O(t) = 0$ para todo $t \in I$. Entonces:

$$(f + O)(t) = f(t) + 0 = f(t)$$

para todo $t$, así que $f + O = f$.

## Axioma 6 — Existencia de opuestos

Para $f \in V$, tomamos $(-1)f$ definida por $((-1)f)(t) = -f(t)$. Entonces:

$$(f + (-1)f)(t) = f(t) + (-f(t)) = 0 = O(t)$$

para todo $t$, así que $f + (-1)f = O$.

## Axioma 7 — Ley asociativa de la multiplicación por escalares

$$(a(bf))(t) = a \cdot (bf)(t) = a \cdot (b \cdot f(t)) = (ab) \cdot f(t) = ((ab)f)(t)$$

por asociatividad de la multiplicación en $\mathbb{R}$.

## Axioma 8 — Distributiva respecto de la adición en $V$

$$(a(f+g))(t) = a \cdot (f(t)+g(t)) = a \cdot f(t) + a \cdot g(t) = (af)(t) + (ag)(t) = (af + ag)(t)$$

por distributividad en $\mathbb{R}$.

## Axioma 9 — Distributiva respecto de la adición de escalares

$$((a+b)f)(t) = (a+b) \cdot f(t) = a \cdot f(t) + b \cdot f(t) = (af)(t) + (bf)(t) = (af + bf)(t)$$

## Axioma 10 — Existencia del elemento idéntico

$$(1 \cdot f)(t) = 1 \cdot f(t) = f(t)$$

para todo $t$, así que $1 \cdot f = f$.

---

> **Nota:** La estructura es prácticamente idéntica a la de $V_n$. En $V_n$ evalúas en la componente $i$-ésima, aquí evalúas en el punto $t$. Es como pasar de un índice discreto $i \in \{1, \ldots, n\}$ a un índice continuo $t \in I$. La lógica subyacente es la misma: **operaciones punto a punto heredan las propiedades del cuerpo base**.
