# Subespacio de funciones con $f(1) = 0$

Sea $W = \{ f \in \mathcal{F}(I) : f(1) = 0 \}$, el conjunto de todas las funciones definidas en el punto 1 con $f(1) = 0$.

Como ya probamos que $\mathcal{F}(I)$ es un espacio lineal, basta verificar que $W$ es un **subespacio**.

---

## 1. El elemento cero pertenece al conjunto

$O(t) = 0$ cumple $O(1) = 0$. Entonces $O \in W$.

## 2. Clausura bajo la adición

Si $f(1) = 0$ y $g(1) = 0$, entonces:

$$(f + g)(1) = f(1) + g(1) = 0 + 0 = 0$$

Así que $f + g \in W$.

## 3. Clausura bajo multiplicación por escalar

Si $f(1) = 0$ y $\alpha \in \mathbb{R}$, entonces:

$$(\alpha f)(1) = \alpha \cdot f(1) = \alpha \cdot 0 = 0$$

Así que $\alpha f \in W$.

---

## ¿Por qué el 0 es esencial?

Si en cambio tomáramos $W_c = \{ f : f(1) = c \}$ con $c \neq 0$, la estructura se destruye por completo:

**Falla la clausura bajo la adición:** Si $f(1) = c$ y $g(1) = c$:

$$(f + g)(1) = c + c = 2c \neq c$$

La suma se sale del conjunto.

**Falla la clausura bajo multiplicación por escalar:** Si $f(1) = c$ y $\alpha \in \mathbb{R}$:

$$(\alpha f)(1) = \alpha c \neq c \quad \text{(en general)}$$

**El elemento cero no pertenece al conjunto:** $O(1) = 0 \neq c$.

> **Nota:** Un cambio aparentemente pequeño (reemplazar 0 por $c \neq 0$) destruye la estructura por completo. La condición $f(1) = 0$ es una ecuación **homogénea**, y esa homogeneidad es lo que garantiza la clausura. Este patrón aparece constantemente en álgebra lineal: las condiciones homogéneas producen subespacios, las no homogéneas no.