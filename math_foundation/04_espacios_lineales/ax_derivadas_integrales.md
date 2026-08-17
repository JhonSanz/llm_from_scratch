# Subespacios de funciones: derivables e integrables

Como ya probamos que $\mathcal{F}(I)$ (el conjunto de todas las funciones $f: I \to \mathbb{R}$) es un espacio lineal, para los siguientes conjuntos basta verificar que son **subespacios** de $\mathcal{F}(I)$, es decir, que cumplen las tres condiciones de clausura. Los axiomas 3–10 se heredan automáticamente del espacio mayor.

---

## Funciones derivables en un punto dado

Sea $V = \{ f \in \mathcal{F}(I) : f \text{ es derivable en } c \}$, donde $c \in I$ es un punto fijo.

### 1. El elemento cero pertenece al conjunto

La función $O(t) = 0$ es derivable en $c$ (su derivada es 0). Entonces $O \in V$.

### 2. Clausura bajo la adición

Si $f$ y $g$ son derivables en $c$, entonces $f + g$ es derivable en $c$, porque:

$$(f + g)'(c) = f'(c) + g'(c)$$

Esto es un teorema del cálculo (la derivada de la suma es la suma de las derivadas). Entonces $f + g \in V$.

### 3. Clausura bajo multiplicación por escalar

Si $f$ es derivable en $c$ y $\alpha \in \mathbb{R}$, entonces $\alpha f$ es derivable en $c$, porque:

$$(\alpha f)'(c) = \alpha f'(c)$$

Entonces $\alpha f \in V$.

---

## Funciones integrables en un intervalo dado

Sea $W = \{ f \in \mathcal{F}([a, b]) : f \text{ es integrable en } [a, b] \}$.

### 1. El elemento cero pertenece al conjunto

La función $O(t) = 0$ es integrable en $[a, b]$ (su integral es 0). Entonces $O \in W$.

### 2. Clausura bajo la adición

Si $f$ y $g$ son integrables en $[a, b]$, entonces $f + g$ es integrable, porque:

$$\int_a^b (f + g) = \int_a^b f + \int_a^b g$$

Esto es un teorema del cálculo (la integral de la suma es la suma de las integrales). Entonces $f + g \in W$.

### 3. Clausura bajo multiplicación por escalar

Si $f$ es integrable en $[a, b]$ y $\alpha \in \mathbb{R}$, entonces $\alpha f$ es integrable, porque:

$$\int_a^b \alpha f = \alpha \int_a^b f$$

Entonces $\alpha f \in W$.

---

> **Nota:** Ambos casos siguen el mismo patrón: cada vez que una propiedad analítica (derivabilidad, integrabilidad) se preserva bajo suma y multiplicación por escalar, el subconjunto de funciones que la cumple forma un subespacio. Es una idea muy potente porque te permite construir muchos espacios lineales sin repetir los 10 axiomas cada vez.