Buena pregunta. La diferencia es sutil pero importante.

En el ejemplo $\mathbb{R}[t]$ el conjunto de **todos** los polinomios, sin restricción de grado, cada polinomio tiene *algún* grado $n$, pero $n$ no está fijo — puede ser 0, 1, 2, 1000, etc. Cuando sumas dos polinomios, el resultado es otro polinomio de *algún* grado, y como no hay tope, siempre cae dentro del conjunto.

Ahora, cuando fijamos un $n$ y solo admitimos polinomios cuyo grado cumpla cierta condición. Y ahí es donde aparece la diferencia:

**Grado $\leq n$:** Si $p$ tiene grado 3 y $q$ tiene grado 5 (con $n = 5$), la suma tiene grado $\leq 5$. Si hay cancelación del término líder, el grado baja, digamos a 3. Pero $3 \leq 5$, así que sigue dentro. No importa si el grado sube o baja, nunca puede superar $n$ porque el coeficiente de mayor grado posible es $a_n + b_n$, y de ahí para arriba no hay términos. **Siempre te quedas dentro.**

**Grado $= n$:** Aquí exiges que el grado sea **exactamente** $n$. El problema es la cancelación: si $p(t) = t^2 + 1$ y $q(t) = -t^2 + 3t$, ambos tienen grado exactamente 2, pero al sumarlos el término $t^2$ se cancela y obtienes $3t + 1$, que tiene grado 1. **Te saliste del conjunto.**

Entonces la clave es que $\leq$ absorbe las cancelaciones (si el grado baja, no pasa nada), mientras que $=$ no las tolera (si el grado baja, ya no cumples la condición).

# Espacio lineal de polinomios de grado $\leq n$

Sea $V_n$ el conjunto de todos los polinomios con coeficientes reales de grado $\leq n$, siendo $n$ fijo. Un elemento típico es:

$$p(t) = a_0 + a_1 t + a_2 t^2 + \cdots + a_n t^n$$

donde $a_i \in \mathbb{R}$ y se sobrentiende que el polinomio nulo siempre está incluido.

Como ya probamos que $\mathbb{R}[t]$ (el conjunto de todos los polinomios) es un espacio lineal, basta verificar que $V_n$ es un **subespacio** de $\mathbb{R}[t]$. Para ello necesitamos tres condiciones:

---

## 1. El elemento cero pertenece al conjunto

El polinomio nulo $O(t) = 0$ se considera de grado $\leq n$ para cualquier $n$ (por convención). Entonces $O \in V_n$.

## 2. Clausura bajo la adición

Sean $p(t) = \sum_{i=0}^{n} a_i t^i$ y $q(t) = \sum_{i=0}^{n} b_i t^i$ con grado $\leq n$. Su suma es:

$$(p + q)(t) = \sum_{i=0}^{n} (a_i + b_i) t^i$$

El término de mayor grado posible es $(a_n + b_n)t^n$. Si no se cancela, el grado es $n$. Si se cancela, el grado es menor. En ambos casos, grado $\leq n$, así que $p + q \in V_n$.

**Contraste con grado $= n$:** Si en cambio exigiéramos que el grado fuera **exactamente** $n$, esta cancelación sería un problema. Por ejemplo, con $n = 2$: $p(t) = t^2 + 1$ y $q(t) = -t^2 + 3t$ ambos tienen grado 2, pero $p(t) + q(t) = 3t + 1$ tiene grado 1. La suma se sale del conjunto, no hay clausura, y por lo tanto no es espacio lineal. El $\leq$ absorbe las cancelaciones; el $=$ no.

## 3. Clausura bajo multiplicación por escalar

Sea $p(t) = \sum_{i=0}^{n} a_i t^i$ con grado $\leq n$ y $\alpha \in \mathbb{R}$:

$$(\alpha p)(t) = \sum_{i=0}^{n} \alpha a_i t^i$$

El término de mayor grado posible es $\alpha a_n t^n$, que tiene grado $\leq n$. Entonces $\alpha p \in V_n$.

---

> **Nota:** Los axiomas 3–10 se heredan de $\mathbb{R}[t]$ porque si una propiedad vale para todos los polinomios, vale en particular para los de grado $\leq n$. Esta es la ventaja de demostrar subespacios: solo verificamos clausura y el resto viene gratis del espacio mayor.